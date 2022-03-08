<script>
    import Icons from "../Icons/Icons.svelte";
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
        class="flex gap-2 content-center items-center bg-red-900 hover:bg-white active:bg-violet-700 focus:outline-none focus:ring focus:ring-red-300 border-red-900 border-2 px-2 py-1 rounded-md disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-red-500 disabled:text-red-800  text-white hover:text-red-900">
        <Icons name="toggl" tailwind="flex-no-shrink fill-current h-4 w-4 text-[#e00000]" />
           Get Tasks from Toggl
        </button>
    </label>
</form>