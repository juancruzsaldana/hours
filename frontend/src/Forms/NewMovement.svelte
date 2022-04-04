<script>
    import Icons from "../Icons/Icons.svelte";
    export let onSubmit;
    export let sending;
    const initialMovementStructure ={
        name: '',
        amountInDollars: 0,
        amountInPesos: 0,
        type: "1",
        sellValue: "1",
        date: new Date().toISOString().substring(0, 10),
    }
    export let movementProp;
    let movement = { ...movementProp, ...initialMovementStructure};

    const handleSubmit = (e) => {
        onSubmit(movement);
        movement= initialMovementStructure;
    };
</script>

<form on:submit|preventDefault={handleSubmit} class="sm:flex justify-between text-neutral-500 items-center text-xs flex-wrap sm:px-1">
    <div class="sm:w-1/2 mb-2 sm:pr-1">
        <label for="date" class="font-bold sm:mr-1">Date</label>
        <input type="date" id="date" class="w-full h-6 py-0 rounded bg-emerald-200 border border-emerald-400 text-xs" bind:value={movement.date} placeholder="Date"/>
    </div>
    <div class="sm:w-1/2 mb-2">
        <label for="type" class="font-bold sm:mr-1">Type</label>
        <select id="type" class="w-full h-6 py-0 rounded bg-emerald-200 border border-emerald-400" bind:value={movement.type}>
            <option value="1">Crédito</option>
            <option value="2">Débito</option>
        </select>
    </div>
    <div class="w-full mb-2">
        <input type="hidden" name="movementId" id="movementId" bind:value={movement.id}>
        <label for="name" class="font-bold sm:mr-1">Movement</label>
        <input type="text" id="movement" bind:value={movement.name} placeholder="Movement"
        class="sm:mr-1 h-6 w-full py-0 text-sm rounded bg-emerald-200 border border-emerald-400" />
    </div>
    <div class="sm:w-1/2 mb-2 sm:pr-1">
        <label for="amountInDollars" class="font-bold">Dollars $</label>
        <input type="number" step="any" id="amountInDollars" bind:value={movement.amountInDollars} placeholder="Dollars $"
        class="sm:mr-1 h-6 w-full py-0 text-sm rounded bg-emerald-200 border border-emerald-400"/>
    </div>
    <div class="sm:w-1/2 mb-2">
        <label for="amountInPesos" class="font-bold">Pesos $</label>
        <input type="number" step="any" id="amountInPesos" bind:value={movement.amountInPesos} placeholder="Pesos $"
        class="sm:mr-1 h-6 w-full py-0 text-sm rounded bg-emerald-200 border border-emerald-400"/>
    </div>
    <div class="sm:w-full justify-between flex">
        <select id="sellValue" class="h-6 py-0 rounded bg-emerald-200 border border-emerald-400" bind:value={movement.sellValue}>
            <option value="1">Default</option>
            <option value="2">AIRTM</option>
        </select>
        <button type="submit" 
        class="flex gap-2 content-center items-center bg-lime-900 hover:bg-lime-700 active:bg-lime-700 focus:outline-none border-transparent border-1 px-2 py-1 rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-lime-500 disabled:text-lime-800 text-white ml-auto">
            {#await sending}
                <Icons name="loader" tailwind="animate-spin flex-no-shrink fill-current h-4 w-4 text-white"/>
            {:then sended} 
                <Icons name="dollars" tailwind="flex-no-shrink h-4 w-4" />
            {/await}
            New Movement
        </button>
    </div>
</form>

