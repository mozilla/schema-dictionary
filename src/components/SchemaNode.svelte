<script>
  export let node = {};
  export let parentFields = [];
</script>

<div style={node.visible ? '' : 'display: none;'}>
  <p>
    <span class="text-gray-700">{parentFields.join('.')}</span>
    <span>{node.name}</span>
  </p>
  {#if node.description}
    <p class="text-gray-600 text-xs ml-2">{node.description}</p>
  {/if}
</div>

{#if node.fields && node.childrenVisible}
  {#each node.fields as childNode}
    <svelte:self node={childNode} parentFields={[...parentFields, node.name]} />
  {/each}
{/if}
