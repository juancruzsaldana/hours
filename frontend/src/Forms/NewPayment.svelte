<script>
    import { tick } from 'svelte';
    import Icons from "../Icons/Icons.svelte";
    export let payment ={};
    export let onSubmit;
    export let sending;
    export let expenses;
    export let expense;
    export let cell;
    export let onBlur;
    
    payment.expense = payment.expense ?? expense ?? '';

    let files;
    const handleSubmit = async (e) => {
        onSubmit(payment, files);
        await tick();
        payment = {};
    }
    const selectExpense = (event) => {
        const expense_id = event.target.value;
        const selectedExpense = expenses.find(expense => expense.id == expense_id);
        payment.estimated = selectedExpense.amount;
    }

</script>
<form on:submit|preventDefault={handleSubmit} enctype="multipart/form-data"
class="text-sm sm:flex flex-wrap text-neutral-500 {cell? 'p-0 w-full justify-end':'p-4'}">
    {#if cell}
        <input type="number" id="amount" min="0" step="any" bind:value={payment.amount} on:blur={onBlur(cell)}
        class="h-4 p-0 text-sm rounded-0 w-full !bg-transparent text-right border-0 grow inner-cell" />
    {:else}    
        <input type="hidden" name="hoursValue" bind:value={payment.hoursValue}>
        <input type="hidden" name="estimated" bind:value={payment.estimated}>
        <div class="sm:w-1/2">
            <label for="expense" class="font-bold mb-1">Expense</label>
            <select id="expense" bind:value={payment.expense} required  on:change={(e) => selectExpense(e)}
                class="w-full h-7 py-0 text-sm  rounded bg-violet-200 border border-violet-400">
                <option value="">Select Expense...</option>
                {#each expenses as expense }
                <option value="{expense.id}"> {expense.name} </option>
                {/each}
            </select>
        </div>
        <div class="sm:w-1/2 sm:pl-1">
            <label for="date" class="font-bold mb-1">Date</label>
            <input type="date" bind:value={payment.date}
            class="w-full h-7 py-0 text-sm  rounded bg-violet-200 border border-violet-400" />
        </div>
        <div class="sm:w-full mb-2">
            <label for="amount" class="font-bold mb-1">Amount</label>
            <input required type="number" id="amount" min="0" step="any" bind:value={payment.amount} placeholder="Amount"
            class="w-full h-7 py-0 text-sm  rounded bg-violet-200 border border-violet-400" />
        </div>
        <div class="sm:w-full mb-2">
            <input type="file" name="voucher" id="voucher" bind:files
            class="block w-full text-sm text-slate-500 rounded file:mr-4 file:py-2 file:px-4 file:rounded file:text-sm file:font-semibold
                    file:bg-violet-900 file:text-violet-700
                    hover:file:bg-violet-100 "/>
        </div>
        <div class="sm:w-full mb-2">
            <label for="description" class="font-bold mb-1">Description</label>
            <textarea id="description" bind:value={payment.description} placeholder="Description"
            class="w-full h-7 py-0 text-sm  rounded bg-violet-200 border border-violet-400" />
        </div>
        <div class="sm:w-full text-right">
            <button type="submit" 
            class="flex gap-2 content-center items-center bg-violet-900 hover:bg-violet-700 active:bg-violet-700 focus:outline-none border-transparent border-1 px-2 py-1 rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-violet-500 disabled:text-violet-800 text-white ml-auto">
            {#await sending}
                <Icons name="loader" tailwind="animate-spin flex-no-shrink fill-current h-4 w-4 text-white"/>
            {:then sended} 
                <Icons name="cash-o" tailwind="flex-no-shrink h-4 w-4" />
            {/await}
                New Expense
            </button>
        </div>

    {/if}
</form>
<style>
    input.inner-cell::-webkit-outer-spin-button, 
    input.inner-cell::-webkit-inner-spin-button { margin-left: 5px; } 
</style>