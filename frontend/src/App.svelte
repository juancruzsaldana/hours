<script>
	import {Router, Route} from 'svelte-navigator';
	import TasksTable from "./tasksTable/TasksTable.svelte";
	import Expenses from './Expenses/Expenses.svelte';
	import appConfigService from './services/appConfigService';
	import Sidebar from './Components/Sidebar.svelte';
	import 'flowbite';
	let {sidebarItems, home} = appConfigService.getFeatures();
</script>
<svelte:head>
	<title>Local Status</title>
</svelte:head>
<Router>
	<div class="w-full flex flex-col sm:flex-row flex-grow">
		<Sidebar items={sidebarItems} home={home}/>
		<Route path="/">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-neutral-900 via-neutral-900 to-neutral-800 ">
				<Expenses/>
			</div>
		</Route>
		<Route path="tasks">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800">
				<TasksTable/>
			</div>
		</Route>
	</div>
</Router>

<style lang="postcss" global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	@layer base {
		a[aria-current="page"] {
			background-color: rgb(63 131 248); /*@apply directive show an svelte error */
		}
	}
</style>