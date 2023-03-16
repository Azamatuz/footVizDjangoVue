<template>
    {{ playerStats }}
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
  Legend)

  export default {
    name: 'RadarChart',
    components: {
      Bar: Radar },
    props: {
      playerStats: Array,
    },
    data() {
      return {
        chartData: {
          labels: [ 'assists', 'goals', 'passes', 'blocks' ],
          datasets: [
          {
      label: 'My First dataset',
      backgroundColor: 'rgba(179,181,198,0.2)',
      borderColor: 'rgba(179,181,198,1)',
      pointBackgroundColor: 'rgba(179,181,198,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(179,181,198,1)',
      data: this.playerStats
    }]
        },
        chartOptions: {
          responsive: true
        }
      }
    }
  }
  </script>