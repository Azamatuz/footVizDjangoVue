<template>
  <Scatter :style="{ height: '400px' }" :data="chartData" :options="chartOptions" />
</template>

<script>
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Scatter } from 'vue-chartjs'

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)

export default {
    name: 'ScatterChart',
    components: {
        Scatter
    },
    props: {
        homeTeam: Boolean,
    },
    computed: {
        chartData() {
            return {
                datasets: [
                    {
                        label: 'Scatter Dataset',
                        data: [
                            {
                                x: -10,
                                y: 0
                            },
                            {
                                x: 0,
                                y: 10
                            },
                            {
                                x: 10,
                                y: 5
                            }
                        ],
                        backgroundColor: this.bgColor
                    }
                ]
            }
        }
    },
    data() {
        return {
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom'
                    }
                }
            },
            bgColor: this.homeTeam ? 'rgb(255, 99, 132)' : 'rgb(54, 162, 235)',
        }
    }
}
</script>

<style>

</style>