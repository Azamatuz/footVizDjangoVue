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
        filteredStats: [],
        homeTeam: '',
        awayTeam: '',
    }
  },
  mounted() {
  },
  computed: {
    computedHomeStats() {
      return this.homeTeamStats[0]
    },
    computedAwayStats() {
      return this.awayTeamStats[0]
    },
    // remove 'passes', 'touches', 'carries' from the teamStats.stats object
    homeFilteredData() {
      if (!this.computedHomeStats) {
        return [];
      }
      const { player_name, player_team, touches, passes, carries, ...rest } = this.computedHomeStats;
      return Object.values(rest);
    },
    awayFilteredData() {
      if (!this.computedAwayStats) {
        return [];
      }
      const { player_name, player_team, touches, passes, carries, ...rest } = this.computedAwayStats;
      return Object.values(rest);
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
            label: this.homeTeam,
            data: this.homeFilteredData,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)',
          },
          {
            label: this.awayTeam,
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
  watch: {
  homeTeamStats: {
    immediate: true, // set the initial value of homeTeam when the component mounts
    handler(newValue) {
      if (newValue.length > 0) {
        this.homeTeam = newValue[0].player_team;
      }
    }
  },
  awayTeamStats: {
    immediate: true, // set the initial value of awayTeam when the component mounts
    handler(newValue) {
      if (newValue.length > 0) {
        this.awayTeam = newValue[0].player_team;
      }
    }
  }
}

}
</script>