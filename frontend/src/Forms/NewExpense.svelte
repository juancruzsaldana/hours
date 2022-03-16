<script>
    import Icons from "../Icons/Icons.svelte";
    export let expense ={};
    export let onSubmit;
    export let sending;
    const handleSubmit = (e) => {
        onSubmit(expense);
        expense = {};
    }
</script>
<form on:submit|preventDefault={handleSubmit} class="text-sm sm:flex flex-wrap text-neutral-500">
    <div class="sm:w-3/4 mb-2 sm:pr-1">
        <label for="name" class="font-bold mb-1">Name</label>
        <input required type="text" id="name" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.name} placeholder="Name"/>
    </div>
    <div class="sm:w-1/4 mb-2 sm:pl-1">
        <label for="amount" class="font-bold mb-1">Amount</label>
        <input required type="number" id="amount" min="0" step="any" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.amount} placeholder="Amount"/>
    </div>
    <div class="sm:w-1/3 mb-2 sm:pr-1">
        <label for="type" class="font-bold mb-1">Type</label>
        <select id="type" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.type}>
            <option value="1">Monthly</option>
            <option value="2">Variable Monthly</option>
        </select>
    </div>
    <div class="sm:w-1/3 mb-2 sm:px-1">
        <label for="start" class="font-bold mb-1">Start</label>
        <input type="month" id="start" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.start} placeholder="Start"/>
    </div>
    <div class="sm:w-1/3 mb-2 sm:pl-1">
        <label for="end" class="font-bold mb-1">End</label>
        <input type="month" id="end" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.end} placeholder="End"/>
    </div>
    <div class="sm:w-full mb-2">
        <label for="description" class="font-bold mb-1">Description</label>
        <textarea id="description" class="w-full h-7 py-0 text-sm  rounded bg-indigo-200 border border-indigo-400" bind:value={expense.description} placeholder="Description"></textarea>
    </div>
    <div class="sm:w-full text-right">
        <button type="submit" 
        class="flex gap-2 content-center items-center bg-indigo-900 hover:bg-indigo-700 active:bg-indigo-700 focus:outline-none border-transparent border-1 px-2 py-1 rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-indigo-500 disabled:text-indigo-800 text-white ml-auto">
            {#await sending}
                <Icons name="loader" tailwind="animate-spin flex-no-shrink fill-current h-4 w-4 text-white"/>
            {:then sended} 
                <Icons name="expenses" tailwind="flex-no-shrink h-4 w-4" />
            {/await}
            New Expense
        </button>
    </div>
</form>