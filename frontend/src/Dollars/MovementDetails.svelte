<script>
    import {moneyFormater, dollarFormater, dynamicMoney} from "../services/utils";
    const moneyLang ={
        'BRL' : 'pt-BR',
    }
    export let movement;
    export let details;
</script>
<div class="rounded-md overflow-hidden pb-1 mt-2">
    <p class="text-xs mb-0">
        <strong>Movement Total: </strong> {dollarFormater.format(movement.amountInDollars > 0 ? movement.amountInDollars : movement.amountInDollars * -1)}
    </p>
    <table class="table-auto text-xs w-full text-emerald-300 border-collapse border border-emerald-500">
        <thead>
            <tr>
                <th  class="pl-1 text-center border border-emerald-500 bg-emerald-300 text-emerald-500">Name</th>
                <th  class="pl-1 text-center border border-emerald-500 bg-emerald-300 text-emerald-500">Pesos</th>
                <th  class="pl-1 text-center border border-emerald-500 bg-emerald-300 text-emerald-500">Dollars</th>
                <th  class="pl-1 text-center border border-emerald-500 bg-emerald-300 text-emerald-500">Local</th>
            </tr>
        </thead>
        <tbody class="text-neutral-900">
            {#if details.length}    
                {#each details as detail }
                    <tr>
                        <td class="text-center border border-emerald-500">{detail.name}</td>
                        <td class="text-right border border-emerald-500">{moneyFormater.format(Number(detail.amountInPesos))}</td>
                        <td class="text-right border border-emerald-500">{dollarFormater.format(Number(detail.amountInDollars))}</td>
                        <td class="text-right border border-emerald-500">{dynamicMoney(moneyLang[detail.localCurrencyCode],detail.localCurrencyCode).format(Number(detail.amountInLocal))}</td>
                    </tr>
                {/each}
            {:else}
                <tr>
                    <td class="text-center border border-emerald-500" colspan="5">No details</td>
                </tr>
            {/if}
        </tbody>
        {#if details.length}  
            <tfoot class="text-neutral-900">
                <tr>
                    <td class="pl-1 text-center border border-emerald-500 bg-emerald-300 font-bold">Total</td>
                    <td class="text-right pr-1 border border-emerald-500 bg-emerald-300">{moneyFormater.format(details.reduce((acc, d) => {
                            return acc + Number(d.amountInPesos)
                        }, 0))}
                    </td>
                    <td class="text-right pr-1 border border-emerald-500 bg-emerald-300">{dollarFormater.format(details.reduce((acc, d) => {
                            return acc + Number(d.amountInDollars)
                        }, 0))}
                    </td>
                    <td></td>
                </tr>
            </tfoot>
        {/if}
    </table>
</div>