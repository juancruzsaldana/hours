<script>
    export let items = [];
    export let activeTabValue;
  
    const handleClick = tabValue => () => (activeTabValue = tabValue);

    const changeBorderColor = (element, color) => {
      element.style.borderBottomColor = color;
    };
  </script>

<ul class="flex flex-wrap -mb-px">
    {#if Array.isArray(items)}
      {#each items as {pid, tasks, project}, i}
        <li class="{activeTabValue === i ? 'active' : ''} mr-2">
          <!-- svelte-ignore a11y-mouse-events-have-key-events -->
          <button style:color={project.data.hex_color} on:mouseleave={(e) => changeBorderColor(e.target, 'transparent')} on:mouseover={(e) => changeBorderColor(e.target, project.data.hex_color)}  on:click={handleClick(i)}
            class="font-bold inline-block py-4 px-4 capitalize text-sm font-medium text-center border-b-2 border-transparent hover:text-gray-600 hover:border-b-gray-300 dark:hover:text-gray-300 hover:no-underline focus:border-transparent" >
            {project.data.name}
          </button>
        </li>
      {/each}
    {/if}
  </ul>