<template>

    <div class="row justify-content-end">
        <div class="col-12">
            <div class="table-responsive my-3">
                <table class="table table-striped table-sm">
                    <thead>
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
                    <tbody>
                        <tr v-for="index in playerStats.length" :key="index">
                            <td>{{ playerStats[index-1].name }}</td>
                            <td>{{ playerStats[index-1].stats[0].shots }}</td>
                            <td>{{ playerStats[index-1].stats[0].sca }}</td>
                            <td>{{ playerStats[index-1].stats[0].touches }}</td>
                            <td>{{ playerStats[index-1].stats[0].passes }}</td>
                            <td>{{ playerStats[index-1].stats[0].carries }}</td>
                            <td>{{ playerStats[index-1].stats[0].tackled }}</td>
                            <td>{{ playerStats[index-1].stats[0].interceptions }}</td>
                            <td>{{ playerStats[index-1].stats[0].blocks }}</td>
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

}
</script>
<style scoped>
</style>