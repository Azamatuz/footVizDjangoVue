<template>
  <ul class="nav nav-tabs" :id="'myTab'+tabId" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" :id="'radar-tab'+tabId" data-bs-toggle="tab" :data-bs-target="'#radar'+tabId" type="button" role="tab" aria-controls="radar" aria-selected="true">Radar Chart</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" :id="'scatter-tab'+tabId" data-bs-toggle="tab" :data-bs-target="'#scatter'+tabId" type="button" role="tab" aria-controls="scatter" aria-selected="false">Attack/Defense</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" :id="'table-tab'+tabId" data-bs-toggle="tab" :data-bs-target="'#table'+tabId" type="button" role="tab" aria-controls="table" aria-selected="false">Table</button>
        </li>
      </ul>
      <div class="tab-content" :id="'myTabContent'+tabId">
        <div class="tab-pane fade show active" :id="'radar'+tabId" role="tabpanel" :aria-labelledby="'radar-tab'+tabId">
          <div class="col-6 d-inline-flex" v-for="(player, index) in PlayersData" :key="index">
            <RadarChart v-bind:playerStats="Object.values(player)" v-bind:homeTeam=homeTeam />
          </div>
        </div>
        <div class="tab-pane fade" :id="'scatter'+tabId" role="tabpanel" :aria-labelledby="'scatter-tab'+tabId">
            <ScatterChart v-bind:playerStats="PlayersData" v-bind:homeTeam=homeTeam />
        </div>
        <div class="tab-pane fade" :id="'table'+tabId" role="tabpanel" :aria-labelledby="'table-tab'+tabId">
          <StatsTable v-bind:playerStats="PlayersData" />
        </div>
      </div>
</template>

<script>
// components
import RadarChart from './RadarChart.vue'
import StatsTable from './StatsTable.vue'
import ScatterChart from './ScatterChart.vue';
export default {
    name: 'TabNav',
    props: {
        PlayersData: Array,
        homeTeam: Boolean,
        tabId: String,
    },
    components: {
        RadarChart,
        StatsTable,
        ScatterChart,
    },
    data() {
        return {
        };
    },
    methods: {
    },
    mounted() {

    }

}
</script>

<style>

</style>