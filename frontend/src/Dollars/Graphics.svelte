<script>
    import { Chart } from "frappe-charts"
    import 'frappe-charts/dist/frappe-charts.min.css'
    import { afterUpdate } from 'svelte';

    export let movements;
    export let sellValues;
    const labels = movements.map(movement => movement.date);
    afterUpdate(async () => {
        const cotizationData = {
            labels: labels,
            datasets: [
                {
                    name: "Cotizarion", chartType: "line",
                    values: movements.map((m) => Number(m.quote.toFixed(2)))
                }
            ]
        }

        const partialData = {
            labels: labels,
            datasets: [
                {
                    name: "Values", chartType: "line",
                    values: movements.map((m) => Number(m.partial.toFixed(2)))
                }
            ]
        }
        const resultsData = {
            labels : labels,
            datasets: [
                {
                    name: "Results", chartType: "bar",
                    values: movements.map((m) =>  Number(m.amountInDollars) * sellValues[Number(m.sellValue)] - Number(m.amountInPesos))
                }
            ]
        }

		const cotizationChart = new Chart("#cotization", {  
            title: "Cotization",
            data: cotizationData,
            type: 'line', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
            height: 350,
            colors: ['#1e3a8a'],
            axisOptions: {
                xAxisMode: 'tick'
            },
            lineOptions: {
                hideDots: 1
            },
        });
        const partialsChart = new Chart("#partials", {  
            title: "Partials",
            data: partialData,
            type: 'line',
            height: 350,
            colors: ['#22d3ee'],
            axisOptions: {
                xAxisMode: 'tick'
            },
            lineOptions: {
                hideDots: 1
            },
        });

        const resultsChart = new Chart("#results", {  
            title: "Results",
            data: resultsData,
            type: 'bar',
            height: 350,
            colors: ['#0284c7'],
            axisOptions: {
                xAxisMode: 'tick'
            },
            barOptions: {
                stacked: 1
            },
        });
	});
    

</script>
<div id="cotization" class="bg-green-300 rounded"></div>
<div id="partials" class="bg-green-300 rounded mt-2"></div>
<div id="results" class="bg-green-300 rounded mt-2"></div>