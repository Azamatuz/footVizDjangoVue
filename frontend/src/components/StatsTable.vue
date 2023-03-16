<template>

    <div class="row justify-content-end">
        <div class="col-12">
            <div class="table-responsive my-3">
                <table class="table table-striped table-sm">
                    <thead>
                        <tr>
                            <th>Player</th>
                            <th style="max-width: 20px;">Number</th>
                            <th>Goals</th>
                            <th>Assists</th>
                            <th>Passes</th>
                            <th>Blocks</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="index in playerStats.length" :key="index">
                            <td>{{ playerStats[index-1].name }}</td>
                            <td>{{ playerStats[index-1].number }}</td>
                            <td>{{ playerStats[index-1].stats.assists }}</td>
                            <td>{{ playerStats[index-1].stats.goals }}</td>
                            <td>{{ playerStats[index-1].stats.passes }}</td>
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