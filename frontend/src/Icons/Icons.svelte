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

{#if name === 'toggl'}
    <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
    width="588.000000pt" height="592.000000pt" viewBox="0 0 588.000000 592.000000"
    preserveAspectRatio="xMidYMid meet"
    class={tailwind}>
        <g transform="translate(0.000000,592.000000) scale(0.100000,-0.100000)"
        fill="#e00000" stroke="none">
        <path d="M2600 5756 c-770 -99 -1443 -486 -1902 -1094 -296 -393 -478 -844
        -543 -1345 -18 -139 -20 -509 -4 -655 14 -137 62 -367 103 -504 164 -541 521
        -1071 956 -1421 395 -318 910 -532 1412 -586 125 -14 491 -14 616 0 165 17
        390 67 559 124 582 194 1049 549 1416 1077 273 393 447 852 496 1310 17 149
        14 515 -5 660 -99 768 -492 1442 -1109 1901 -371 276 -778 445 -1262 523 -135
        22 -589 28 -733 10z m528 -2043 l2 -973 -200 0 -200 0 0 975 0 975 198 -2 197
        -3 3 -972z m-558 318 l0 -198 -50 -21 c-82 -34 -212 -124 -288 -201 -200 -199
        -303 -468 -288 -746 24 -459 354 -835 811 -926 77 -15 273 -15 350 0 390 78
        686 359 786 747 34 132 32 331 -5 469 -47 181 -134 333 -263 460 -75 74 -204
        164 -282 196 l-51 22 0 198 c0 118 4 199 9 199 25 0 166 -58 261 -106 365
        -186 623 -531 711 -947 31 -145 31 -381 1 -523 -107 -500 -442 -881 -915
        -1039 -146 -49 -257 -66 -427 -66 -170 0 -281 17 -427 66 -471 157 -809 538
        -915 1028 -31 144 -31 399 0 540 91 412 343 748 703 937 94 49 239 108 267
        110 9 0 12 -46 12 -199z"/>
        </g>
    </svg>
{/if}

{#if name === 'menu'}
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    class={tailwind}>
        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
    </svg>
{/if}

{#if name === 'close'}
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2"
    class={tailwind}>  
        <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
    </svg>
{/if}

{#if name === 'home' || name === '/'}
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    class={tailwind} >
        <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
    </svg>
{/if}

{#if name === 'clock'|| name === 'tasks'}
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    class={tailwind}>
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
{/if}

{#if name === 'dollars'}
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    class={tailwind}>
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
{/if}

{#if name === 'cash' || name === 'expenses'}
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
    class={tailwind}>
        <path stroke-linecap="round" stroke-linejoin="round" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
    </svg>
{/if}