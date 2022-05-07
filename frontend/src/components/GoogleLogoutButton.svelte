<script>
    import { isUserLoggedIn, name } from '../stores.js';
    window.signOut = () => {
      const auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(() => {
        
      });
      isUserLoggedIn.set(false);
      name.set('[]');
    }
  </script>
  
<a href="/" on:click={window.signOut}>Sign out</a>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
a:link, a:visited {
  color: white;
  height:100%;
  padding: 14px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-family:"Roboto Mono", sans-serif;
}

a:hover, a:active {
  background-color: #b00b69;
}
</style>