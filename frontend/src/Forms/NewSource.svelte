<script>
import Icons from "../Icons/Icons.svelte";
export let onSubmit;
export let buttonText = "New Source";
let source = {}

const handleSubmit = () => {
    onSubmit(source);
    source = {};
} 

</script>
<form on:submit|preventDefault={handleSubmit} enctype="multipart/form-data"
    class="sm:flex flex-wrap text-neutral-500">
    <input type="hidden" bind:value={source.id}>
    <div class="sm:w-1/4 px-1">
        <input type="text" bind:value={source.name} placeholder="Name"
        class="w-full h-7 py-0 text-xs  rounded bg-emerald-200 border border-emerald-400" />
    </div>
    <div class="sm:w-1/4 mb-2 px-1">
        <input type="text" bind:value={source.description} placeholder="Description"
        class="w-full h-7 py-0 text-xs  rounded bg-emerald-200 border border-emerald-400" />
    </div>
    <div class="sm:w-1/4 mb-2 px-1">
        <input type="number" id="amount" min="0" step="any" bind:value={source.amount} placeholder="Amount"
        class="w-full h-7 py-0 text-xs  rounded bg-emerald-200 border border-emerald-400" />
    </div>
    <div class="sm:w-1/4 mb-2 self-stretch px-1 text-xs">
        <button type=submit
            class="h-full w-full bg-emerald-900 hover:bg-emerald-800 active:bg-emerald-700 focus:outline-none border-emerald-900 border- rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-emerald-500 disabled:text-emerald-800  text-white">
            {buttonText}
        </button>
    </div>
</form>