<template>
    <Bar
      class="my-4"
      id="my-chart-id"
      :options="chartOptions"
      :data="chartData"
    />
  </template>

<script>
import { Radar } from 'vue-chartjs'
import { Chart as ChartJS, RadialLinearScale, Tooltip, Legend, Filler, LineElement, PointElement } from 'chart.js'

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
)

export default {
  name: 'RadarChart',
  components: {
    Bar: Radar
  },
  props: {
    playerStats: Array,
    homeTeam: Boolean,
  },
  computed: {
    chartData() {
      return {
        labels: [
          'shots',
          'sca',
          'touches',
          'passes',
          'carries',
          'tackled',
          'interceptions',
          'blocks'
        ],
        datasets: [
          {
            label: this.playerStats[1],
            data: Object.values(this.playerStats.slice(3)),
            backgroundColor: this.bgColor,
            borderColor: this.borderColor,
            pointBackgroundColor: this.pointColor,
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: this.pointHoverColor,
          }
        ]
      }
    }
  },
  data() {
    return {
      bgColor: this.homeTeam ? 'rgba(255, 99, 132, 0.2)' : 'rgba(54, 162, 235, 0.2)',
      borderColor: this.homeTeam ? 'rgb(255, 99, 132)' : 'rgb(54, 162, 235)',
      pointColor: this.homeTeam ? 'rgb(255, 99, 132)' : 'rgb(54, 162, 235)',
      pointHoverColor: this.homeTeam ? 'rgb(255, 99, 132)' : 'rgb(54, 162, 235)',
      chartOptions: {
        responsive: true,
        scales: {
          r: {
              angleLines: {
                  display: false
              },
              suggestedMin: 0,
              suggestedMax: 1
          }
        }
      }
    }
  }
}
</script>
