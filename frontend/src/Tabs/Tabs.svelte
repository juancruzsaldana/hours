<script>
    import { onMount } from "svelte";
  
    export let items = [];
    export let activeTabValue;
  
    onMount(() => {
      // Set default tab value
      if (Array.isArray(items) && items.length && items[0].value) {
        activeTabValue = items[0].value;
      }
    });
  
    const handleClick = tabValue => () => (activeTabValue = tabValue);
  </script>

<ul class="flex flex-wrap -mb-px">
    {#if Array.isArray(items)}
      {#each items as {pid, tasks}, i}
        <li class="{activeTabValue === i ? 'active' : ''} mr-2">
          <!-- svelte-ignore a11y-invalid-attribute -->
          <a href="#" class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg border-b-2 border-transparent hover:text-gray-600 hover:border-gray-300 dark:text-gray-400 dark:hover:text-gray-300 hover:no-underline" on:click={handleClick(i)}>{pid}</a>
        </li>
      {/each}
    {/if}
  </ul>