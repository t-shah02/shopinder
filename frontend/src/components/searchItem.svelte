<script>
    import popup from "./popup.svelte"
    export let name;
    export let currency;
    export let price;
    export let image;
    export let store;

    function setupNotification(){

    }
</script>

<div class="card">
    <h1>{name}</h1>
    <div class="divider">
        <div class="image">
            <img src={image} alt="searchItem image" width=90%/>
        </div>
        <div class="text">
            <div>
                <h2>Store name: {store}</h2>
                <h3>Price: {price}</h3>
                <h3>Currency: {currency}</h3>
            </div>
            <button>Add Notification</button>
        </div>
    </div>
   
</div>

<style>
    .card {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
        background-color: #8e749d;
        max-width: 50%;
    }
    .divider {
        display:flex;
        justify-content:space-between;
        margin-bottom:25px;
    }

    .image {
        padding-left:30px;
        padding-right:10px;
        width:50%;
    }

    .text {
        display:flex;
        flex-direction: column;
        justify-content: space-between;
        padding-left:10px;
        padding-right:30px;
        width: 50%;
        overflow-wrap: break-word;
    }

    h1 {
        margin-top: 25px;
        font-family: "Roboto Mono", sans-serif;
		font-size: 32px;
        text-align : center;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 15px;
    }

    h2 {
        font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
    }

    h3 {
        margin-top: 5px;
        font-family: "Roboto", sans-serif;
		font-size: 16px;
    }

    button {
        align-items: center;
        background-color: #FFFFFF;
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: .25rem;
        box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
        box-sizing: border-box;
        color: rgba(0, 0, 0, 0.85);
        cursor: pointer;
        display: inline-flex;
        font-family: "Roboto",sans-serif;
        font-size: 16px;
        justify-content: center;
        line-height: 1.25;
        margin: 0;
        min-height: 3rem;
        padding: calc(.875rem - 1px) calc(1.5rem - 1px);
        position: relative;
        text-decoration: none;
        transition: all 250ms;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: baseline;
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

</style>