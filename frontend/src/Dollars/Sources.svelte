<script>
    import NewSource from "../Forms/NewSource.svelte";    
    import dollarsService from "../services/dollarsService";
    import Icons from "../Icons/Icons.svelte";
    import {moneyFormater, dollarFormater} from "../services/utils";
    export let sellValue;
    let buttonText = 'New Source';
    let visibleSources = [];
    let editingId = [];
    let promiseSources = (async () =>{ 
        visibleSources = await dollarsService.getSources();
        return visibleSources;
    })();
    
    const showEditSource = (event, source_id, field) =>{
        let editIds = editingId;
        editIds.push(source_id + field);
        editingId = editIds;
        setTimeout(() => {
            event.target.querySelector('input')?.select();
        }, 2);
    };

    const hideEditSource = async (source_id, field) =>{
        let editIds = editingId;
        editIds = editIds.filter(id => id !== source_id + field);
        editingId = editIds;
        promiseSources = await promiseSources;
    };

    const onNewSource = (source) => {
        dollarsService.newSource(source).then(async (r) => {
            let sourceArray = await promiseSources;
            sourceArray.push(r.source);
            console.log(r);
            promiseSources = new Promise((resolve) => resolve(sourceArray));
            visibleSources = sourceArray;
        });
    };

    const onUpdateSource = (source) => {
        dollarsService.editSource(source.id, source).then(async (r) => {
            let sourcesArray = await promiseSources;
            promiseSources = new Promise((resolve) => {
                resolve(sourcesArray);
            });
            visibleSources = sourcesArray;
            buttonText = 'New Source';
        });
    };

    const submitSourceForm = (source) =>{
        return source.id ? onUpdateSource(source) : onNewSource(source);
    }
</script>

<h3 class="text-center font-bold text-neutral-600 mt-2 mb-2">Sources</h3>

<NewSource onSubmit={submitSourceForm} buttonText={buttonText}></NewSource>
<div class="rounded-md overflow-hidden pb-1 mt-2">
    {#await promiseSources}
        <p class="dark:text-emerald-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Sources...</p>
    {:then sources} 
        <table class="table-auto text-sm w-full text-sm text-emerald-300 border-collapse border border-emerald-500">
            <thead>
                <tr class="text-center bg-emerald-300 text-emerald-500">
                    <th colspan="4">Sources</th>
                </tr>
                <tr>
                    <th class="pl-1 text-left border border-emerald-500 bg-emerald-300 text-emerald-500">Source</th>
                    <th class="pl-1 text-left border border-emerald-500 bg-emerald-300 text-emerald-500">$</th>
                    <th class="pl-1 text-left border border-emerald-500 bg-emerald-300 text-emerald-500">AR$</th>
                    <th class="pl-1 text-left border border-emerald-500 bg-emerald-300 text-emerald-500">O</th>
                </tr>
            </thead>
            <tbody class="text-white">
                {#each visibleSources as source, i }
                    <tr>
                        <td on:click={(e) => {showEditSource(e, source.id, 'name')}} 
                            class="text-left border border-emerald-500">
                            {#if editingId.includes(source.id + 'name')}
                                <input on:blur={(e) => {hideEditSource(source.id, 'name')}}
                                on:keydown={(e) => e.key === 'Escape'?hideEditSource(source.id, 'name'): true}
                                on:keypress={(e) => {if(e.key !== 'Enter') return; return submitSourceForm(source)}} type="text" name="name" bind:value={source.name} 
                                class="text-sm pr-1 w-full h-full py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                            {:else}
                                {source.name}
                            {/if}           
                        </td>
                        <td on:click={(e) => {showEditSource(e, source.id, 'amount')}}
                            class="pl-1 text-right border border-emerald-500">
                            {#if editingId.includes(source.id + 'amount')}
                                <input on:blur={(e) => {hideEditSource(source.id, 'amount')}}
                                on:keydown={(e) => e.key === 'Escape'?hideEditSource(source.id, 'amount'): true}
                                on:keypress={(e) => {if(e.key !== 'Enter') return; return submitSourceForm(source)}} type="text" name="amount" bind:value={source.amount} 
                                class="text-sm pr-1 w-full h-full py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                            {:else}
                                {dollarFormater.format(Number(source.amount))}
                            {/if}
                        </td>
                        <td class="pl-1 text-right border border-emerald-500">
                            {moneyFormater.format(Number(source.amount * sellValue))}
                        </td>
                        <td on:click={(e) => {showEditSource(e, source.id, 'description')}} 
                            class="pl-1 text-right border border-emerald-500"> 
                            {#if editingId.includes(source.id + 'description')}
                                <input on:blur={(e) => {hideEditSource(source.id, 'description')}}
                                on:keydown={(e) => e.key === 'Escape'?hideEditSource(source.id, 'description'): true}
                                on:keypress={(e) => {if(e.key !== 'Enter') return; return submitSourceForm(source)}} type="text" name="description" bind:value={source.description} 
                                class="text-sm pr-1 w-full h-full py-0 pl-0 border-0 bg-transparent focus:border-0 focus:ouline-0 focus:shadow-none focus:ring-offset-transparent focus:ring-offset-0 focus:ring-transparent" />
                            {:else}
                                {source.description}
                            {/if}  
                        </td>
                    </tr>
                {/each}
            </tbody>
            <tfoot>
                <tr>
                    <td class="text-left border border-emerald-500">Total</td>
                    <td class="pl-1 text-right border border-gray-500 bg-amber-300 text-gray-900 font-bold text-lg">
                        {dollarFormater.format(visibleSources.reduce((acc, source) => acc + Number(source.amount), 0))}
                    </td>
                    <td class="pl-1 text-right border border-gray-500 bg-amber-300 text-gray-900 font-bold text-lg">
                        {moneyFormater.format(visibleSources.reduce((acc, source) => acc + Number(source.amount) * sellValue, 0))}
                    </td>
                    <td class="pl-1 text-right border border-emerald-500"></td>
                </tr>
            </tfoot>
        </table>
    {/await}
</div>
