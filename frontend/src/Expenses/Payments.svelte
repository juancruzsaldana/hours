<script>
    import Icons from "../Icons/Icons.svelte";
    import Modal from "../Components/Modal.svelte";
    import NewPayment from "../Forms/NewPayment.svelte";
    import expensesService from "../services/expensesService";
    import {media_url} from "../services/appConfigService";
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
    endDate = new Date(end_date);
    let periods = [];
    for (let start = new Date(startDate) ; start <= endDate ; start.setMonth(start.getMonth() + 1)) {
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
        newPaymentPromise = expensesService.newPayment(payment, files).then(async r => {
            showModal = false;
            //TODO show success message
            setPayment(r.payment);
            
        })
    };
    const onEditPayment = async (payment, files) => {
        newPaymentPromise = expensesService.editPayment(payment.id, payment, files).then(async r => {
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
    <table class="table-fixed text-sm w-full text-xs text-violet-300 border-collapse border border-violet-500">
        <thead>
            <tr>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500">Period</th>
                {#each expenses as expense }
                    <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize break-words"> {expense.name} </th>
                {/each}
                <th class="text-center border border-violet-500 bg-violet-400 text-violet-600 capitalize font-bold text-sm">Total</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Horas</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Estimado</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Diferencia</th>
                <th class="text-center border border-violet-500 bg-violet-300 text-violet-500 capitalize">Horas Valor</th>
            </tr>
        </thead>
        <tbody>
            {#each periods as period }
                <tr>
                    <td class="pl-1 text-left border border-violet-500 capitalize font-bold">{period.label}</td>
                    {#each expenses as expense }
                        {#await paymentsPromise}
                            <td class="text-center border border-violet-500"> <Icons name="loader" tailwind="animate-spin h-2 w-2"/> </td>
                        {:then payments} 
                            <td on:click={(e) => {showEditPayment(e, period.label + expense.id)}}
                            class="text-center border border-violet-500"> 
                                {#if editingPayments.includes(period.label + expense.id)}
                                    <NewPayment  onSubmit={onSubmitFormCell} sending={newPaymentPromise} 
                                    expense={expense.id} 
                                    payment={payments[period.label + expense.id] ||  {hoursValue: rate, date: period.date, estimated: expense.amount}} 
                                    cell={period.label + expense.id} onBlur={hideEditPayment}/>
                                {:else}
                                    {#if payments[period.label + expense.id]}
                                        {#if payments[period.label + expense.id].voucher}
                                            <a  on:click|stopPropagation={ e => e} href={media_url + payments[period.label + expense.id].voucher} target="_blank"
                                            class="text-violet-500 visited:text-violet-500">
                                                {payments[period.label + expense.id ].amount || '' } 
                                            </a>
                                        {:else}
                                            <input type="file" on:click|stopPropagation={ e => e} name="" id={`voucher${payments[period.label + expense.id ].id}`} class="hidden" on:change={(e)=>{addVoucher(e, payments[period.label + expense.id ])}}>
                                            <!-- svelte-ignore a11y-invalid-attribute -->
                                            <a href="javascript:;" on:click|preventDefault|stopPropagation={addVoucherToPayment(payments[period.label + expense.id ].id)}
                                            class="text-violet-300 visited:text-violet-300">
                                                {payments[period.label + expense.id ].amount } 
                                            </a>
                                        {/if}
                                    {:else}
                                        {''}
                                    {/if}
                                {/if}   
                            </td>
                        {/await}
                    {/each}
                    <td class="text-center border border-violet-500">
                        {#await paymentsPromise}
                            <Icons name="loader" tailwind="animate-spin h-2 w-2"/>
                        {:then payments} 
                            { payments[period.label]?.total ?? '' } 
                        {/await}
                    </td>
                    <td class="text-center border border-violet-500">
                        {#await paymentsPromise}
                            <Icons name="loader" tailwind="animate-spin h-2 w-2"/>
                        {:then payments} 
                        { (payments[period.label]?.hours).toFixed(2) ?? '' } 
                        {/await}
                    </td>
                    <td class="text-center border border-violet-500">
                        {#await paymentsPromise}
                            <Icons name="loader" tailwind="animate-spin h-2 w-2"/>
                        {:then payments} 
                            { (payments[period.label]?.estimated).toFixed(2) ?? '' } 
                        {/await}
                    </td>
                    <td class="text-center border border-violet-500">
                        {#await paymentsPromise}
                            <Icons name="loader" tailwind="animate-spin h-2 w-2"/>
                        {:then payments} 
                            { (payments[period.label]?.diference).toFixed(2) ?? '' } 
                        {/await}
                    </td>
                    <td class="text-center border border-violet-500">
                        {#await paymentsPromise}
                            <Icons name="loader" tailwind="animate-spin h-2 w-2"/>
                        {:then payments}
                            { payments[period.label]?.hoursValue ?? '' } 
                        {/await} 
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>