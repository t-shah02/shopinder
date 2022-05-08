<script>

</script>
<div class="headings">
  <h1 align="center">About Us</h1>
  <hr>
  <hr>
  <h1 align="center">Meet the team</h1>
</div>

<div class="main-column">
    <div class="profile-block">
      <img src="https://cdn.discordapp.com/attachments/947020818104332338/972772918658469918/unknown.png" alt="bruh"/>
      <div class="card__content">
        <h2>Chau Pham (they/them)</h2>
        <h4>Simon Fraser University| 1st Year | Computer Science</h4>
        <p>Chau is a first-year computing science major at SFU aiming to use programming to create innovative solutions
          here</p>
      </div>
    </div>
    <div class="profile-block">
      <img src="https://cdn.discordapp.com/attachments/945541500329152522/972784202997170197/tanish.jpg" alt="bruh"/>            
      <div class="card__content">
        <h2>Tanish Shah</h2>
        <h4>Simon Fraser University | 2nd Year | Data Science </h4>
        <p>Hello world, my name is Tanish Shah. I am a data science student, who is interested in becoming more fluent in back end web development and machine learning. This project was extremely fun to design, and it really helped solve my common problem of not having a global shopping list for all of my online stores. The skills I acquired from this project, included learning how state changes worked and their power in making reactive components on your front end and desigining a good server-side backend, to handle user authentication and data modifications.</p>
      </div>
    </div>
    <div class="profile-block">
      <img src="https://cdn.discordapp.com/attachments/895138190254542948/972771910066790410/IMG_20220430_175643.jpg" alt="bruh"/>
      <div class="card__content">
        <h2>Yunxiao (Tony) Liu (he/him)</h2>
        <h4>University of British Columbia | 2nd year | Computer Engineering</h4>
        <p>Hi, my name is Tony Liu, and I am a computer engineering student with a strong passion for software development. I recognize that this is a very diverse and constantly evolving field, with plenty of aspects to explore. Going into this hackathon I knew some CSS and HTML, but had hardly any knowledge about JavaScript frameworks. As a result, developing Shopinder had its fair share of challenges. From learning JavaScript, to learning how to use Svelte to make reactive components (thank god that wasn't the most difficult challenge), to figuring out how to integrate the different aspects of our application (such as Twilio notifications, database storage, and web scraping). However, I can say that along with Chau and Tanish, we overcame these challenges, and in the process, greatly improved our web development skills. I am looking forward to using these skills to create further amazing projects, and to build a bright future for myself and the world around.</p>
      </div>
    </div>
  </div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@100;200;400&family=VT323&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300&family=Ubuntu:wght@300;400&display=swap');
.main-column {
  display:flex;
  width:90vw;
  justify-content: space-between;
}

.profile-block{
  width:360px;
  margin:40px 10px;
  padding:1rem;
  cursor:pointer;
  background-color:#9c6db8;
}
.profile-block img{
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
  margin-top:-400px;
  opacity:0;
  visibility:hidden;
  transition:all .5s ease-in-out;
  align-items:center;
}

.profile-block:hover img{
  margin-top: 1px;
  box-shadow:0 0 4px 6px rgba(0,0,0,0.3);
}
.profile-block:hover>.card__content{
  margin-top:0;
  opacity:1;
  visibility:visible;
}

h1 {
        margin-top: 18px;
        font-family: "Roboto Mono", sans-serif;
		    font-size: 36px;
        text-align : center;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 15px;
    }

  h2 {
    margin-top: 8px;
    font-family: "Roboto Mono", sans-serif;
		font-size: 24px;
    text-align : center;
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 5px;
  }

  h4 {
    margin-top: 5px;
    font-family: "Roboto Mono", sans-serif;
		font-size: 18px;
    padding-left: 10px;
    padding-right: 10px;
    text-align : center;
  }

  p {
        margin-top:5px;
        font-family: "Roboto", sans-serif;
		    font-size: 14px;
        text-align : center;
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 5px;
    }

</style>