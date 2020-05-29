<script>
  export let node = {};
  export let parentFields = [];
</script>

<p style={node.visible ? '' : 'display: none;'}>
  <span class="less-important">{parentFields.join('.')}</span>
  <span>{node.name}</span>
</p>
{#if node.fields}
  {#each node.fields as childNode}
    <svelte:self node={childNode} parentFields={[...parentFields, node.name]} />
  {/each}
{/if}
