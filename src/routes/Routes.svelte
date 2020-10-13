<script>
  import page from "page";

  // Pages
  import TableList from "./TableList.svelte";
  import TableView from "./TableView.svelte";
  import SearchClientsDaily from "./SearchClientsDaily.svelte";
  import MetricSearch from "./MetricSearch.svelte";

  let component = TableList;
  let params;

  function setComponent(c) {
    return function setComponentInner({ params: p }) {
      component = c;
      params = p;
    };
  }
  page("/", setComponent(TableList));
  page("/tables/:table", setComponent(TableView));
  page("/search-clients-daily", setComponent(SearchClientsDaily));
  page("/metric-search", setComponent(MetricSearch));
  page.exit("*", function(ctx, next) {
    ga("set", "page", ctx.page.current);
    ga("send", "pageview");
    next();
  });

  page({ hashbang: true });
</script>

<style>
  .active-link {
    @apply text-blue-100;
  }

  .brand {
    @apply text-gray-100;
  }
</style>

<nav class="flex items-center justify-between flex-wrap bg-blue-800 p-2">
  <div class="flex items-center flex-shrink-0 mr-6">
    <a class="brand font-semibold text-xl tracking-tight" href="/">
      Schema Dictionary&nbsp;
      <i>Prototype</i>
    </a>
  </div>
  <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
    <div class="text-sm space-x-2 lg:flex-grow">
      <a class={component === TableList ? 'active-link' : ''} href="/">home</a>
      <a
        class={component === SearchClientsDaily ? 'active-link' : ''}
        href="/search-clients-daily">
        search-clients-daily-DEMO
      </a>
    </div>
  </div>
</nav>

<div class="container py-4 mx-auto">

  <svelte:component this={component} bind:params />

</div>
