<script>
    import { onMount } from "svelte";
    import Tabs from "../Tabs/Tabs.svelte";
    let promise = getTasksFromServer();
    let currentTab = 0;
    const endpoint = "http://127.0.0.1:8000/tasks/?start_date=2022-01-01T15:00:00-03:00&end_date=2022-01-31T16:00:00-03:00";
    async function getTasksFromServer() {
        let response = await fetch(endpoint);
        let tasks = await response.json();
        return tasks;
    }
    onMount(() => {
    });
</script>
<h2 class="text-center font-bold text-lg  text-indigo-500">Projects</h2>
{#await promise}
    <p>...</p>
{:then tasks}
    <div class="border-b border-gray-200 dark:border-gray-700">
        <Tabs bind:activeTabValue={currentTab} items={tasks} />
    </div>
    
    <div id="myTabContent">
    {#each tasks as taskstructure, j }
        <div class="{currentTab == j ? '' : 'hidden'} p-4 bg-gray-50 rounded-lg dark:bg-gray-800" id="cont{j}tab" role="tabpanel">
            <table class="table-auto border-collapse border border-indigo-500 text-sm">
                <thead>
                    <tr>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">Order</th>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">Task</th>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">ID</th>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">Start</th>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">End</th>
                        <th class="px-4 py-2 bg-indigo-400 text-stone-800">Duration</th>
                    </tr>
                </thead>
                <tbody>
                    {#each taskstructure.tasks as task, j}
                        <tr class="{j%2? 'bg-indigo-200': ''}">
                            <td class="border border-indigo-500 px-4 py-2">{j}</td>
                            <td class="border border-indigo-500 px-4 py-2">{task?.description}</td>
                            <td class="border border-indigo-500 px-4 py-2">{task?.id}</td>
                            <td class="border border-indigo-500  px-4 py-2">{task?.start}</td>
                            <td class="border border-indigo-500 px-4 py-2">{task?.stop}</td>
                            <td class="border border-indigo-500 px-4 py-2 lining-nums tabular-nums">{task?.duration}</td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </div>
    {/each}
    </div>
{/await}