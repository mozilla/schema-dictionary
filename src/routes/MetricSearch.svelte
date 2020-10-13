<script>
  import lunr from "lunr";

  let searchText = "";

  let idx = undefined;
  fetch("/metrics-index.json")
    .then(r => r.json())
    .then(idxData => {
      idx = lunr.Index.load(idxData);
    });

  let metrics = undefined;
  fetch("/metrics.json")
    .then(r => r.json())
    .then(metricsData => (metrics = metricsData));

  let searchResults = [];
  const searchObjects = () => {
    if (!searchText.length) {
      searchResults = [];
      return;
    }

    const modifiedSearchText = searchText
      .split(" ")
      .filter(s => s.length > 0)
      .map(s => (s.endsWith("*") ? s : s + "*"))
      .join(" ");
    searchResults = idx
      .search(modifiedSearchText)
      .slice(0, 20)
      .map(idxResult => {
        const metricInfo = metrics[idxResult.ref];
        return {
          name: idxResult.ref,
          description: metricInfo.history[0].description
        };
      });
  };
</script>

<style>
  .description {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 75ch;
    @apply text-gray-600;
  }
</style>

{#if metrics && idx}
  <div class="container mx-auto">
    <input
      class="shadow appearance-none border rounded w-full p-2 text-gray-700
      leading-tight focus:outline-none focus:shadow-outline"
      type="text"
      bind:value={searchText}
      on:input={searchObjects}
      placeholder="filter terms" />
  </div>
  <div class="container py-4 mx-auto">
    {#each searchResults as searchResult}
      <div class="container py-1">
        <b>{searchResult.name}</b>
        <br />
        <p class="description">{searchResult.description}</p>
      </div>
      <hr />
    {/each}
  </div>
{/if}
