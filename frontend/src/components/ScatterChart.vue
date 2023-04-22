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
        playerStats: Array,
    },
    mounted() {

    },
    watch: {
        playerStats() {
            this.setDataSets();
        }
    },
    methods: {
        roundUp(value) {
            let roundedValue = Math.ceil(value * 2) / 2;
            if (roundedValue % 1 === 0) {
                return roundedValue + 0.5;
            } else {
                return roundedValue;
            }
        },
        setDataSets() {
            this.datasets = [];
            this.playerStats.forEach(player => {
                let dataset = {
                    label: player.player_name,
                    data: [
                        {
                            x: player.attack,
                            y: player.defense
                        }
                    ],
                    backgroundColor: this.bgColor
                };
                this.datasets.push(dataset);
            });
            const attack = this.playerStats.map(({attack}) => attack);
            const avgAttack =  (Math.max(...attack)) / 2;
            const maxAttack =  (Math.max(...attack));
            const defense = this.playerStats.map(({defense}) => defense);
            const avgDefense =  (Math.max(...defense)) / 2;
            const maxDefense =  (Math.max(...defense));

            this.datasets.push({
                borderColor: 'grey',
                showLine: true,
                pointRadius: 0,
                segment: {borderDash: [5, 5]},
                label: 'Average Defense Line',
                data: [[0, avgDefense], [this.roundUp(maxAttack), avgDefense]]
            });
            this.datasets.push({
                borderColor: 'grey',
                showLine: true,
                pointRadius: 0,
                segment: {borderDash: [5, 5]},
                label: 'Average Attack Line',
                data: [[avgAttack, 0], [avgAttack, this.roundUp(maxDefense)]]
            });
        },
    },
    computed: {
        chartData() {
            return {
                datasets:
                    this.datasets
            }
        },
        chartOptions() {
            return {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom',
                        title: {
                            display: true,
                            text: 'Attack',
                        },
                    },
                    y: {
                        type: 'linear',
                        position: 'left',
                        title: {
                            display: true,
                            text: 'Defense',
                        },
                    },
                },
                plugins: {
                    legend: {
                        position: 'right',
                    },
                }
            }
        },
    },
    data() {
        return {
            datasets: [],
            bgColor: this.homeTeam ? 'rgb(255, 99, 132)' : 'rgb(54, 162, 235)',
        }
    },
}
</script>

<style>

</style>