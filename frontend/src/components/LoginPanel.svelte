<script>
  import { isUserLoggedIn, name, email, phoneNumber, shoppingList } from '../stores.js';
  window.onSignIn = async (googleUser) => {

     var profile = googleUser.getBasicProfile();
     var logged = gapi.auth2.getAuthInstance().isSignedIn.get();
     
     if (logged && "data" in localStorage) {
       let cachedData = JSON.parse(localStorage.getItem("data"));
       name.set(cachedData.name);
       email.set(cachedData.email);
       phoneNumber.set(cachedData.phone_number);
       shoppingList.set(cachedData.shopping_list);
       isUserLoggedIn.set(true);
       return;
     }

     var fullName = profile.getName();
     var userEmail = profile.getEmail();
     var subID = profile.getId(); 
    
     let infoBody = {
       fullname : fullName,
       email : userEmail,
       subID : subID
     }

     let payLoad = {
       method : 'POST',
       headers: {
        'Content-Type': 'application/json'},
       body : JSON.stringify(infoBody)
     }

     const userResponse = await fetch("/user",payLoad);
     const userJSON = await userResponse.json();
     console.log(userJSON)
     name.set(userJSON.name);
     isUserLoggedIn.set(true);
     email.set(userJSON.email);
     phoneNumber.set(userJSON.phone_number);
     shoppingList.set(userJSON.shopping_list);
     
     localStorage.setItem("data",JSON.stringify(userJSON));
  };
</script>

<svelte:head>
  <script src="https://apis.google.com/js/platform.js?onload=onLoadCallback" async defer></script>
</svelte:head>

<div class="login-container">
  <h1 class="join-us-heading">Join us today!</h1>
  <img alt="bag clock img" class="bag-clock" src="https://media.discordapp.net/attachments/946229978373161010/972319906118922280/unknown.png?width=625&height=472">
  <div class="social-auth-container">
    <h1 class="signup-reg-heading">Google:</h1>
    <div class="g-signin2" data-longtitle="true" data-onsuccess="onSignIn" />
  </div>
</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');

  .join-us-heading {
    font-family: 'Roboto Mono', monospace;
    font-size : 20px;
    text-align : center;
  }

  .bag-clock {
    width : 25%;
    height : 25%;
    display : block;
    margin-left : auto;
    margin-right : auto;
  }

  .g-signin2 {
    margin-bottom : 25px;
    margin-left : 20px;
  }

  .login-container {
    width : 450px;
    display : block;
    margin-left : auto;
    margin-right : auto;
    margin-top : 50px;
    border-radius : 10px;
  }
  
  .social-auth-container {
    display : flex;
    justify-content : center;
    margin-top : 30px;
  }

  .signup-reg-heading {
    font-family: 'Roboto Mono', monospace;
    font-size : 15px;
    text-align : center;
    margin-top : 7px;
  }

</style>
