<script>
	import TasksTable from "./tasksTable/TasksTable.svelte";
	import 'flowbite';
</script>
<div class="all-screen min-h-screen pt-4 dark:bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800">
	<div class="container mx-auto">
		<h1 class="text-center font-bold text-lg  text-[#40628f]">Águilas devs</h1>
		<TasksTable/>
	</div>
</div>

<style lang="postcss" global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
  </style>