<script>
  import throttle from "just-throttle";

  let filterText = "";

  let tableNames, filteredTableNames;
  const filterTableNames = () => {
    const filterTerms = filterText
      .trim()
      .split(" ")
      .filter(t => t.length > 0);
    filteredTableNames = tableNames.filter(tableName =>
      filterTerms.every(term => tableName.includes(term))
    );
  };
  const request = fetch("tables.json")
    .then(r => r.json())
    .then(t => {
      tableNames = t.map(t => `${t.dataset}.${t.name}`).sort();
      filterTableNames();
    });
</script>

<p class="py-4">
  This is a demo of a schema dictionary: the intention is to provide
  understandable, human-readable table and column descriptions for all our
  datasets. Currently it allows you to browse / scan through the tables
  generated in
  <span>
    &nbsp;
    <a href="https://github.com/mozilla-services/mozilla-pipeline-schemas">
      mozilla-pipeline-schemas
    </a>
    &nbsp;
  </span>
  for a proof-of-concept. There is also an example of mixing this type of data
  with generated documentation (even more proof-of-concept) in&nbsp;
  <a href="/search-clients-daily">search_clients_daily</a>
  . For more information on the vision for the project, check out the&nbsp;
  <a
    href="https://docs.google.com/document/d/1bEJhvyYcijeP5JwwnamLCKyxaKdFIpWYs_ud_OzYC_E/edit#heading=h.dh34mdvj1r6y">
    prototype proposal
  </a>
  .
</p>

<hr />

<h2 class="py-4">Tables</h2>

{#if filteredTableNames}
  <div class="container mx-auto">
    <input
      class="shadow appearance-none border rounded w-full p-2 text-gray-700
      leading-tight focus:outline-none focus:shadow-outline"
      type="text"
      bind:value={filterText}
      on:input={throttle(filterTableNames, 200)}
      placeholder="filter terms" />
  </div>
  <div class="container py-4 mx-auto">
    {#each filteredTableNames as tableName}
      <p>
        <a href="/tables/{tableName}">{tableName}</a>
      </p>
    {/each}
  </div>
{/if}
