<template>

    <div class="row">
        <div class="col-12 text-end my-2">
            <button type="button" class="btn btn-sm btn-outline-secondary"
                @click="toggle">{{ toggleBtnText }}
            </button>
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
                            <td>{{ player.player_name }}</td>
                            <td>{{ player.shots }}</td>
                            <td>{{ player.sca }}</td>
                            <td>{{ player.touches }}</td>
                            <td>{{ player.passes }}</td>
                            <td>{{ player.carries }}</td>
                            <td>{{ player.tackled }}</td>
                            <td>{{ player.interceptions }}</td>
                            <td>{{ player.blocks }}</td>
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
          showFullTable: true,
          toggleBtnText: 'Hide Table',
      };
  },
  methods: {
      toggle() {
            this.showFullTable = !this.showFullTable;
            if (this.showFullTable) {
                this.toggleBtnText = 'See Full Table';
            } else {
                this.toggleBtnText = 'Hide Table';
            }
      }
  }

}
</script>
<style scoped>
</style>