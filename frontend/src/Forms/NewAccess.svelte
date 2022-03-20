<script>
    import Icons from "../Icons/Icons.svelte";
    export let onSubmit;
    export let access = {};
    export let buttonText = 'New Access';
    const handleSubmit = (e) => {
        onSubmit(access);
        access = {};
    };
</script>

<form on:submit|preventDefault={handleSubmit} class="sm:flex justify-between border-t border-stone-500 mt-2 pt-2 text-neutral-500 items-center text-xs">
    <input type="hidden" name="accessId" id="accessId" bind:value={access.id}>
    <label for="service" class="font-bold sm:mr-1">Service</label>
    <input required type="text" id="service" class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-cyan-200 border border-cyan-400" bind:value={access.service} placeholder="Service"/>
    <label for="url" class="font-bold sm:mr-1">URL</label>
    <input type="text" id="url" class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-cyan-200 border border-cyan-400" bind:value={access.url} placeholder="URL"/>
    <label for="user" class="font-bold sm:mr-1">Usuario</label>
    <input type="text" id="user" class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-cyan-200 border border-cyan-400" bind:value={access.user} placeholder="Usuario"/>
    <label for="password" class="font-bold sm:mr-1">Password</label>
    <input type="text" id="password" class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-cyan-200 border border-cyan-400" bind:value={access.password} placeholder="Password"/>
    <label for="observations" class="font-bold sm:mr-1">Observations</label>
    <input type="text" id="observations" class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-cyan-200 border border-cyan-400" bind:value={access.observations} placeholder="Observations"/>
    <button type=submit
            class="flex gap-2 content-center items-center bg-cyan-900 hover:bg-cyan-800 active:bg-cyan-700 focus:outline-none border-cyan-900 border-2 px-2 py-1 rounded-md disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:bg-cyan-500 disabled:text-cyan-800  text-white">
        <Icons name="key" tailwind="flex-no-shrink h-4 w-4" />
        {buttonText}
    </button>
</form>