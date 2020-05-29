<script>
  import SchemaNode from "./SchemaNode.svelte";
  export let nodes = [];
  export let filterText = "";

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

<div class="container schema-browser mx-auto">
  <p>
    {#each nodesWithVisibility as node}
      <SchemaNode {node} />
    {/each}
  </p>
</div>
