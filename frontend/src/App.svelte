<script>
	import {Router, Route} from 'svelte-navigator';
	import TasksTable from "./tasksTable/TasksTable.svelte";
	import Expenses from './Expenses/Expenses.svelte';
	import appConfigService from './services/appConfigService';
	import Sidebar from './Components/Sidebar.svelte';
	import Access from './Access/Access.svelte';
	import 'flowbite';
	import Dollars from './Dollars/Dollars.svelte';
	let {sidebarItems, home} = appConfigService.getFeatures();
	const rate = appConfigService.getRate();
</script>
<svelte:head>
	<title>Local Status</title>
</svelte:head>
<Router>
	<div class="w-full flex flex-col sm:flex-row flex-grow">
		<Sidebar items={sidebarItems} home={home}/>
		<Route path="access">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-stone-900 via-stone-900 to-stone-800 ">
				<Access/>
			</div>
		</Route>
		<Route path="expenses">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-neutral-900 via-neutral-900 to-neutral-800 ">
				<Expenses rate={rate}/>
			</div>
		</Route>
		<Route path="tasks">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800">
				<TasksTable rate={rate}/>
			</div>
		</Route>
		<Route path="/">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-emerald-900 via-emerald-900 to-emerald-800">
				<Dollars/>	
			</div>
		</Route>
	</div>
</Router>

<style lang="postcss" global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>