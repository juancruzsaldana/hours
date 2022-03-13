<script>
	import {Router, Route, Link} from 'svelte-navigator';
	import TasksTable from "./tasksTable/TasksTable.svelte";
	import 'flowbite';
	import Icons from "./Icons/Icons.svelte";
	let showSidebar = false;
	const toggleSidebar = () => {
		showSidebar = !showSidebar;
	};
</script>
<svelte:head>
	<title>Local Status</title>
</svelte:head>
<Router>
	<div class="w-full flex flex-col sm:flex-row flex-grow">
		<div class={`${showSidebar?'sm:w-2/12 md:2/12':'sm:w-12 md:w-12'} w-full flex-shrink flex-grow-0 sticky top-0 transition-all`}>
			<div class="sticky top-0 dark:bg-blue-900 w-full sm:min-h-screen">
				<div class="hidden sm:flex  sm:pt-4 {showSidebar?'justify-end pr-2':'justify-center'} ">
					<button on:click={(e) => {toggleSidebar()}} class="flex text-white border-0 mb-3 hover:text-blue-500">
							{#if showSidebar}
								<Icons name="close" tailwind="w-5 h-5"/>
							{:else}	
								<Icons name="menu" tailwind="w-5 h-5 transition-all "/>
							{/if}
					</button>
				</div>
				<nav class="">					
					<ul class="flex sm:flex-col overflow-hidden content-center justify-around sm:justify-between space-y-2 sm:divide-y sm:divide-stone-900">
						<li class="!mt-0">
							<Link title="Tasks"  to="/tasks" getProps
							class="w-full hover:bg-blue-500 flex align-center font-bold hover:no-underline py-2 gap-2 {showSidebar?'justify-start px-2':'justify-center'}">
								<Icons name="clock" tailwind="w-6 h-6 text-white"/>
								<span class={`hidden text-white ${showSidebar?'sm:inline':''}`}>Tasks</span>
							</Link>
						</li>
						<li class="!mt-0">
							<Link title="Expenses" to="/" getProps
							 class="w-full hover:bg-blue-500 flex align-center font-bold hover:no-underline py-2 gap-2 px-2 {showSidebar?'justify-start sm:px-2':'justify-center sm:px-0'}">
								<Icons name="cash" tailwind="w-6 h-6 text-white"/>
								<span class={`hidden  text-white ${showSidebar?'sm:inline':''}`}>Expenses</span>
							</Link>
						</li>
						
					</ul>
				</nav>
			</div>
		</div>
		<Route path="/">
			<div class="all-screen min-h-screen w-full flex-grow pt-4 dark:bg-gradient-to-br from-neutral-900 via-neutral-900 to-neutral-800 ">

				<h1>Hola che!</h1>
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
			@apply bg-blue-500;
		}
	}
</style>