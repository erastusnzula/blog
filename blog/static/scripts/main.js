let category = document.querySelector(".category-items")
let categories = document.getElementById('category-link')
let dropdownMenu = document.getElementById("nav-dropdown-menu")

categories.addEventListener('mouseover',() =>{
    dropdownMenu.style.display = 'grid'
})

categories.addEventListener('click',() =>{
    dropdownMenu.style.display = 'grid'
})

category.addEventListener('mouseleave',() =>{
    dropdownMenu.style.display = 'none'
})


const goToTopButton = document.getElementById("to-top");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    goToTopButton.style.display = "block";
  } else {
    goToTopButton.style.display = "none";
  }
}

function goToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

const copyright = document.getElementById("copyright")
copyright.innerHTML += " " + new Date().getFullYear()

function closeIconFunction(){
  const messages = document.getElementById("messages")
  messages.style.display="none"
}

const changeTheme = document.getElementById("change-theme")
const lightTheme= document.getElementById("light-mode")
const darkMode = document.getElementById("dark-mode")
let change = false
const selectedTheme = localStorage.getItem('selected-theme')

function toLightMode(){
  lightTheme.style.backgroundColor="rgb(245, 239, 239)"
  darkMode.style.backgroundColor="rgb(54, 51, 51)"
  changeTheme.title="switch to dark mode"
  change=false
}

function toDarkMode(){
  lightTheme.style.backgroundColor="rgb(54, 51, 51)"
  darkMode.style.backgroundColor="rgb(245, 239, 239)"
  changeTheme.title="switch to light mode"
  change=true
}


changeTheme.addEventListener('dragover',()=>{themeChange()})
const themeChange= ()=>{

  changeTheme.addEventListener("click", ()=>{
    if(change){
      // In light mode.
      toLightMode()
    }else{
      // In dark mode.
      toDarkMode()
    }
  })
}

themeChange()

if (selectedTheme){
  if (selectedTheme == 'light'){
    toLightMode()
  }else{
    toDarkMode()
  }

}


document.addEventListener("DOMContentLoaded", function(event) {
  if (selectedTheme){document.documentElement.setAttribute("data-theme", selectedTheme);
}else{document.documentElement.setAttribute("data-theme", "light");}
  
  changeTheme.onclick = function() {
    let currentTheme = document.documentElement.getAttribute("data-theme");
    let switchTheme = currentTheme === "dark" ? "light" : "dark"
    document.documentElement.setAttribute("data-theme", switchTheme);
    localStorage.setItem('selected-theme', switchTheme)
  }
});

const collapseBar = document.querySelector(".collapse")
const navItems = document.querySelector(".nav-items")
const topBar = document.querySelector(".top-bar")
const mediumBar = document.querySelector(".medium-bar")
const bottomBar = document.querySelector(".bottom-bar")
const navBar = document.querySelector(".navbar")

collapseBar.addEventListener("click",()=>{
  collapseBar.classList.toggle("show-navbar")
  navItems.classList.toggle("show-navbar")
  topBar.classList.toggle("show-navbar")
  mediumBar.classList.toggle("show-navbar")
  bottomBar.classList.toggle("show-navbar")
  navBar.classList.toggle("show-navbar")

})

const navLink = document.querySelectorAll(".nav-link")

navLink.forEach(n=>n.addEventListener('click',()=>{
  collapseBar.classList.remove("show-navbar")
  navItems.classList.remove("show-navbar")
  topBar.classList.remove("show-navbar")
  mediumBar.classList.remove("show-navbar")
  bottomBar.classList.remove("show-navbar")
  

}))


const showSideBar = document.querySelector(".show-about-me")
const postContainer = document.querySelector(".post-container")
const getSideBar = document.querySelector(".side-bar")
const postsTitles = document.querySelector(".posts-titles-container")

if(getSideBar){
  showSideBar.addEventListener("click",()=>{
    getSideBar.classList.toggle("active")
    postContainer.classList.toggle("in-active")
    postsTitles.style.display='none'
  
})
}
