<script>
    import Icons from "../Icons/Icons.svelte";
    import NewAccess from "../Forms/NewAccess.svelte";
    import accessService from "../services/accessService";
    let visibleAccess = [];
    let promiseAccess = (async () =>{ 
        visibleAccess = await accessService.getAccess();
        return visibleAccess;
    })();
    let selectedAccess = {};
    let buttonText = 'New Access';
    let search = '';
    const onNewAccess = (access) => {
        accessService.newAccess(access).then(async (r) => {
            let accessArray = await promiseAccess;
            accessArray.push(r.access);
            promiseAccess = new Promise((resolve) => resolve(accessArray));
            visibleAccess = accessArray;
        });
    };

    const onUpdateAccess = (access) => {
        accessService.editAccess(access.id, access).then(async (r) => {
            let accessArray = await promiseAccess;
            promiseAccess = new Promise((resolve) => {
                resolve(accessArray);
            });
            visibleAccess = accessArray;
            buttonText = 'New Access';
        });
    };

    const submitAccessForm = (access) =>{
        return access.id ? onUpdateAccess(access) : onNewAccess(access);
    }

    const deleteAccess = (access_id) => {
        accessService.removeAccess(access_id).then(async (r) => {
            let accessArray = await promiseAccess;
            accessArray = accessArray.filter(acc => acc.id !== access_id);
            promiseAccess = new Promise((resolve) => {
                resolve(accessArray);
            });
            visibleAccess = accessArray;
        });
    }

    const selectAccess = (access) => {
        selectedAccess = access;
        buttonText = 'Edit Access';
    };

    const filterAccess = async () => {
        let accessArray = await promiseAccess;
        accessArray = search ? accessArray.filter(acc =>{return acc.service.toLowerCase().match(`${search.toLowerCase()}.*`)}) : accessArray;
        visibleAccess = accessArray;
    };
</script>
<div class="container mx-auto">
    <h1 class="text-center font-bold text-lg  text-stone-600">Access</h1>
    <NewAccess onSubmit={submitAccessForm} access={selectedAccess} buttonText={buttonText} />
    <div class="sm:flex justify-end border-t border-stone-500 mt-2 pt-2 text-neutral-500 items-center text-xs">
        <label for="search" class="font-bold sm:mr-1">Search: </label>
        <input type="text" id="search" bind:value={search} placeholder="Search" on:keyup={(e) => filterAccess()}
        class="sm:mr-1 h-6 w-32  py-0 text-sm  rounded-sm bg-white border border-cyan-400" />
    </div>
    <div class="rounded-md overflow-hidden pb-1 mt-4">
        {#await promiseAccess}
            <p class="dark:text-cyan-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Access...</p>
        {:then access} 
            <table class="table-auto text-sm w-full text-sm text-cyan-300 border-collapse border border-cyan-500">
                <thead>
                    <tr class="text-center bg-cyan-300 text-cyan-500">
                        <th colspan="7">Access</th>
                    </tr>
                    <tr>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">#</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">Service</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">Url</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">User</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">Password</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">Observation</th>
                        <th class="pl-1 text-left border border-cyan-500 bg-cyan-300 text-cyan-500">Actions</th>
                    </tr>
                </thead>
                <tbody class="text-white">
                    {#each visibleAccess as acc, i }
                        <tr>
                            <td class="text-center border border-cyan-500">{i+1}</td>
                            <td class="pl-1 text-left border border-cyan-500">{acc.service}</td>
                            <td class="pl-1 text-left border border-cyan-500">
                                {#if acc.url}
                                    <a href={acc.url} title="{acc.url}" target="_blank" rel="noopener noreferrer" class="text-cyan-200 visited:text-cyan-200">{acc.url}</a>
                                {/if}
                            </td>
                            <td class="pl-1 text-left border border-cyan-500">
                                {acc.user ?? ''}
                            </td>
                            <td class="pl-1 text-left border border-cyan-500">
                                {acc.password ?? ''}
                            </td>
                            <td class="pl-1 text-left border border-cyan-500">
                                {acc.observations}
                            </td>
                            <td class="pl-1 text-left border border-cyan-500">
                                <button on:click|preventDefault={(e) => selectAccess(acc)}
                                class="align-text-bottom mr-2 text-blue-500 hover:text-blue-600 cursor-pointer hover:opacity-75 focus:outline-none">
                                    <Icons name="edit" tailwind="flex-no-shrink h-4 w-4" />
                                </button>
                                <button on:click|preventDefault={(e) => deleteAccess(acc.id)}
                                class="align-text-bottom text-red-500 hover:text-red-600 cursor-pointer hover:opacity-75 focus:outline-none">
                                    <Icons name="delete" tailwind="flex-no-shrink h-4 w-4" />
                                </button>
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        {/await}
    </div>
</div>