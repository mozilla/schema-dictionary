<script>
  import page from "page";

  // Pages
  import Index from "./Index.svelte";
  import TelemetryMain from "./TelemetryMain.svelte";
  import SearchClientsDaily from "./SearchClientsDaily.svelte";

  let component = Index;
  let params;

  page("/", p => {
    if (p.hash === "telemetry-main") {
      component = TelemetryMain;
    } else if (p.hash === "search-clients-daily") {
      component = SearchClientsDaily;
    } else {
      component = Index;
    }
  });
  page.start();
</script>

<svelte:component this={component} />
