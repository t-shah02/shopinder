

<div class="app-heading-container">
    <img class="shopinder-logo-img" src="https://media.discordapp.net/attachments/945541500329152522/972323213063372841/shopinder-logo.png" alt="logo"/>
    <h1 class="app-title-heading">SHOPINDER</h1>
    <h1 class="animated-text-heading"> <img class="shopping-cart.png" src="https://cdn.discordapp.com/attachments/947691654901559326/972676010090835979/shopping-cart.png" alt="shopping cart"/><img class="dollar-sign.png" src="https://cdn.discordapp.com/attachments/947691654901559326/972675979308826634/dollar-sign.png" alt="dollar sign"/> <span id="typed-word"></span></h1>
</div>

<script>
    import Typed from 'typed.js';

    const EXPRESSIONS = ["Your friendly shopping list reminder!"
    , "So you never forget to buy an item ever again!"
    , "So you remember to buy black pants before your first day of work!",
    " We will remind you when there is a back to school sale",
    "100% off needing to remember",
    "Online shopping is no longer a hassle",
    "Gives SMS notifications in real time for your shopping list",
    "Created by Tanish, Tony and Chau"];
    
    let animatedExpressions = [];
    const numPhrases = 4;
    while (animatedExpressions.length < numPhrases) {
        let randIndex = Math.floor(Math.random()*EXPRESSIONS.length);
        let pickedElement = EXPRESSIONS[randIndex];
        if (EXPRESSIONS.includes(pickedElement)) {
            animatedExpressions.push(pickedElement);
        }
    }

    window.onload = () => {
        var options = {
        strings: animatedExpressions,
        typeSpeed: 30,
        backSpeed : 30,
        smartBackspace : true,
        loop : true,
        cursorChar : null
      };
    
        var typed = new Typed('#typed-word', options);
    }
    
    
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
    
    .animated-text-heading {
        text-align: center;
    }
    
    .shopinder-logo-img {
        display : block;
        margin-left : auto;
        margin-right : auto;
        margin-top : 30px;
        width : 25%;
        height : 25%;
        transition : transform 200ms ease-in-out;
        
    }
    
    #typed-word {
        color: rgba(37, 248, 255, 0.8);
        font-family: 'Roboto Mono', monospace;
        font-size : 25px;

    }

    .shopinder-logo-img:hover {
        transform : scale(1.05);
    }

    .app-title-heading {
        text-align : center;
        padding-top : 10px;
        font-family: 'Roboto Mono', monospace;
        font-size: 40px;
        color : #B00B69;
        font-style: italic;
        transition : color 200ms ease-in-out;
    }

    .app-title-heading:hover {
        color : #620e7e;
    }

</style>