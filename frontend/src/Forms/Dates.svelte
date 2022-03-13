<script>
    import Icons from "../Icons/Icons.svelte";
    export let start;
    export let end;
    export let onSubmit;
    export let icon;
    export let color;
    export let buttonText;
    function handleSubmit() {
        onSubmit(start, end)
    }

</script>

<form on:submit|preventDefault={handleSubmit} class="mt-3 text-xs">
    <label class="flex gap-4 justify-end content-center items-center">
        <span class="text-{color}-300">From :</span>
        <input type="date" id="start" name="start" bind:value={start} placeholder="Start"
        class="bg-{color}-200 border border-{color}-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-{color}-500 transition duration-150 ease-in-out sm:text-xs sm:leading-4 py-1 px-3"
        />
        <span class="text-{color}-300">To :</span>
        <input type="date" id="end" name="end" bind:value={end} placeholder="Start"
        class="bg-{color}-200 border border-{color}-300 rounded-md text-sm shadow-sm placeholder-slate-400 focus:outline-none focus:border-{color}-800 transition duration-150 ease-in-out sm:text-xs sm:leading-4 py-1 px-3"
        />
        <button disabled={!start || !end} type=submit
        class="flex gap-2 content-center items-center bg-{color}-900 hover:bg-white active:bg-{color}-700 focus:outline-none border-{color}-900 border-2 px-2 py-1 rounded-md disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-{color}-500 disabled:text-{color}-800  text-white hover:text-{color}-900">
        <Icons name={icon} tailwind="flex-no-shrink h-5 w-5" />
           {buttonText}
        </button>
    </label>
</form>
