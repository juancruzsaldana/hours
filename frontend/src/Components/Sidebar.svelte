<script>
	import Icons from "../Icons/Icons.svelte";
    import {Link} from 'svelte-navigator';
    export let items;
    export let home;
    let showSidebar = false;
	const toggleSidebar = () => {
		showSidebar = !showSidebar;
	};
</script>
<div class={`${showSidebar?'sm:w-2/12 md:2/12':'sm:w-12 md:w-12'} w-full flex-shrink flex-grow-0 sticky top-0 transition-all`}>
    <div class="sticky top-0 dark:bg-blue-900 w-full sm:min-h-screen">
        <div class="hidden sm:flex  sm:pt-4 {showSidebar?'justify-end pr-2':'justify-center'} ">
            <button on:click={(e) => {toggleSidebar()}} class="flex text-white border-0 mb-3 hover:text-blue-500">
                    {#if showSidebar}
                        <Icons name="close" tailwind="w-5 h-5"/>
                    {:else}	
                        <Icons name="menu" tailwind="w-5 h-5 transition-all "/>
                    {/if}
            </button>
        </div>
        <nav class="">					
            <ul class="flex sm:flex-col overflow-hidden content-center justify-around sm:justify-between space-y-2 sm:divide-y sm:divide-stone-900">
                {#each items as item}
                    <li class="!mt-0">
                        <Link title="{item[0].toUpperCase() + item.slice(1)}"  to="/{item !== home?item:''}" getProps
                        class="w-full hover:bg-blue-500 flex align-center font-bold hover:no-underline py-2 gap-2 px-2 {showSidebar?'justify-start':'justify-center sm:px-0'}">
                            <Icons name={item} tailwind="w-6 h-6 text-white"/>
                            <span class={`hidden capitalize text-white ${showSidebar?'sm:inline':''}`}>{item}</span>
                        </Link>
                    </li>
                {/each}
            </ul>
        </nav>
    </div>
</div>
<style lang="postcss" global>
	a[aria-current="page"] {
		background-color: rgb(63 131 248); /*@apply directive show an svelte error */
	}
</style>