<script>
  import SchemaViewer from "../components/SchemaViewer.svelte";

  export let params;
  const URL = "tables.json";
  let table;
  const request = fetch(URL)
    .then(r => r.json())
    .then(tables => {
      table = tables.find(t => `${t.dataset}.${t.name}` === params.table);
      return fetch(table.bq_definition_raw_json).then(r => r.json());
    });
</script>

<style>
  .table-header {
    @apply table-auto;
    @apply my-4;
  }

  .table-header td {
    @apply border;
    @apply p-2;
  }
</style>

{#await request then nodes}
  <h1>{table.dataset}.{table.name}</h1>
  <table class="table-header">
    <tr>
      <td>BigQuery definition</td>
      <td>
        <a href={table.bq_definition}>
          {table.bq_definition.split('/').slice(-1)}
        </a>
      </td>
    </tr>
    <tr>
      <td>Live Data</td>
      <td>
        <code>{table.dataset}_live_v{table.version}.{table.name}</code>
      </td>
    </tr>
    <tr>
      <td>Stable View</td>
      <td>
        <code>{table.dataset}.{table.name}</code>
      </td>
    </tr>

  </table>

  <SchemaViewer glean_app={table.glean_app} {nodes} />
{/await}
