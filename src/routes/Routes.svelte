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

<style>
  .active-link {
    @apply text-blue-100;
  }
</style>

<nav class="flex items-center justify-between flex-wrap bg-blue-800 p-2">
  <div class="flex items-center flex-shrink-0 text-white mr-6">
    <span class="font-semibold text-xl tracking-tight">
      Schema Dictionary
      <i>Prototype</i>
    </span>
  </div>
  <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
    <div class="text-sm space-x-2 lg:flex-grow">
      <a class={component.name === 'Index' ? 'active-link' : ''} href="/">
        home
      </a>
      <a
        class={component.name === 'TelemetryMain' ? 'active-link' : ''}
        href="/telemetry-main">
        telemetry-main
      </a>
      <a
        class={component.name === 'SearchClientsDaily' ? 'active-link' : ''}
        href="/search-clients-daily">
        search-clients-daily
      </a>
    </div>
  </div>
</nav>

<svelte:component this={component} bind:params />
