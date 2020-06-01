<script>
  import page from "page";

  // Pages
  import Index from "./Index.svelte";
  import TelemetryMain from "./TelemetryMain.svelte";
  import SearchClientsDaily from "./SearchClientsDaily.svelte";

  let component = Index;
  let params;

  function setComponent(c) {
    return function setComponentInner({ params: p }) {
      component = c;
      params = p;
    };
  }
  page("/", setComponent(Index));
  page("/telemetry-main", setComponent(TelemetryMain));
  page("/search-clients-daily", setComponent(SearchClientsDaily));

  page({ hashbang: true });
</script>

<svelte:component this={component} bind:params />
