<script>
    import { onMount } from "svelte";
    import Tabs from "../Tabs/Tabs.svelte";
    import tasksService from "../services/tasksService";
    import Dates from "../Forms/Dates.svelte";
    import Icons from "../Icons/Icons.svelte";
    import {slide} from 'svelte/transition';
    export let rate;
    const timezoneHoursOffset = new Date().getTimezoneOffset() / 60;
    let startDate = new Date(new Date().getFullYear(), new Date().getMonth(), 1);
    let endDate = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
    let promise = (async () => await tasksService.getTasks(startDate.toISOString(), endDate.toISOString()))();
    let currentTab = 0;
    let writePromise = new Promise(resolve => {resolve();});
    let actionInProgress = '';
    let showSubtasks = [];
    const getTasks = (startDate, endDate) =>{
        startDate = new Date(startDate);
        endDate = new Date(new Date(endDate).getFullYear(), new Date(endDate).getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
        promise = (async () => await tasksService.getTasks(startDate.toISOString(), endDate.toISOString()))();
    }
    const setShowSubtasks = (taskId) => {
        showSubtasks = showSubtasks.includes(taskId)? showSubtasks.filter(id => id !== taskId) : [...showSubtasks, taskId];
    }
    const wiriteDocs = async (projects = [], exclude = false) => {
        let tasks = await promise;
        let sendTasks = JSON.parse(JSON.stringify(tasks));
        if(projects.length > 0 && !exclude){
            sendTasks = sendTasks.filter(task => projects.includes(task.project.data.name));
            actionInProgress = 'selected';
        }else if(projects.length > 0 && exclude){
            sendTasks = sendTasks.filter(task => !projects.includes(task.project.data.name));
            sendTasks = sendTasks.map(sheet => {
                if (sheet.project.data.name !== 'Totales'){
                    return sheet;
                }
                sheet.tasks = sheet.tasks.filter(task => !projects.includes(task.description));
                return sheet;
            });
            actionInProgress = 'exclude';
        }else{
            actionInProgress = 'all';
        }
        writePromise = tasksService.writeInGdoc(sendTasks);
    }
    onMount(() => {
    });
</script>
<div class="container mx-auto">
    <h1 class="text-center font-bold text-lg  text-[#40628f]">Águilas devs</h1>
    <Dates onSubmit={getTasks} start={startDate.toISOString().split('T')[0]} end={endDate.toISOString().split('T')[0]}
    icon="toggl" buttonText="Get Tasks from Toggl" color="red"/>
    {#await promise}
        <p class="dark:text-slate-400 flex gap-2 items-center"><Icons name="loader" tailwind="animate-spin h-4 w-4"/>Load Tasks...</p>
    {:then tasks}
        <div class="border-b border-gray-200 dark:border-gray-700">
            <Tabs bind:activeTabValue={currentTab} items={tasks} />
        </div>
        
        <div id="myTabContent">
        {#each tasks as taskstructure, j }
            <div class="{currentTab == j ? 'lg:flex' : 'hidden'} py-4" id="cont{j}tab" role="tabpanel">
                <div class="flex-auto w-full lg:w-2/3 md:shrink-0">
                    <table class="table-auto text-sm w-full">
                        <thead>
                            <tr>
                                <th style:background-color={taskstructure.project.data.hex_color} colspan="4" class="py-1 text-neutral-900 text-center border-b border-b-indigo-800 capitalize">
                                    {taskstructure.project.data.name}
                                </th>
                            </tr>
                            <tr>
                                <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-left w-1/12">Order</th>
                                <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-left w-28">Date</th>
                                <th class="pr-2 py-2 bg-indigo-400 text-stone-800 text-left  w-2/3">
                                    {j===0 ? 'Projects' : 'Tasks'}
                                </th>
                                <th class="px-2 py-2 bg-indigo-400 text-stone-800 text-center">Duration</th>
                            </tr>
                        </thead>
                        <tbody>
                            {#each taskstructure.tasks as task, j}
                                <tr class="{j%2? 'bg-indigo-300': 'bg-indigo-200'} text-stone-800">
                                    <td class="border border-transparent px-2 py-1 align-text-bottom">{j + 1}</td>
                                    <td class="border border-transparent px-2 py-2  align-text-bottom">{task?.date}</td>
                                    <td class="border border-transparent pr-4 py-2 capitalize">
                                        {#if task?.count > 1}
                                            <span on:click={setShowSubtasks(task?.id)} class="text-stone-800 border dark:border-gray-400 py-1 px-2 mr-1 cursor-pointer select-none">{task?.count}</span>
                                        {/if}
                                        {task?.description}
                                        {#if showSubtasks.includes(task?.id)}
                                            <div transition:slide="{{duration: 150}}" class="flex flex-col border-t border-neutral-800 text-xs mt-5">
                                                {#each task?.subtasks as subtask, st}
                                                    <div class="flex items-center py-1 px-1 justify-between border-b border-neutral-600">
                                                        <span class="text-neutral-800">{subtask?.description}</span>
                                                        <span class="text-neutral-800"><strong>Start: </strong>{`${new Date(subtask?.start).toLocaleTimeString()}`}</span>
                                                        <span class="text-neutral-800"><strong>Stop: </strong>{`${new Date(subtask?.stop).toLocaleTimeString()}`}</span>
                                                        <span class="text-neutral-800"><strong>Duration: </strong>{`${subtask?.duration}`}</span>
                                                    </div>
                                                {/each}
                                            </div>
                                        {/if}
                                    </td>
                                    <td class="border border-y-indigo-900 border-x-transparent px-2 py-1 lining-nums tabular-nums dark:bg-indigo-400 dark:text-indigo-900 font-bold text-base text-center align-text-bottom">
                                        {task?.duration}
                                    </td>
                                </tr>
                            {/each}
                        </tbody>
                    </table>                
                </div>
                <div class="flex-auto w-full lg:w-1/3 pl-4 md:shrink-0">
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
                                <td>{parseFloat(taskstructure.project.durationHours.toFixed(9))}</td>
                            </tr>
                            <tr>
                                <td>Totals</td>
                                <td>$ {(taskstructure.project.durationHours * rate ).toFixed(2)}</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="lg:flex mt-4 gap-2 justify-between lg:flex-wrap-reverse">
                        <button on:click={(e) => {wiriteDocs()}} 
                        class="bg-[#188038] hover:bg-white border-2 border-[#188038] text-white hover:text-black font-bold tracking-wide py-1 px-1 rounded-sm flex gap-2 content-center items-center text-xs order-2 mb-2 lg:mb-0">
                                {#await writePromise}
                                    <Icons name={actionInProgress === 'all'?"loader":"gsheet"} tailwind={`${actionInProgress === 'all'?"animate-spin":''} flex-no-shrink fill-current h-4 w-4 text-white`} />
                                {:then result } 
                                    <Icons name="gsheet"/>
                                {/await}
                                Write All
                        </button>
                        {#if taskstructure.project.data.name !== 'Totales'}    
                            <button on:click={(e) => {wiriteDocs([taskstructure.project.data.name])}} 
                            class="bg-[#188038] hover:bg-white border-2 border-[#188038] text-white hover:text-black pl-1 rounded-sm flex gap-2 content-center items-center text-xs justify-center mb-2 lg:mb-0 order-3">
                                {#await writePromise}
                                    <Icons name={actionInProgress === 'selected'?"loader":"gsheet"} tailwind={`${actionInProgress === 'selected'?"animate-spin":''} flex-no-shrink fill-current h-4 w-4 text-white`} />
                                {:then result } 
                                    <Icons name="gsheet"/>
                                {/await}
                                Write Only <span  style="background-color:{taskstructure.project.data.hex_color};" 
                                class="font-bold text-black px-2 py-1 capitalize" >{taskstructure.project.data.name}</span>
                            </button>
                            <button on:click={(e) => {wiriteDocs([taskstructure.project.data.name], 'exclude')}} 
                            class="bg-[#188038] hover:bg-white border-2 border-[#188038] text-white hover:text-black pl-1 rounded-sm flex gap-2 content-center items-center text-xs justify-center order-1">
                                {#await writePromise}
                                    <Icons name={actionInProgress === 'exclude'?"loader":"gsheet"} tailwind={`${actionInProgress === 'exclude'?"animate-spin":''} flex-no-shrink fill-current h-4 w-4 text-white`} />
                                {:then result } 
                                    <Icons name="gsheet"/>
                                {/await}
                                Write All Except <span  style:color={taskstructure.project.data.hex_color} 
                                class="font-bold text-black px-2 py-1 bg-slate-900 capitalize" >{taskstructure.project.data.name}</span>
                            </button>
                        {/if}
                    </div>
                </div>
            </div>
        {/each}
        </div>
    {/await}
</div>