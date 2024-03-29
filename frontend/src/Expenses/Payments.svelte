<script>
    import Icons from "../Icons/Icons.svelte";
    import Modal from "../Components/Modal.svelte";
    import NewPayment from "../Forms/NewPayment.svelte";
    import expensesService from "../services/expensesService";
    import {media_url} from "../services/appConfigService";
    import {moneyFormater} from "../services/utils";
    export let expenses;
    export let start_date;
    export let end_date;
    export let rate;
    let newPaymentPromise = new Promise((resolve, reject) => resolve(true));
    let paymentsPromise = new Promise((resolve, reject) => resolve(true));
    $: startDate = new Date(start_date);
    $: endDate = new Date(end_date);
    paymentsPromise = (async () => {
        let r = await expensesService.getPayments(start_date?.toISOString(), end_date?.toISOString())
        return r;
    })();
    
	startDate = new Date(start_date);
    let startWithoutOffset = new Date(startDate.getTime() + startDate.getTimezoneOffset() * 60000);
    endDate = new Date(end_date);
    let endWithoutOffset = new Date(endDate.getTime() + endDate.getTimezoneOffset() * 60000);
    let periods = [];
    for (let start = startWithoutOffset ; start <= endWithoutOffset ; start.setMonth(start.getMonth() + 1)) {
        periods.unshift({
            label: start.toLocaleString('default', { month: 'short', year: 'numeric' }),
            date: start.getTime(),
        });
    }

    let showModal = false;
    const setPayment = async (payment) => {
        let key = expensesService.getKeyFromPayment(payment);
        let paymentsObjects = await paymentsPromise;
        paymentsObjects = {...paymentsObjects, [key]: payment};
        paymentsPromise = expensesService.refreshPayments(paymentsObjects);
    }
    const onNewPayment = async (payment, files) => {
        const expense = expenses.find(e => e.id === payment.expense);
        let filename = `${expense.name}_${new Date(payment.date).toISOString()}`;
        newPaymentPromise = expensesService.newPayment(payment, files, filename).then(async r => {
            showModal = false;
            //TODO show success message
            setPayment(r.payment);
            
        })
    };
    const onEditPayment = async (payment, files) => {
        const expense = expenses.find(e => e.id === payment.expense);
        let filename = `${expense.name}_${new Date(payment.date).toISOString()}`;
        newPaymentPromise = expensesService.editPayment(payment.id, payment, files, filename).then(async r => {
            //TODO show success message
            setPayment(r.payment);
        })
    };
    const onDeletePayment = async (payment_id) => {
        return new Promise((resolve, reject) => {
            newPaymentPromise = expensesService.deletePayment(payment_id).then(r => {
                resolve(r);
            })
        });
    };
    let editingPayments = [];
    const showEditPayment = (event, cell) => {
        if(!cell){
            return;
        }
        editingPayments.push(cell);
        editingPayments = editingPayments
        setTimeout(() => {
            event.target.querySelector('input')?.select();
        }, 2);
    };

    const hideEditPayment = ( cell) => {
        editingPayments = editingPayments.filter(id => id !== cell);
    };

    const onSubmitFormCell = async (payment) => {
        const key = expensesService.getKeyFromPayment(payment);
        if(payment.id && !payment.amount){
            await onDeletePayment(payment.id);
            let paymentsObjects = await paymentsPromise;
            delete paymentsObjects[key];
            paymentsPromise = expensesService.refreshPayments(paymentsObjects);
            hideEditPayment(key);
            return;
        }
        if(payment.id){
            onEditPayment(payment);
            return;
        }
        onNewPayment(payment);
    }
    const addVoucherToPayment = (key) => {
        document.getElementById(`voucher${key}`)?.click();
    }
    const addVoucher = (event, payment) => {
        onEditPayment(payment, event.target.files);
    }
</script>
{#if showModal}
<Modal on:close={()=>showModal = false}>
    <h2 slot="title" class="font-bold text-violet-600 text-md">New Payment</h2>
    <NewPayment onSubmit={onNewPayment} sending={newPaymentPromise} expenses={expenses} payment={{hoursValue: rate}}/>
</Modal>   
{/if}
<div class="sm:w-full rounded-md overflow-hidden pb-1">
    <div class="flex w-full justify-end mb-1">
        <button on:click="{() => showModal = true}" 
        class="text-sm flex gap-2 content-center items-center bg-violet-900 hover:bg-violet-700 active:bg-violet-700 focus:outline-none border-transparent border-1 px-2 py-1 rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-violet-500 disabled:text-violet-800 text-white">
            <Icons name="cash-o" tailwind="flex-no-shrink h-5 w-5" />
            New Payment
        </button>
    </div>
    <table class="table-fixed text-sm w-full text-xs text-violet-300 border-collapse border border-violet-500 mb-4">
        <thead>
            <tr>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500">Period</th>
                {#each expenses as expense }
                    <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize break-words"> {expense.name} </th>
                {/each}
                <th class="text-center border border-violet-500 bg-violet-400 text-violet-600 capitalize font-bold text-sm">Total</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Hours</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Estimate</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Diference</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Hours Value</th>
            </tr>
        </thead>
        <tbody class="text-xs">
            {#each periods as period }
                <tr>
                    <td title={period.label}
                    class="pl-1 text-left border border-violet-500 capitalize font-bold truncate">{period.label}</td>
                    {#each expenses as expense }
                        {#await paymentsPromise}
                            <td class="text-center border border-violet-500"> <Icons name="loader" tailwind="animate-spin h-2 w-2"/> </td>
                        {:then payments} 
                            <td title={payments[period.label + expense.id]?.amount ?? ''} on:click={(e) => {showEditPayment(e, period.label + expense.id)}}
                            class="text-right border border-violet-500 relative trunctate {payments[period.label + expense.id]?.description? 'with-description pointer before:content-[""] before:block before:absolute before:top-0 before:right-0 before:h-1 before:w-1 before:border-4 before:border-b-transparent before:border-l-transparent before:border-red-500': ''}"> 
                                {#if editingPayments.includes(period.label + expense.id)}
                                    <NewPayment  onSubmit={onSubmitFormCell} sending={newPaymentPromise} 
                                    expense={expense.id} 
                                    payment={payments[period.label + expense.id] ||  {hoursValue: rate, date: period.date, estimated: expense.amount}} 
                                    cell={period.label + expense.id} onBlur={hideEditPayment}/>
                                {:else}
                                    {#if payments[period.label + expense.id]}

                                        {#if payments[period.label + expense.id].description}
                                            <div class="comment-tooltip absolute bg-orange-200 py-3 px-2 text-xv rounded-sm shadow-[2px_2px_2px_3px_rgba(0,0,0,1)] text-black z-10 left-full bottom-full">
                                                {payments[period.label + expense.id].description}
                                            </div>
                                        {/if}

                                        {#if payments[period.label + expense.id].voucher}
                                            <a  on:click|stopPropagation={ e => e} href={media_url + payments[period.label + expense.id].voucher} target="_blank"
                                            class="text-violet-500 visited:text-violet-500">
                                                {moneyFormater.format(payments[period.label + expense.id ].amount) || '' } 
                                            </a>
                                        {:else}
                                            <input type="file" on:click|stopPropagation={ e => e} name="" id={`voucher${payments[period.label + expense.id ].id}`} class="hidden" on:change={(e)=>{addVoucher(e, payments[period.label + expense.id ])}}>
                                            <!-- svelte-ignore a11y-invalid-attribute -->
                                            <a href="javascript:;" on:click|preventDefault|stopPropagation={addVoucherToPayment(payments[period.label + expense.id ].id)}
                                            class="text-violet-300 visited:text-violet-300">
                                                {moneyFormater.format(payments[period.label + expense.id ].amount) } 
                                            </a>
                                        {/if}
                                    {:else}
                                        {''}
                                    {/if}
                                {/if}   
                            </td>
                        {/await}
                    {/each}
                    {#await paymentsPromise}
                        <td><Icons name="loader" tailwind="animate-spin h-2 w-2"/></td>
                    {:then payments} 
                        <td title={payments[period.label]?.total ?? '' }  
                        class="text-center border border-violet-500 bg-violet-300 font-bold text-violet-600 truncate">
                            {payments[period.label]? moneyFormater.format(payments[period.label]?.total ?? 0) :'' } 
                        </td>
                    {/await}
                    {#await paymentsPromise}
                        <td><Icons name="loader" tailwind="animate-spin h-2 w-2"/></td>
                    {:then payments} 
                        <td title={ (payments[period.label]?.hours).toFixed(2) ?? '' } 
                        class="text-right border border-violet-500 font-semibold truncate">
                            { (payments[period.label]?.hours).toFixed(2) ?? '' } 
                        </td>
                    {/await}
                    {#await paymentsPromise}
                       <td><Icons name="loader" tailwind="animate-spin h-2 w-2"/></td>
                    {:then payments} 
                        <td title={payments[period.label]?.estimated ?? ''} 
                        class="text-right border border-violet-500 font-semibold truncate">
                            {payments[period.label]? moneyFormater.format(payments[period.label]?.estimated ?? 0) :'' } 
                        </td>
                    {/await}
                    {#await paymentsPromise}
                        <td><Icons name="loader" tailwind="animate-spin h-2 w-2"/></td>
                    {:then payments} 
                        <td title={payments[period.label]?.diference ?? '' }
                        class="text-right border border-violet-500 font-semibold truncate">
                            {payments[period.label]? moneyFormater.format(payments[period.label]?.diference ?? 0) :'' } 
                        </td>
                    {/await}
                    {#await paymentsPromise}
                        <td><Icons name="loader" tailwind="animate-spin h-2 w-2"/></td>
                    {:then payments}
                        <td title={ payments[period.label]?.hoursValue ?? '' } 
                        class="text-right border border-violet-500 font-semibold truncate">
                            { payments[period.label]?.hoursValue ?? '' } 
                        </td>
                    {/await} 
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    .comment-tooltip{
        display: none;
    }
    td.with-description:hover .comment-tooltip{
        display: block;
    }
</style>