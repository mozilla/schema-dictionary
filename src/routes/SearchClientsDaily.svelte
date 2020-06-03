<script>
  import marked from "marked";
  import SchemaViewer from "../components/SchemaViewer.svelte";

  const URL = "search-clients-daily.bq.json";
  const request = fetch(URL).then(r => r.json());
</script>

<h1>telemetry.search-clients-daily</h1>
<p>
  search_clients_daily is designed to enable client-level search analyses.
  Querying this dataset can be slow; consider using search_aggregates for coarse
  analyses.
</p>
<p>
  Schema:
  <a
    href="https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/master/schemas/telemetry/main/main.4.schema.json">
    mozilla-pipeline-schemas
  </a>
</p>
<p>
  Scheduling:
  <a
    href="https://github.com/mozilla/telemetry-airflow/blob/master/dags/main_summary.py">
    Airflow
  </a>
</p>

{#await request then resp}
  {@html marked(resp.docs)}
{/await}

{#await request then resp}
  <SchemaViewer nodes={resp.fields} />
{/await}
