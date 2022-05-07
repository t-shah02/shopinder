<script>
	let name = '';
	async function search() {
		let resp = await fetch("/sample")
		let respJSON = await resp.json();
		console.log(respJSON);
	}
</script>

<div class="bruh">
	<input bind:value={name} on:input = {search}>
	<h1>We will search for: {name}</h1>
</div>
<style>
	@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
	input {
		padding-top: 10px;
		padding-bottom: 10px;
		margin-left: 50px;
		margin-right: 50px;
		margin-top: 50px;
		margin-bottom: 10px;
		width:90%;
		max-width: 980px;
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

	input {
		background: transparent;
    	border: none;
    	border-bottom: 2px solid #000000;
		
	}

</style>
