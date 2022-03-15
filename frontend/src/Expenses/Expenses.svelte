<script>
    import Dates from "../Forms/Dates.svelte";
    import Icons from "../Icons/Icons.svelte";
    import expensesService from "../services/expensesService";
    import NewExpense from "../Forms/NewExpense.svelte";
    export let rate;
    const timezoneHoursOffset = new Date().getTimezoneOffset() / 60;
    let startDate = new Date(new Date().getFullYear(), new Date().getMonth(), 1);
    let endDate = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
    let promiseExpense = (async () => await expensesService.getExpenses(startDate.toISOString(), endDate.toISOString()))();
    let newExpensePromise = new Promise((resolve, reject) => resolve(true));
    let deletingId = [];
    let editingId = [];
    const getExpenses = () => true;
    const onNewExpense = async (expense) => {
        newExpensePromise = expensesService.newExpense(expense).then(async r => {
            console.log(r, expense);
            let expensesArray = await promiseExpense;
            expensesArray.push(r.result.expense);
            promiseExpense = new Promise((resolve) => {
                resolve(expensesArray);
            });
        })
    };
    const deleteExpense = (expense_id) => {
        let delIds = deletingId;
        delIds.push(expense_id);
        deletingId = delIds;
        expensesService.deleteExpense(expense_id).then(async r => {
            let expensesArray = await promiseExpense;
            expensesArray = expensesArray.filter(expense => expense.id !== expense_id);
            promiseExpense = new Promise((resolve) => {
                resolve(expensesArray);
            });
            deletingId = delIds.filter(id => id !== expense_id);
        })
    };

    const showEditExpense = (event, expense_id) =>{
        let editIds = editingId;
        editIds.push(expense_id);
        editingId = editIds;
        setTimeout(() => {
            event.target.querySelector('input')?.select();
        }, 2);
    };

    const hideEditExpense = async (expense_id) =>{
        let editIds = editingId;
        editIds = editIds.filter(id => id !== expense_id);
        editingId = editIds;
        promiseExpense = await promiseExpense;
    };

    const editExpense = async (event, expense_id) => {
        if(event.key !== 'Enter') return;
        let expensesArray = await promiseExpense;
        expensesArray = expensesArray.filter(expense => expense.id === expense_id);
        let expense = expensesArray[0];
        expense.amount = event.target.value;
        expensesService.editExpense(expense_id, expense).then(async r => {
            //TODO add message with result
            hideEditExpense(expense_id);
        });
    };
</script>

<div class="container mx-auto">
    <h1 class="text-center font-bold text-lg  text-neutral-600">Expenses</h1>
    <Dates onSubmit={getExpenses} start={startDate.toISOString().split('T')[0]} end={endDate.toISOString().split('T')[0]} 
    icon="expenses" buttonText="Get Expenses" color="indigo" />
    <div class="sm:flex py-2 my-2 border-t border-neutral-800 justify-between">
        <div class="sm:w-3/5 rounded-md overflow-hidden pb-1">
            {#await promiseExpense}
                <p class="dark:text-indigo-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Tasks...</p>
            {:then expenses}
                <table class="table-auto text-sm w-full text-sm text-indigo-300 border-collapse border border-indigo-500">
                    <thead>
                        <tr class="border-b border-indigo-500 bg-indigo-200 text-indigo-400">
                            <th colspan="5" class="pr-2 py-1 text-right text-xs">Hours Value: {rate}</th>
                        </tr>
                        <tr class="text-center bg-indigo-300 text-indigo-500"><th  colspan="5">Fixed Expenses</th></tr>
                        <tr>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Nombre</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Period</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Value</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Hours</th>
                            <th class="text-center border border-indigo-500 bg-indigo-300 text-indigo-500">Eliminar</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each  expenses as expense}
                            <tr>
                                <td class="pl-1 text-left border border-indigo-500">{expense.name}</td>
                                <td class="pl-1 text-left border border-indigo-500">{expense.type}</td>
                                <td on:click={(e) => {showEditExpense(e, expense.id)}} 
                                    class="{editingId.includes(expense.id)?'':"pr-1"} text-right border border-indigo-500 w-1/5">
                                    {#if editingId.includes(expense.id)}
                                        <input on:blur={(e)=>{hideEditExpense(expense.id)}} on:keydown={(e) => e.key === 'Escape'? hideEditExpense(expense.id):true} on:keypress={(e) => editExpense(e, expense.id)} type="number" value={expense.amount}
                                        class="-indent-8 pr-1 w-full h-full text-right py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                                    {:else}
                                        {expense.amount}
                                    {/if}
                                </td>
                                <td class="pr-1 text-right border border-indigo-500">{(expense.amount/rate).toFixed(2)}</td>
                                <td class="pr-1 text-center border border-indigo-500">
                                    <!-- <a href="#" class="text-indigo-500 hover:text-indigo-600">Edit</a>-->
                                    <buton on:click={(e) => {deleteExpense(expense.id)}} title="Delete {expense.name}" 
                                    class="text-red-500 hover:text-red-600 cursor-pointer">
                                        <Icons name="{deletingId.includes(expense.id)?'loader':'delete'}" tailwind="{deletingId.includes(expense.id)?'animate-spin text-white':''} h-5 w-5 mx-auto stroke-0"/>
                                    </buton> 
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                    <tfoot>
                        <tr class="bg-indigo-300 text-indigo-500">
                            <td colspan="2" class="font-bold text-right text-sm pr-1">Totals</td>
                            <td class="font-bold text-right border border-indigo-500">{(expenses.reduce((acc, expense) => acc + Number(expense.amount), 0)).toFixed(2)}</td>
                            <td class="font-bold text-right border border-indigo-500">{(expenses.reduce((acc, expense) => acc + Number(expense.amount/rate), 0)).toFixed(2)}</td>
                            <td></td>
                        </tr>
                    </tfoot>
                </table>
            {/await}
        </div>
        <div class="sm:w-2/5 overflow-hidden pb-1 sm:pl-2 pt-2 sm:pt-0">
            <NewExpense onSubmit={onNewExpense} sending={newExpensePromise}/>
        </div>
    </div>
</div>
<style>
    input::-webkit-outer-spin-button, 
    input::-webkit-inner-spin-button { margin-left: 5px; } 
</style>