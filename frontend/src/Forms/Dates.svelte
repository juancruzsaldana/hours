<script>
    export let start;
    export let end;
    export let onSubmit;
    function handleSubmit() {
        onSubmit(start, end)
    }

</script>

<form on:submit|preventDefault={handleSubmit} class="mt-3 text-xs">
    <label class="flex gap-4 justify-end content-center items-center">
        <span class="text-violet-300">Start Date</span>
        <input type="date" id="start" name="start" bind:value={start} placeholder="Start"
        class="bg-violet-200 border border-violet-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-violet-500 transition duration-150 ease-in-out sm:text-xs sm:leading-4 py-1 px-3"
        >
        <span class="text-violet-300">End Date</span>
        <input type="date" id="end" name="end" bind:value={end} placeholder="Start"
        class="bg-violet-200 border border-violet-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-violet-800 transition duration-150 ease-in-out sm:text-xs sm:leading-4 py-1 px-3"
        >
        <button disabled={!start || !end} type=submit
        class="bg-violet-500 hover:bg-violet-600 active:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-300 border-transparent px-2 py-1 rounded-md text-violet-800 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-violet-500 disabled:text-violet-800 ">
           Get Tasks</button>
    </label>
</form>