<script>
    import { shoppingList } from "../stores"
    export let name;
    export let currency;
    export let price;
    export let image;
    export let store;
    export let NotificationMethod;
    export let date;
    export let phoneNo;
    export let link;
    let date1 = date.replace("T", " ");

    if (image == "Check website for the product image") {
        image = "https://media.discordapp.net/attachments/894109258235396118/972693222302306384/unknown.png"
    }

    let data = {"Store":store, "Price":price + " " + currency, "Notification Method": NotificationMethod, "Notification Time":date1};
    let keys = Object.keys(data);
    let values = Object.values(data);
    let entries = Object.entries(data);

    async function remove() {
        const filteredShoppingList = [];
        for (let i = 0; i < $shoppingList.length; i++) {
            if ($shoppingList[i].productURL != link) {
                filteredShoppingList.push($shoppingList[i]);
            }
        }
        
        shoppingList.set(filteredShoppingList);
        const userCache = JSON.parse(localStorage.getItem("data"))
        userCache.shopping_list = filteredShoppingList;
        localStorage.setItem("data", JSON.stringify(userCache));

        let reqBody = {
          googleID : userCache["_id"],
          updatedShoppingList : filteredShoppingList
        }

        let payLoad = {
          method : 'POST',
          headers: {
            'Content-Type': 'application/json'},
          body : JSON.stringify(reqBody)
      }

        let response = await fetch("/removeitem",payLoad);
        if (response.ok) {
          // console.log("mongodb worked")
        }
        
    }

</script>

<div class="container">
    <div class="card">
        <img src={image} alt="image"/>
        <div class="card__content">
            <h1>{name}</h1>
            {#each entries as [key, value]}
            <h3>{key}: {value}</h3>
            {/each}
            {#if phoneNo != null}
            <h3>Phone Number: {phoneNo}</h3>
            {/if}
            <div class="product-link">
                <a target="_blank" href={link}>Link to website</a>
            </div>
            <button class="remove" on:click={remove}>REMOVE</button>
        </div>
    </div>
</div>
<style>
.container{
  max-width:1000px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.card{
  width:360px;
  margin:40px 10px;
  padding:1rem;
  cursor:pointer;
  background-color:#9c6db8;
}
.card img{
  width:100%;
  border-radius:10px;
  position:relative;
  z-index:1000;
  transition:all .5s ease-in-out;
}
.card__content{
  margin:1rem 0;
  color:#222;
  overflow:hidden;
  margin-top:-200px;
  opacity:0;
  visibility:hidden;
  transition:all .5s ease-in-out;
  align-items:center;
}

.card:hover img{
  margin-top: 1px;
  box-shadow:0 0 4px 6px rgba(0,0,0,0.3);
}
.card:hover>.card__content{
  margin-top:0;
  opacity:1;
  visibility:visible;
}

    h1 {
        margin-top: 18px;
        font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
        text-align : center;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 15px;
    }

    h3 {
        margin-top: 5px;
        font-family: "Roboto", sans-serif;
		font-size: 14px;
        text-align : center;
    }

.product-link {
    padding-top:5px;
    padding-bottom:5px;
    padding-left:5px;
    padding-right:5px;
    margin-top:10px;
    text-align:center;
}

a:link, a:visited {
  background-color:  #FFFFFF;;
  color: black;
  padding: 14px 25px;
  font-family: "Roboto",sans-serif;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  border-radius: .25rem;
}

button {
        margin-top: 8px;
        background-color: #FFFFFF;
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: .25rem;
        box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
        box-sizing: border-box;
        color: rgba(0, 0, 0, 0.85);
        cursor: pointer;
        display: block;
        margin-left : auto;
        margin-right : auto;
        font-family: "Roboto",sans-serif;
        font-size: 16px;
        justify-content: center;
        line-height: 1.25;
        min-height: 3rem;
        padding: calc(.875rem - 1px) calc(1.5rem - 1px);
        position: relative;
        text-decoration: none;
        transition: all 250ms;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        width: auto;
    }

    button:hover,
    button:focus {
        border-color: rgba(0, 0, 0, 0.15);
        box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
        color: rgba(0, 0, 0, 0.65);
        background-color: rgba(255,231,235,255);
    }

    button:hover {
        transform: translateY(-1px);
    }

    button:active {
        background-color: rgba(255,231,235,255);
        border-color: rgba(0, 0, 0, 0.15);
        box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
        color: rgba(0, 0, 0, 0.65);
        transform: translateY(0);
    }
    a:hover, a:active {
        background-color: rgba(255,231,235,255);
    }
</style>