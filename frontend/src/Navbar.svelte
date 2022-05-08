<script>
    import { onMount } from "svelte";
    import { isAboutOn } from "./stores.js";
    import GoogleLogoutButton from "./components/GoogleLogoutButton.svelte";
    // Show mobile icon and display menu
    let showMobileMenu = false;
    let isAboutSet = false;
    let isClose="";
    export let names;
    export let numItems;
  
    // Mobile menu click event handler
    const handleMobileIconClick = () => (showMobileMenu = !showMobileMenu);
  
    // Media match query handler
    const mediaQueryHandler = e => {
      // Reset mobile state
      if (!e.matches) {
        showMobileMenu = false;
      }
    };
    
    // Attach media query listener on mount hook
    onMount(() => {
      const mediaListener = window.matchMedia("(max-width: 767px)");
  
      mediaListener.addListener(mediaQueryHandler);
    });

    function setAbout() {
      isAboutSet = !isAboutSet;
      if (isAboutSet == true) {
        isClose = "Close ";
      }
      else {
        isClose = "";
      }
      update();
    }

    function update(){
      isAboutOn.set(isAboutSet);
    }
  </script>
  
  <nav>
    <div class="inner">
      <div on:click={handleMobileIconClick} class={`mobile-icon${showMobileMenu ? ' active' : ''}`}>
        <div class="middle-line"></div>
      </div>
      <ul class={`navbar-list${showMobileMenu ? ' mobile' : ''}`}>
          <li>
            <p>Welcome back, {names}</p>
          </li>
          <li>
            <p>{numItems} items in list</p>
          </li>
          <li>
            <button on:click={setAbout}>{isClose}About Us</button>
          </li>
        <li>
        <GoogleLogoutButton></GoogleLogoutButton>
        </li>
      </ul>
    </div>
  </nav>
  
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
button {
  color: white;
  background-color:transparent;
  border:none;
  height:100%;
  padding: 14px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-family:"Roboto Mono", sans-serif;
  font-size:20px;
}

button:hover, button:active {
  background-color: #b00b69;
}

    nav {
      background-color : purple;
      font-size: 20px;
      height: 60px;
    }


    .inner {
      max-width: 9000px;
      padding-left: 20px;
      padding-right: 20px;
      margin: auto;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      height: 100%;
    }
  
    .mobile-icon {
      width: 25px;
      height: 14px;
      position: relative;
      cursor: pointer;
    }
  
    .mobile-icon:after,
    .mobile-icon:before,
    .middle-line {
      content: "";
      position: absolute;
      width: 100%;
      height: 2px;
      background-color: #fff;
      transition: all 0.4s;
      transform-origin: center;
    }
  
    .mobile-icon:before,
    .middle-line {
      top: 0;
    }
  
    .mobile-icon:after,
    .middle-line {
      bottom: 0;
    }
  
    .mobile-icon:before {
      width: 66%;
    }
  
    .mobile-icon:after {
      width: 33%;
    }
  
    .middle-line {
      margin: auto;
    }
  
    .mobile-icon:hover:before,
    .mobile-icon:hover:after,
    .mobile-icon.active:before,
    .mobile-icon.active:after,
    .mobile-icon.active .middle-line {
      width: 100%;
    }
  
    .mobile-icon.active:before,
    .mobile-icon.active:after {
      top: 50%;
      transform: rotate(-45deg);
    }
  
    .mobile-icon.active .middle-line {
      transform: rotate(45deg);
    }
  
    .navbar-list {
      display: none;
      width: 100%;
      justify-content: space-between;
      margin: 0;
      padding: 0 40px;
    }
  
    .navbar-list.mobile {
      background-color: rgba(37, 248, 255, 0.8);
      position: fixed;
      display: block;
      height: calc(100% - 60px);
      bottom: 0;
      left: 0;
    }
  
    .navbar-list li {
      list-style-type: none;
      position: relative;
    }
  
    .navbar-list li:before {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 1px;
      background-color: #fff;
    }
  
    .navbar-list p {
      color: #fff;
      text-decoration: none;
      display: flex;
      justify-content: space-between;
      height: 60px;
      align-items: center;
      font-size: 20px;
      font-family: 'Roboto Mono', sans-serif;
    }
  
    @media only screen and (min-width: 767px) {
      .mobile-icon {
        display: none;
      }
  
      .navbar-list {
        display: flex;
        padding: 0;
      }
  
      .navbar-list a {
        display: inline-flex;
      }
    }
  </style>