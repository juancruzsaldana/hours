<script>
    import Dates from "../Forms/Dates.svelte";
    export let rate;
    const timezoneHoursOffset = new Date().getTimezoneOffset() / 60;
    let startDate = new Date(new Date().getFullYear(), new Date().getMonth(), 1);
    let endDate = new Date(new Date().getFullYear(), new Date().getMonth() + 1, 0, 23-timezoneHoursOffset, 59, 59, 999);
</script>

<div class="container mx-auto">
    <h1 class="text-center font-bold text-lg  text-neutral-600">Expenses</h1>
    <h1 class="text-center font-bold text-lg  text-neutral-600">{rate}</h1>
</div>