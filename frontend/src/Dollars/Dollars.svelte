<script>
    import dollarsService from "../services/dollarsService";
    import Icons from "../Icons/Icons.svelte";
    import {moneyFormater, dollarFormater} from "../services/utils";
    import NewMovement from "../Forms/NewMovement.svelte";
    let sellValue = 199;
    let buyValue = 204;
    let airtmSellValue = 180.469482814;
    let galiciaSellValue = 106;
    let data = [];
    let selectedMovement = {};
    let promiseMovements = (async () =>{ 
        data = await dollarsService.getMovements();
        return data;
    })();
    let newMovementPromise = new Promise((resolve, reject) => resolve(true));

    const onNewMovement = async (movement) => {
        newMovementPromise = dollarsService.newMovement(movement).then(async () => {
            data = await dollarsService.getMovements();
            promiseMovements = new Promise((resolve, reject) => resolve(data));
        });
    };

</script>

<h1 class="text-center font-bold text-lg  text-neutral-600 border-b border-neutral-600 pb-2 mb-2">Dollars</h1>
<div class="sm:flex text-sm text-stone-900 justify-between">
    <div class="account-data px-1 text-xs w-1/6">
        <p>Banco Galicia - Caja Ahorro Dólares</p>
        <p>Nro. de Cuenta: ...4440704</p>
        <p>Fecha Actual 27/07/2018</p>
        <p>Hora Actual:12:28 p.m.</p>
        <p>Intervalo de Consulta: del 27/01/2018 al 27/07/2018</p>
    </div>
    <div class="actual-values px-2">
        <form class="w-full mb-2">
            <div class="flex justify-between items-center">
                <label for="from" class="font-bold sm:mr-1">Valor de venta: </label>
                <input class="py-0" type="number" id="sellValue" bind:value={sellValue}>
            </div>
        </form>
        <form class="w-full mb-2">
            <div class="flex justify-between items-center">
                <label for="from" class="font-bold sm:mr-1">Valor de compra: </label>
                <input class="py-0" type="number" id="buyValue" bind:value={buyValue}>
            </div>
        </form>
        <form class="w-full">
            <div class="flex justify-between items-center">
                <label for="from" class="font-bold sm:mr-1">Valor de venta Airtm: </label>
                <input class="py-0" type="number" id="airtmSellValue" bind:value={airtmSellValue}>
            </div>
        </form>
    </div>
    <div class="">
        <div class="value-in-pesos sm:flex justify-between content-center items-center py-5 pl-1 pr-5 bg-green-400 mb-2">
            <label for="valueInPesos" class="font-bold">Valor en Pesos</label>
            {#await promiseMovements}
                <Icons name="loader" tailwind="animate-spin h-4 w-4"/>
            {:then _}    
                <input type="text" readonly id="valueInPesos" class="py-0 ml-2 text-right" value={moneyFormater.format(data.totals.lastPartial * sellValue)}>
            {/await}
        </div>
        <div class="flex justify-between items-center text-xs">
            <label for="from" class="font-bold sm:mr-1">Venta en Galicia: </label>
            <input class="py-0 text-xs" type="number" id="airtmSellValue" bind:value={galiciaSellValue}>
        </div>
        <div class="flex justify-between items-center text-xs">
            <label for="from" class="font-bold sm:mr-1">Con 65 %: </label>
            <input class="py-0 text-xs" type="number" id="airtmSellValue" readonly value={(galiciaSellValue * 1.65).toFixed(2)}>
        </div>
    </div>
    <div class="sm:w-1/4 pl-2">
        <NewMovement onSubmit={onNewMovement} movementProp={selectedMovement} sending={newMovementPromise}></NewMovement>
    </div>
</div>
<div class="sm:flex px-1">
    <div class="rounded-md overflow-hidden pb-1 mt-4 w-3/4">
        {#await promiseMovements}
            <p class="dark:text-gray-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Movements...</p>
        {:then _}
            <table class="table-auto text-sm w-full bg-neutral-200 text-neutral-900 border-collapse border border-gray-500">
                <thead>
                    <tr>
                        <th class="pl-1 text-left border border-gray-500 bg-gray-300 text-gray-500">#</th>
                        <th class="pl-1 text-left border border-gray-500 bg-gray-300 text-gray-500">Fecha</th>
                        <th class="pl-1 text-left border border-gray-500 bg-gray-300 text-gray-500">Movimiento</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Monto</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Saldo Parcial</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Monto en pesos</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Cotización</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Saldo Individual</th>
                        <th class="pr-1 text-center border border-gray-500 bg-gray-300 text-gray-500">Valor en cotización Actual</th>
                    </tr>
                </thead>
                <tbody>
                    {#each data.movements as movement, i }
                        <tr>
                            <td class="text-center border border-gray-500">{i+1}</td>
                            <td class="text-center border border-gray-500">{movement.date}</td>
                            <td title={movement.name}
                            class="text-left border border-gray-500 truncate max-w-[12rem]">{movement.name}</td>
                            <td class={`text-right border border-gray-500 ${movement.amountInDollars < 0? 'text-red-600':''}`}>
                                {dollarFormater.format(movement.amountInDollars)}
                            </td>
                            <td class={`text-right border border-gray-500 ${i === 0? 'font-bold': ''}`}>
                                {dollarFormater.format(movement.partial)}
                            </td>
                            <td class={`text-right border border-gray-500 ${movement.amountInPesos < 0? 'text-red-600':''}`}>
                                {moneyFormater.format(movement.amountInPesos)}
                            </td>
                            <td class={`text-right border border-gray-500 ${movement.quote > buyValue? 'text-red-600':'text-green-600 bg-neutral-400'} `}>
                                {movement.quote}
                            </td>
                            {#if movement.sellValue === "2"}
                                <td class={`text-right border border-gray-500 ${movement.amountInDollars * airtmSellValue -  movement.amountInPesos < 0 ? 'text-red-600 bg-red-300': 'bg-green-300 text-green-600'}`}>
                                    {moneyFormater.format(movement.amountInDollars * airtmSellValue -  movement.amountInPesos)}
                                </td>
                                <td class={`text-right border border-gray-500 ${movement.amountInDollars * airtmSellValue < 0 ? 'text-red-700': ''}`}>
                                    {moneyFormater.format(movement.amountInDollars * airtmSellValue)}
                                </td>
                            {:else}    
                                <td class={`text-right border border-gray-500 ${movement.amountInDollars * sellValue -  movement.amountInPesos < 0 ? 'text-red-600 bg-red-300': 'bg-green-300 text-green-600'}`}>
                                    {moneyFormater.format(movement.amountInDollars * sellValue -  movement.amountInPesos)}
                                </td>
                                <td class={`text-right border border-gray-500 ${movement.amountInDollars * sellValue < 0 ? 'text-red-700': ''}`}>
                                    {moneyFormater.format(movement.amountInDollars * sellValue)}
                                </td>
                            {/if}
                        </tr>
                    {/each}
                </tbody>
                <tfoot>
                    <tr>
                        <td class="pl-1 text-left border border-gray-500 bg-gray-300 text-gray-500 font-bold" colspan="2">Totales</td>
                        <td class="pr-5 text-right border border-gray-500 bg-gray-300 text-gray-500 font-bold" colspan="3">
                            Debit : {dollarFormater.format(data.totals.totalDebit)}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Credit : {dollarFormater.format(data.totals.totalCredit)}
                        </td>
                        <td class="pl-1 text-right border border-gray-500 bg-gray-300 text-gray-500 font-bold">
                            {moneyFormater.format(data.totals.totalInPesos)}
                        </td>
                        <td class="pl-1 text-right border border-gray-500 bg-gray-300 text-gray-500 font-bold">
                            {data.totals.quoteAvg}
                        </td>
                        <td class="pl-1 text-right border border-gray-500 bg-amber-300 text-gray-900 font-bold text-lg">
                            {moneyFormater.format(data.movements.reduce((acc, m) => {
                                let multiplier = m.sellValue === "2"? airtmSellValue : sellValue;
                                return acc + (m.amountInDollars * multiplier - m.amountInPesos)
                            }, 0))}
                        </td>
                        <td class="pl-1 text-right border border-gray-500 bg-amber-300 text-gray-900 font-bold text-lg">
                            {moneyFormater.format(data.movements.reduce((acc, m) => {
                                let multiplier = m.sellValue === "2"? airtmSellValue : sellValue;
                                return acc + (m.amountInDollars * multiplier)
                            }, 0))}
                        </td>
                    </tr>
                </tfoot>
            </table>
        {/await} 
    </div>
    <div class="w-1/4">
            graphs
    </div>
</div>