<script>
  import SchemaViewer from "../components/SchemaViewer.svelte";

  const URL = "/main.4.bq.json";
  const request = fetch(URL).then(r => r.json());
</script>

<div class="container mx-auto">
  <h1>telemetry.main</h1>
  <p>
    This table represents a stable view of the main ping. It is updated daily.
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
  {#await request then nodes}
    <SchemaViewer {nodes} />
  {/await}

</div>
