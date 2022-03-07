<script>
    import { onMount } from "svelte";
    import Tabs from "../Tabs/Tabs.svelte";
    import tasksService from "../services/tasksService";
    import Dates from "../Forms/Dates.svelte";
    let rate = tasksService.getRate();
    const timezoneHoursOffset = new Date().getTimezoneOffset() / 60;
    let startDate = new Date(new Date().getFullYear(), new Date().getMonth(), 1);
    let endDate = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
    let promise = (async () => await tasksService.getTasks(startDate.toISOString(), endDate.toISOString()))();
    let currentTab = 0;
    const getTasks = (startDate, endDate) =>{
        startDate = new Date(startDate);
        endDate = new Date(new Date(endDate).getFullYear(), new Date(endDate).getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
        promise = (async () => await tasksService.getTasks(startDate.toISOString(), endDate.toISOString()))();
    }
    onMount(() => {
    });
</script>
<Dates onSubmit={getTasks} start={startDate.toISOString().split('T')[0]} end={endDate.toISOString().split('T')[0]}/>
{#await promise}
    <p class="dark:text-slate-400">Load Tasks...</p>
{:then tasks}
    <div class="border-b border-gray-200 dark:border-gray-700">
        <Tabs bind:activeTabValue={currentTab} items={tasks} />
    </div>
    
    <div id="myTabContent">
    {#each tasks as taskstructure, j }
        <div class="{currentTab == j ? '' : 'hidden'} py-4 flex" id="cont{j}tab" role="tabpanel">
            <div class="flex-auto w-full lg:w-3/4 ">
                <table class="table-auto text-xs w-full">
                    <thead>
                        <tr>
                            <th style:background-color={taskstructure.project.data.hex_color} colspan="4" class="py-1 text-neutral-900 text-center border-b border-b-indigo-800 capitalize">
                                {taskstructure.project.data.name}
                            </th>
                        </tr>
                        <tr>
                            <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-left w-1/12">Order</th>
                            <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-left w-24">Date</th>
                            <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-center  w-2/3">
                                {j===0 ? 'Projects' : 'Tasks'}
                            </th>
                            <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-center">Duration</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each taskstructure.tasks as task, j}
                            <tr class="{j%2? 'bg-indigo-300': 'bg-indigo-200'} text-stone-800">
                                <td class="border border-transparent px-2 py-1">{j}</td>
                                <td class="border border-transparent px-2 py-2">{task?.date}</td>
                                <td class="border border-transparent px-4 py-1 capitalize">
                                    {#if task?.count > 1}
                                        <span class="text-stone-800 border dark:border-gray-400 py-1 px-2 mr-1">{task?.count}</span>
                                    {/if}
                                    {task?.description}
                                </td>
                                <td class="border border-y-indigo-900 border-x-transparent px-2 py-1 lining-nums tabular-nums dark:bg-indigo-400 dark:text-indigo-900 font-bold text-base text-center">
                                    {task?.duration}
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>                
            </div>
            <div class="flex-auto w-full lg:w-1/4 pl-4">
                <table class="table-auto text-xs w-full text-base text font-bold">
                    <thead>
                        <tr>
                            <th colspan="2" class="text-left">Totals</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Rate</td>
                            <td>$ {rate}</td>
                        </tr>
                        <tr>
                            <td>Totals Hours</td>
                            <td>{taskstructure.project.durationFormated}</td>
                        </tr>
                        <tr class="border-b border-b-slate-700">
                            <td>Amount Hours</td>
                            <td>{taskstructure.project.durationHours.toFixed(2)}</td>
                        </tr>
                        <tr>
                            <td>Totals</td>
                            <td>$ {(taskstructure.project.durationHours * rate ).toFixed(2)}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    {/each}
    </div>
{/await}