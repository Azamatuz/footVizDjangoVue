<template>

    <div class="row justify-content-end">
        <div class="row p-0">
            <div class="col-12 col-md-10 text-start m-0 p-0">
                <h4>Players' normalized performance </h4>
            </div>
            <div class="col-12 col-md-2">
                <button type="button" class="btn btn-sm btn-outline-secondary"
                    @click="toggle">{{ toggleBtnText }}
                </button>
            </div>
        </div>
        <div class="col-12">
            <div class="table-responsive my-3">
                <table class="table table-hover table-sm">
                    <thead class="table-secondary">
                        <tr>
                            <th>Player</th>
                            <th>Shots</th>
                            <th>SCA</th>
                            <th>Touches</th>
                            <th>Passes</th>
                            <th>Carries</th>
                            <th>Tackled</th>
                            <th>Interceptions</th>
                            <th>Blocks</th>
                        </tr>
                    </thead>
                    <tbody v-show="showFullTable">
                        <tr v-for="(player, index) in playerStats" :key="index">
                            <td>{{ player.name }}</td>
                            <td>{{ player.stats[0].shots }}</td>
                            <td>{{ player.stats[0].sca }}</td>
                            <td>{{ player.stats[0].touches }}</td>
                            <td>{{ player.stats[0].passes }}</td>
                            <td>{{ player.stats[0].carries }}</td>
                            <td>{{ player.stats[0].tackled }}</td>
                            <td>{{ player.stats[0].interceptions }}</td>
                            <td>{{ player.stats[0].blocks }}</td>
                        </tr>
                    </tbody>
                    <tbody v-show="!showFullTable">
                        <tr>
                            <td>Total</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                            <td>-</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

</template>

<script>

export default {
  name: 'StatsTable',
  props: {
      playerStats: Array,
  },
  data() {
      return {
          showFullTable: false,
          toggleBtnText: 'See Full Table',
      };
  },
  methods: {
      toggle() {
            this.showFullTable = !this.showFullTable;
            if (this.showFullTable) {
                this.toggleBtnText = 'Hide Table';
            } else {
                this.toggleBtnText = 'See Full Table';
            }
      }
  }

}
</script>
<style scoped>
</style>