<script>
    export let movement;
    export let onSubmit;
    const movementStructure = {
        name: "",
        date: "",
        amountInPesos: '',
        amountInDollars: '',
        amountInLocal: '',
        localCurrency: "",
        localCurrencyCode: "",
    }
    let movement_detail = {
        movement: movement.id,
        ...movementStructure
    };
</script>

<form on:submit|preventDefault={ () =>{ onSubmit(movement_detail); return movement_detail = {movement: movement.id, ...movementStructure};}} class="sm:flex justify-between text-neutral-500 items-center text-xs flex-wrap sm:px-1 border-b border-green-600 pb-2">
    <input type="hidden" name="movement" bind:value={movement_detail.movement}>
    <label class="sm:w-full block text-gray-700 text-xs font-bold mb-2" for="name">
        New Movement Detail
    </label>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Name" bind:value="{movement_detail.name}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="date" type="date" bind:value="{movement_detail.date}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="amountInPesos" type="number" step="any" placeholder="Amount in Pesos" bind:value="{movement_detail.amountInPesos}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="amountInDollars" type="number" step="any" placeholder="Amount in Dollars" bind:value="{movement_detail.amountInDollars}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="amountInLocal" type="number" step="any" placeholder="Amount in Local" bind:value="{movement_detail.amountInLocal}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="localCurrency" type="text" placeholder="Local Currency" bind:value="{movement_detail.localCurrency}">
    </div>
    <div class="sm:w-1/2 p-1">
        <input class="text-xs shadow appearance-none border rounded w-full py-1 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="localCurrencyCode" type="text" placeholder="Local Currency Code" bind:value="{movement_detail.localCurrencyCode}">
    </div>
    <div class="sm:w-1/2 p-1">
        <button type=submit
            class="h-full py-1 w-full bg-emerald-900 hover:bg-emerald-800 active:bg-emerald-700 focus:outline-none border-emerald-900 border- rounded disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-emerald-500 disabled:text-emerald-800  text-white">
            New Detail
        </button>
    </div>
</form>