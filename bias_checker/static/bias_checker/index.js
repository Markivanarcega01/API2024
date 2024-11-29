const mainContent = document.querySelector(".div-inputfield")
const fileForm = document.querySelector(".file-form")
const convertBtn = document.querySelector(".convert-btn")

if(mainContent && fileForm){
    mainContent.addEventListener('input',(event)=>{
        console.log(event.target.innerText)
        if(event.target.innerText != ""){
            console.log("div has text")
            convertBtn.style.display = "block"
            fileForm.style.display = "none";
        }else{
            console.log("div has no text")
            convertBtn.style.display = "none"
            fileForm.style.display = "block"
        }
    })
}

function copyContent(){
    document.getElementById('hiddenTextArea').value = mainContent.innerHTML
    console.log('working function')
    return true;
}

//fileForm.style.display = "none";
console.log(mainContent && fileForm)
console.log("JS loadded")