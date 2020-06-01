<script>
  import SchemaNode from "./SchemaNode.svelte";
  export let nodes = [];
  let filterText = "";

  $: filterTerms = filterText
    .trim()
    .split(" ")
    .filter(t => t.length > 0);

  const addVisibility = node => {
    node.fields && node.fields.forEach(addVisibility);
    node.visible =
      filterTerms.length === 0 ||
      filterTerms.every(term => node.name.includes(term));
    nodes.childrenVisible =
      node.fields &&
      node.fields.some(child => child.visible || child.childrenVisible);
    return node;
  };

  $: nodesWithVisibility = filterTerms != undefined && nodes.map(addVisibility);
</script>

<h2>Schema</h2>
<div class="container py-4 mx-auto">
  <input
    class="shadow appearance-none border rounded w-full p-2 text-gray-700
    leading-tight focus:outline-none focus:shadow-outline"
    type="text"
    bind:value={filterText}
    placeholder="filter terms" />
</div>
<div class="container schema-browser mx-auto">
  <p>
    {#each nodesWithVisibility as node}
      <SchemaNode {node} />
    {/each}
  </p>
</div>
