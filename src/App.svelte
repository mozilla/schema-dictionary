<script>
  import Routes from "./routes/Routes.svelte";
  import Tailwindcss from "./Tailwindcss.svelte";
</script>

<Tailwindcss />

<nav>
  <a href="/">home</a>
  <a href="/telemetry-main">telemetry-main</a>
  <a href="/search-clients-daily">search-clients-daily</a>
</nav>

<Routes />
