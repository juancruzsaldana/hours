<script>
    import {Link} from 'svelte-navigator';
    import Icons from '../Icons/Icons.svelte';
    export let sections;
    export let home
</script>

<h1 class="text-center font-bold text-lg  text-zinc-600">WELCOME!</h1>
<div class="flex justify-around items-center flex-grow flex-wrap">
    {#each sections as section }
        {#if section !== home}
            <div class="card flex flex-col justify-between rounded-lg shadow-md dark:border-gray-700 w-1/5 saturate-50 hover:saturate-150 relative">
                <img class="rounded-t-lg object-fill h-48 w-full" src="./imgs/{section}.jpg" alt={section} />
                <Link title="{section.toUpperCase() + section.slice(1)}"  to="/{section}"
                        class="after:absolute after:inset-0 flex items-center text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-b-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                            <Icons name={section} tailwind="w-6 h-6 text-white"/>
                            <span class={`capitalize text-white ml-2`}>{section}</span>
                </Link>
            </div>
        {/if}
        
    {/each}
</div>