var cardImg = document.querySelector('.card-img')
originalImg = cardImg.src
var is_back = false
cardImg.addEventListener('click', ()=>{
    if (!is_back){
        cardImg.style.animation = "flipBack .4s ease-in-out forwards"
        cardImg.src = "https://static.wikia.nocookie.net/yugioh/images/e/ee/Back-ZX-Site.png"
        is_back = true
    }else{
        cardImg.style.animation = "flipFront .4s ease-in-out forwards"
        cardImg.src = originalImg
        is_back = false
    }
})
