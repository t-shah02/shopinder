<script>
    import Popup from "./popup.svelte"
    import { shoppingList } from "../stores.js"
    export let name;
    export let currency;
    export let price;
    export let image;
    export let store;
    export let productURL;

    let popup;

    let notificationMethod;
    let date;
    let phoneNo;

    let isSetUpNotification = false;

    let showErrorMessage = false;
    let showTelePhoneErrorMessage = true;
    let showDuplicateItemMessage = false;

    function setupNotification(){
        isSetUpNotification = true;
    }

    function close() {
        isSetUpNotification = false;
    }

    function validatePhoneNumber(number) {
      let validator = /^(\+?1 ?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/
      return validator.test(number);
    }
    
    function phoneChange() {
      let phoneCheck = validatePhoneNumber(phoneNo);
      if (phoneCheck) {
        showTelePhoneErrorMessage = false;
      }
      else {
        showTelePhoneErrorMessage = true;
      }
    }
    
    
    async function handleAddItem() {
      
      if (notificationMethod == null || date == null || (notificationMethod=="Phone" && (phoneNo == null || phoneNo == "")) && showTelePhoneErrorMessage) {
        showErrorMessage = true;
      }
      else {
        showErrorMessage = false;

        for (let i = 0; i < $shoppingList.length; i++) {
          if ($shoppingList[i].productURL == productURL) {
            showDuplicateItemMessage = true;
            return;
          }
        }
        
        showDuplicateItemMessage = false;

        let shoppingItemData = {
          name : name,
          currency : currency,
          price : price,
          image : image,
          store : store,
          notificationMethod : notificationMethod,
          phoneNumber : phoneNo,
          date : date,
          productURL : productURL
        }
        shoppingList.set([...$shoppingList,shoppingItemData])
        let currentCache = JSON.parse(localStorage.getItem("data"));
        currentCache.shopping_list.push(shoppingItemData);
        localStorage.setItem("data",JSON.stringify(currentCache))
        
        // make request to the backend to update the MongoDB database

        let reqBody = {
          googleID : currentCache["_id"],
          itemData : shoppingItemData
        }

        let payLoad = {
          method : 'POST',
          headers: {
            'Content-Type': 'application/json'},
          body : JSON.stringify(reqBody)
      }

        let response = await fetch("/additem",payLoad);
        if (response.ok) {
          // console.log("mongodb worked")
        }

      
    }
  }

</script>

<div class="container">
<div class="card">
    <img src={"https://media.discordapp.net/attachments/894109258235396118/972693222302306384/unknown.png" || image} alt="image"/>
    <div class="card__content">
        <h1>{name}</h1>
        <h2>Store name: {store}</h2>
        <h3>Price: {price} {currency}</h3>
        <br>
        <button on:click={()=> popup.show()}>Add Notification</button>
        <Popup bind:this={popup}>
            <div class="popupBox">
                    <label for="method">How would you like to be notified?
                        <fieldset class="notifications">
                            <div>
                                <input type="radio" id="email" name="field1" bind:group={notificationMethod} value={"Email"}>
                                <label for="email">Email</label>
                            </div>
                            <div>
                                <input type="radio" id="phone" name="field1" bind:group={notificationMethod} value={"Phone"}>
                                <label for="phone">Phone</label>
                            </div>
                        </fieldset>
                    </label>
                    {#if notificationMethod == "Phone"}
                        <label for="phone">Phone Number (format: xxx-xxx-xxxx):
                            <input on:input={phoneChange} bind:value={phoneNo} placeholder="Please enter a valid phone number." type="text">
        
                        </label>
                        {#if showTelePhoneErrorMessage}
                          <h1 class="error-heading">Invalid phone number</h1>
                        {/if}
                    {/if}
                    <label for="time">When would you like to be notified?
                        <div>
                            <input type="datetime-local" id="when" min="2022-05-07T00:00" max="2028-06-14T00:00" bind:value={date}>
                        </div>
                    </label>
                    <button class="submit" type="button" on:click={handleAddItem}>Add item to shopping list</button>
                    {#if showErrorMessage}
                      <h1 class="error-heading">Please fill out every field!</h1>
                    {/if}
                    {#if showDuplicateItemMessage}
                      <h1 class="error-heading">Duplicate item detected, please try again!</h1>
                    {/if}
            </div>
        </Popup>
    </div>
</div>
</div>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Ubuntu:wght@300;400&display=swap');
    label {
        font-family:"Roboto Mono", sans-serif;
        font-size: 15px;
        padding-top:5px;
        padding-bottom:5px;
    }

    .error-heading {
      font-family:"Roboto Mono", sans-serif;
      font-size: 15px;
      color : red;
    }

    fieldset {
        margin: 10px auto;
        border:none;
    }

    .popupBox {
        margin-top: 25px;
    }
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

    h2 {
        font-family: "Roboto Mono", sans-serif;
		font-size: 18px;
        text-align : center;
    }

    h3 {
        margin-top: 5px;
        font-family: "Roboto", sans-serif;
		font-size: 14px;
        text-align : center;
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

    @media screen and (max-width:800px){
  .container{
    flex-wrap:wrap;
  }
}

input[type=text]{
		min-width: 500px;
		width:75%;
		background: transparent;
    	border: none;
    	border-bottom: 2px solid #000000;
		padding-top:5px;
        padding-bottom:5px;
	}

input[type=datetime-local] {
    margin-top:5px;
    padding-top: 8px;
    padding-bottom:4px;
    padding-left:5px;
    padding-right:5px;
    background-color:#9c6db8;
    margin-bottom:20px;
    border: none;
    border-bottom: 2px solid #000000;
}

.notifications {
  margin: 10px;
}

.notifications input[type="radio"] {
  opacity: 0;
  position: fixed;
  width: 0;
}

.notifications label {
    display: inline-block;
    background-color: #fff;
    padding: 10px 20px;
    font-family: "Roboto", sans-serif;
    font-size: 16px;
    border: 2px solid #444;
    border-radius: 4px;
}

.notifications label:hover {
  background-color: rgba(255,231,235,255);
}

.notifications input[type="radio"]:focus + label {
    border: 2px solid #444;
}

.notifications input[type="radio"]:checked + label {
    background-color: rgba(255,231,235,255);
    border-color: green;
}

</style>