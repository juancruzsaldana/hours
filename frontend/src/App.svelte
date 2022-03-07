<script>
	import TasksTable from "./tasksTable/TasksTable.svelte";
	import 'flowbite';
</script>
<div class="all-screen dark:bg-slate-900 min-h-screen pt-4">
	<div class="container mx-auto">
		<h1 class="text-center font-bold text-lg  text-indigo-500">Águilas devs</h1>
		<TasksTable/>
	</div>
</div>

<style lang="postcss" global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
  </style>