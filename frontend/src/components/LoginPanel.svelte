<script>
  import { isUserLoggedIn, name } from '../stores.js';
  window.onSignIn = (googleUser) => {
     const profile = googleUser.getBasicProfile();
     console.log('ID: ' + profile.getId());
     console.log('Name: ' + profile.getName());
     console.log('Image URL: ' + profile.getImageUrl());
     console.log('Email: ' + profile.getEmail());
     isUserLoggedIn.set(true);
     name.set(profile.getName());
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
