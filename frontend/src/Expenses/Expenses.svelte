<script>
    import Dates from "../Forms/Dates.svelte";
    import Icons from "../Icons/Icons.svelte";
    import expensesService from "../services/expensesService";
    import NewExpense from "../Forms/NewExpense.svelte";
    import Payments from "./Payments.svelte";
    import {moneyFormater} from "../services/utils";
    export let rate;
    const timezoneHoursOffset = new Date().getTimezoneOffset() / 60;
    let startDate = new Date(new Date().getFullYear(), 0, 1);
    let endDate = new Date(new Date().getFullYear(), new Date().getMonth()+2, 0, 23-timezoneHoursOffset, 59, 59, 999);
    let promiseExpense = (async () => await expensesService.getExpenses(startDate?.toISOString(), endDate?.toISOString()))();
    let newExpensePromise = new Promise((resolve, reject) => resolve(true));
    let deletingId = [];
    let editingId = [];
    const getExpenses = (start_date, end_date) =>{
        startDate = new Date(start_date);
        endDate = new Date(new Date(end_date).getFullYear(), new Date(end_date).getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
        promiseExpense = (async () => await expensesService.getExpenses(startDate.toISOString(), endDate.toISOString()))();
    }
    const onNewExpense = async (expense) => {
        newExpensePromise = expensesService.newExpense(expense).then(async r => {
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

    const showEditExpense = (event, expense_id, field) =>{
        let editIds = editingId;
        editIds.push(expense_id + field);
        editingId = editIds;
        setTimeout(() => {
            event.target.querySelector('input')?.select();
            event.target.querySelector('select')?.focus();
        }, 2);
    };

    const hideEditExpense = async (expense_id, field) =>{
        let editIds = editingId;
        editIds = editIds.filter(id => id !== expense_id + field);
        editingId = editIds;
        promiseExpense = await promiseExpense;
    };

    const editExpense = async (event, expense_id) => {
        if(event.key !== 'Enter' && event.target.name !== 'type') return;
        let expensesArray = await promiseExpense;
        const field = event.target.name;
        expensesArray = expensesArray.filter(expense => expense.id === expense_id);
        let expense = expensesArray[0];
        expense[field] = event.target.value;
        if(field === 'type'){
            expense.get_type_display = event.target.selectedOptions[0].text
        }
        expensesService.editExpense(expense_id, expense).then(async r => {
            //TODO add message with result
            hideEditExpense(expense_id, field);
        });
    };
</script>

<div class="container mx-auto px-2">
    <h1 class="text-center font-bold text-lg  text-neutral-600">Expenses</h1>
    <Dates onSubmit={getExpenses} start={startDate.toISOString().split('T')[0]} end={endDate.toISOString().split('T')[0]} 
    icon="expenses" buttonText="Get Expenses" color="indigo" />
    <div class="sm:flex py-2 my-2 border-t border-neutral-800 justify-between">
        <div class="sm:w-3/5 rounded-md overflow-hidden pb-1">
            {#await promiseExpense}
                <p class="dark:text-indigo-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Expenses...</p>
            {:then expenses}
                <table class="table-auto text-sm w-full text-sm text-indigo-300 border-collapse border border-indigo-500">
                    <thead>
                        <tr class="border-b border-indigo-500 bg-indigo-200 text-indigo-400">
                            <th colspan="6" class="pr-2 py-1 text-right text-xs">Hours Value: {rate}</th>
                        </tr>
                        <tr class="text-center bg-indigo-300 text-indigo-500"><th  colspan="6">Fixed Expenses</th></tr>
                        <tr>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">#</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Nombre</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Period</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Value</th>
                            <th class="pl-1 text-left border border-indigo-500 bg-indigo-300 text-indigo-500">Hours</th>
                            <th class="text-center border border-indigo-500 bg-indigo-300 text-indigo-500">Eliminar</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each  expenses as expense, i}
                            <tr>
                                <td class="text-center border border-indigo-500 ">{i+1}</td>
                                <td on:click={(e) => {showEditExpense(e, expense.id, 'name')}} 
                                class="pl-1 text-left border border-indigo-500 w-2/5">
                                    {#if editingId.includes(expense.id + 'name')}
                                        <input on:blur={(e) => {hideEditExpense(expense.id, 'name')}}
                                               on:keydown={(e) => e.key === 'Escape'?hideEditExpense(expense.id, 'name'): true}
                                               on:keypress={(e) => editExpense(e, expense.id)} type="text" name="name" value={expense.name} 
                                               class="pr-1 w-full h-full py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                                    {:else}
                                        {expense.name}
                                    {/if}           
                                </td>

                                <td  on:click={(e) => {showEditExpense(e, expense.id, 'type')}} 
                                class="pl-1 text-left border border-indigo-500 w-1/5">
                                    {#if editingId.includes(expense.id + 'type')}
                                        <select name="type" value={expense.type}  on:blur={(e) => {hideEditExpense(expense.id, 'type')}}
                                                on:change={(e) => editExpense(e, expense.id)}
                                                class="text-indigo-100 divide-y pr-1 w-full h-full py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent">
                                                {#each expense.type_choices as {value, name}, i }
                                                    <option class="text-indigo-700 text-sm" value={value}>{name}</option>
                                                {/each}
                                        </select>
                                    {:else}
                                        {expense.get_type_display}
                                    {/if}
                                </td>

                                <td on:click={(e) => {showEditExpense(e, expense.id, 'amount')}} 
                                    class="{editingId.includes(`${expense.id}amount`)?'':"pr-1"} text-right border border-indigo-500 w-1/5">
                                    {#if editingId.includes(`${expense.id}amount`)}
                                        <input on:blur={(e)=>{hideEditExpense(expense.id, 'amount')}} 
                                               on:keydown={(e) => e.key === 'Escape'? hideEditExpense(expense.id, 'amount'):true} 
                                               on:keypress={(e) => editExpense(e, expense.id)} type="number" value={expense.amount} name="amount"
                                               class="-indent-8 pr-1 w-full h-full text-right py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                                    {:else}
                                        { moneyFormater.format( Number(expense.amount))}
                                    {/if}
                                </td>
                                <td class="pr-1 text-right border border-indigo-500">{(expense.amount/rate).toFixed(2)}</td>
                                <td class="pr-1 text-center border border-indigo-500">
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
                            <td colspan="3" class="font-bold text-right text-sm pr-1">Totals</td>
                            <td class="font-bold text-right border border-indigo-500">{moneyFormater.format(expenses.reduce((acc, expense) => acc + Number(expense.amount), 0))}</td>
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
    {#await promiseExpense}
        <div></div>
    {:then expenses}
        <div class="sm:flex justify-between">
            <Payments start_date={startDate} end_date={endDate} expenses={expenses} rate={rate}/>
        </div>
    {/await}
</div>
<style>
    input::-webkit-outer-spin-button, 
    input::-webkit-inner-spin-button { margin-left: 5px; } 
</style>