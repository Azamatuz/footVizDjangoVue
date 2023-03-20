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
                            <th>Press</th>
                            <th>Tackled</th>
                            <th>Interceptions</th>
                            <th>Blocks</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="index in playerStats.length" :key="index">
                            <td>{{ playerStats[index-1].name }}</td>
                            <td>{{ playerStats[index-1].stats.shots }}</td>
                            <td>{{ playerStats[index-1].stats.sca }}</td>
                            <td>{{ playerStats[index-1].stats.touches }}</td>
                            <td>{{ playerStats[index-1].stats.passes }}</td>
                            <td>{{ playerStats[index-1].stats.carries }}</td>
                            <td>{{ playerStats[index-1].stats.press }}</td>
                            <td>{{ playerStats[index-1].stats.tackled }}</td>
                            <td>{{ playerStats[index-1].stats.interceptions }}</td>
                            <td>{{ playerStats[index-1].stats.blocks }}</td>
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