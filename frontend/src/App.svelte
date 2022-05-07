<script>
  import { isUserLoggedIn, name } from './stores.js';
  import Navbar from './Navbar.svelte'
  import LoginPanel from "./components/LoginPanel.svelte"
  import AppHeading from "./components/AppHeading.svelte"
  import Search from "./search.svelte"
  import List from "./list.svelte"


  let userLoggedIn;
  isUserLoggedIn.subscribe(value => {
    userLoggedIn = value;
  });

  let userName;

  name.subscribe(value => {
    userName = value;
  });

</script>


{#if userLoggedIn}
  <Navbar names={userName.toUpperCase()}/>
  <div class="loggedin">
    <Search></Search>
    <br>
    <List></List>
  </div>
{:else}
  <AppHeading></AppHeading>
  <LoginPanel></LoginPanel>
{/if}

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');

  .loggedin {
    display:flex;
    flex-direction:column;
    align-items:center;
  }

  .lp {
    align-items: center;
  }

</style>