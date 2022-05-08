<script>
   let shown = false;

   export function show() {
       shown = true;
   }

   export function close() {
       shown = false;
   }

</script>

<svelte:window
  on:keydown={e => {
    if (e.key == 27) {
      close();
    }
  }} />

{#if shown}
<span class="close" on:click={() => close()}>&times;</span>
<slot />
{/if}

<style>

    .close {
        float: right;
        cursor: pointer;
        font-size: 50px;
    }

    .close:hover {
        font-weight: 1000;
    }
</style>