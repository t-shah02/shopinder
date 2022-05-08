<script>
	import SearchItem from "./components/searchItem.svelte"
	
	const GOOD_TO_GO = "good to go!";
	const INVALID_URL = "not a valid URL, please try again!"
	const VALID_BUT_NOT_SUPPORTED = "a valid URL, but it doesn't redirect to our supported stores"
	

	// define props
	export let storesSupported;


	let searchURL = '';
	let validURLState = INVALID_URL;
	let urlMap = {
		GOOD_TO_GO:"color : green;",
		INVALID_URL:"color : red;",
		VALID_BUT_NOT_SUPPORTED:"color : yellow;"
	};
	let name;
	let currency;
	let price;
	let prodImageURL;
	let store;
	
	let displayProductCard = false;

	async function searchForItem() {
		validURLState = isValidURL(searchURL);
		console.log(validURLState,urlMap[validURLState]);
		if (validURLState == GOOD_TO_GO) {
			let endpoint_url = `/productinfo?store_name=${store}&product_url=${searchURL}`
			const resp = await fetch(endpoint_url)
			if (resp.ok) {
				const respJSON = await resp.json();
				name = respJSON.product_title;
				currency = respJSON.currency;
				prodImageURL = respJSON.product_img_link;
				price = respJSON.price_value;
				
				if (currency == null) {
					currency = ""
				}
				if (!price) {
					price = "Check website for price";
					currency = "";
				}

				if (!prodImageURL) {
					prodImageURL = "Check website for the product image";
				}
				if (!name) {
					name = "Check website for the name";
				}
				displayProductCard = true;
			}
			else {
				validURLState = "not finding anything, please try again!"
				displayProductCard = false;
			}
		}
		else {
			displayProductCard = false;
		}
	
		
	}

	function isValidURL(url) {
		let validator = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/
		if (!validator.test(url)) {
			return INVALID_URL
		}

		for (const storeName in storesSupported) {
			let baseURL = storesSupported[storeName][0];
			if (url.startsWith(baseURL)) {
				store = storeName;
				return GOOD_TO_GO
			}
		}

		return VALID_BUT_NOT_SUPPORTED
	}	
</script>

<div class="bruh">
	<input bind:value={searchURL} on:input = {searchForItem} placeholder="Please enter a URL for an item from one of our supported stores.">
	<h1 class="valid-url">The following URL is: <span style={urlMap[validURLState]}>{validURLState}</span></h1>
	{#if displayProductCard}
		<p>Hover over the image below to see product info and set up notifications</p>
		<SearchItem name={name} currency={currency} price={price} image={prodImageURL} store={store} productURL={searchURL}></SearchItem>
	{/if}
</div>
<style>
	@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
	@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Ubuntu:wght@300;400&display=swap');
	input {
		padding-top: 10px;
		padding-bottom: 10px;
		padding-left:20px;
		padding-right:20px;
		margin-left: 50px;
		margin-right: 50px;
		margin-top: 50px;
		margin-bottom: 10px;
		height:90%;
		width:90%;
		max-height:980px;
		max-width:980px;
   }
	
	.valid-url {
		font-size: 15px;
	}

	div {
		align-items: center;
		display: flex;
		flex-direction: column;
	}

	h1 {
		font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
	}

	p {
		margin-top:15px;
		font-family: "Roboto", sans-serif;
		font-size: 14px;
	}

	input {
		min-width: 500px;
		width:75%;
		background: transparent;
    	border: none;
    	border-bottom: 2px solid #000000;
		
	}

    ::placeholder {
		font-family: "Roboto", sans-serif;
  		font-size: 12px;
	}

</style>
