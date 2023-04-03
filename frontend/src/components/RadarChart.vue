<template>
    <Bar
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
    playerStats: Array
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
            label: this.playerStats[0],
            data: Object.values(this.playerStats[1][0]),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
          }
        ]
      }
    }
  },
  data() {
    return {
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
