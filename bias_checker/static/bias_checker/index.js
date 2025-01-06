const mainContent = document.querySelector(".div-inputfield")
const fileForm = document.querySelector(".file-form")
const convertBtn = document.querySelector(".convert-btn")
const upouLinks = document.querySelector('.upou-links')

if(mainContent && fileForm){
    mainContent.addEventListener('input',(event)=>{
        console.log(event.target.innerText)

        if(event.target.innerText == "" || event.target.childNodes[0].nodeName === "BR"){
            console.log("div has no text")
            convertBtn.style.display = "none"
            fileForm.style.display = "block"
        }else{
            console.log("div has text")
            convertBtn.style.display = "block"
            fileForm.style.display = "none";
        }
    })
}

window.addEventListener('resize',function(){
    if(this.window.innerWidth < 768){
        upouLinks.style.display = 'none'
    }else{
        upouLinks.style.display = 'block'
    }
})

window.addEventListener('load',function(){
    if(this.window.innerWidth < 768){
        upouLinks.style.display = 'none'
    }else{
        upouLinks.style.display = 'block'
    }
})


function copyContent(){
    document.getElementById('hiddenTextArea').value = mainContent.innerText
    console.log('working function')
    return true;
}

//fileForm.style.display = "none";
console.log(mainContent && fileForm)
console.log("JS loadded")