
<script>
    export let storesSupported;
</script>

<h1 class="supported-stores-heading">Online stores that are supported by us:</h1>

<div class="icon-row">
    {#each Object.entries(storesSupported) as [storeName, urls]}
    <figure>
        <img class="store-icon" src={urls[1]}
           alt={storeName}>
        <figcaption class="icon-caption">{storeName}</figcaption>
    </figure>    
    {/each}
</div>


<style>

    .supported-stores-heading {
        font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
        margin-top : 15px;
    }

    .icon-caption {
        text-align : center;
        font-family: "Roboto Mono", sans-serif;
		font-size: 15px;
    }

    .icon-row {
        display : flex;
        margin-top : 20px;
    }

    .store-icon {
        width : 100px;
        height : 100px;
        margin-left : 10px;
        margin-right : 10px;
    }
</style>