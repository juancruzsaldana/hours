<script>
    export let name;
    export let tailwind = 'h-4 w-4 flex-no-shrink fill-current';
</script>
{#if name === 'gsheet'}
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 64 88" style="enable-background:new 0 0 64 88;" xml:space="preserve"
        class={tailwind}>
    <style type="text/css">
        .st0{fill:#0DC54C;}
        .st1{fill:#08962D;}
        .st2{fill:#FDFFFF;}
    </style>
    <g id="Layer_4">
        <path class="st0" d="M58,88H6c-3.3,0-6-2.7-6-6V6c0-3.3,2.7-6,6-6h36l22,22v60C64,85.3,61.3,88,58,88z"/>
        <path class="st1" d="M42,0l22,22H42V0z"/>
        <path class="st2" d="M12,34.5v28h40v-28H12z M17,39.5h12.5V46H17V39.5z M17,51h12.5v6.5H17V51z M47,57.5H34.5V51H47V57.5z M47,46   H34.5v-6.5H47V46z"/>
    </g>
    </svg>
{/if}

{#if name === 'loader'}
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
    class={tailwind}>
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
    </svg>
{/if}