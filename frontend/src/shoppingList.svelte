<script>
    import { shoppingList } from "./stores"
    import ShoppingListItem from "./components/shoppingListItem.svelte"
</script>

<h1>MY NOTIFICATION LIST</h1>
<p>Items you have previously added to your shopping list will appear here</p>
<div class="container">
<div class="shopping-list">
{#each $shoppingList as shopItem}
<ShoppingListItem name={shopItem.name} currency={shopItem.currency} price = {shopItem.price} image={shopItem.image} store={shopItem.store} NotificationMethod={shopItem.notificationMethod}
date={shopItem.date} phoneNo={shopItem.phoneNumber} link={shopItem.productURL}></ShoppingListItem>
{/each}
</div>
</div>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Ubuntu:wght@300;400&display=swap');
    h1 {
        margin-top: 25px;
        font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
    }

    p {
        margin-top: 5px;
        font-family: "Roboto", sans-serif;
		font-size: 14px;
    }

    .container {
        width: 99vw;
    }

    .shopping-list {
        display:flex;
        align-items:flex-start;
        overflow-x: scroll;
    }


</style>