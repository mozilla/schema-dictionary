<script>
  export let glean_app;
  export let node = {};
  export let parentFields = [];
</script>

<div style={node.visible ? '' : 'display: none;'}>
  <p>
    <span class="text-gray-700">
      {parentFields.join('.')}{parentFields.length ? '.' : ''}
    </span>
    <span>{node.name}</span>
  </p>
  {#if node.description}
    <p class="text-gray-600 text-xs ml-2">{node.description}</p>
  {/if}
  {#if glean_app && parentFields.length === 2 && parentFields[0] === 'metrics'}
    <p class="text-gray-600 text-xs ml-2">
      <a
        target="blank_"
        href={`https://glean-dictionary.netlify.app/?product=${glean_app}&metric=${node.name}`}>
        [view in glean dictionary]
      </a>
    </p>
  {/if}
</div>

{#if node.fields && node.childrenVisible}
  {#each node.fields as childNode}
    <svelte:self
      {glean_app}
      node={childNode}
      parentFields={[...parentFields, node.name]} />
  {/each}
{/if}
