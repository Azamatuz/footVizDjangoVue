<template>
  <div :style="{ height: '400px' }">
    <Bar id="bar-chart-id" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

export default {
  name: 'BarChart',
  components: {
    Bar
  },
  props: {
    homeTeamStats: Array,
    awayTeamStats: Array,
  },
  data() {
    return {
        chartOptions: {
            elements: {
              bar: {
                borderWidth: 2,
              }
            },
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins: {
              legend: {
                position: 'right',
              },
            }
        },
        teamData: [],
        filteredStats: []
    }
  },
  mounted() {
  },
  computed: {
    computedHomeStats() {
      return this.homeTeamStats.stats
    },
    computedAwayStats() {
      return this.awayTeamStats.stats
    },
    // remove 'passes', 'touches', 'carries' from the teamStats.stats object
    homeFilteredData() {
      if (!this.computedHomeStats) {
        return [];
      }
      return Object.values(this.computedHomeStats.map(({ touches, passes, carries, ...rest }) => rest)[0]);
    },
    awayFilteredData() {
      if (!this.computedAwayStats) {
        return [];
      }
      return Object.values(this.computedAwayStats.map(({ touches, passes, carries, ...rest }) => rest)[0]);
    },

    chartData() {
      return {
        labels: [
          'shots',
          'sca',
          'tackled',
          'interceptions',
          'blocks'
        ],
        datasets: [
          {
            label: this.homeTeamStats.team_name,
            data: this.homeFilteredData,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)',
          },
          {
            label: this.awayTeamStats.team_name,
            data: this.awayFilteredData,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
          }
        ]
      }
    },
  },
  methods: {
    },
}
</script>