// scripts.js
// contains all the scripts necessary to run this website
// separated by webpage

/***** sitewide *****/
function modalImage(classname) {
    let modalEle = document.querySelector(".modal");
    let modalImage = document.querySelector(".modalImage");
    let projectArray = Array.from(document.querySelectorAll(classname));
    projectArray.forEach(project => {
        let imageArray = Array.from(project.children);
        imageArray.forEach(element => {
            element.addEventListener("click", event => {
                modalEle.style.display = "block";
                modalImage.src = event.target.src;
            });
        });
    });
    modalEle.addEventListener("click", event => {
        if (event.target != modalImage) {
            modalEle.style.display = "none";
        }
    })
}

function comicDisplay(classname) {
    let comicArray = Array.from(document.querySelectorAll(classname)); //.comic
    comicArray.forEach(comic => {
        let slide_index = parseInt(comic.dataset.slideIndex);
        let imageArray = Array.from(comic.children);
        imageArray.forEach(image => { image.style.display = "none"; });
        imageArray[slide_index].style.display = "inline";
    });
}

function nextComic(parent, classname) {
    let childnodes = Array.from(parent.children);
    let comicArray;
    childnodes.forEach(child => {
        if (child.className == "comic") {
            comicArray = child;
            return;
        }
    });
    let slindex = parseInt(comicArray.dataset.slideIndex);
    slindex += 1;
    if (slindex < comicArray.childElementCount) {
        comicArray.dataset.slideIndex = slindex
        comicDisplay(classname)
    }
}

function prevComic(parent, classname) {
    let childnodes = Array.from(parent.children);
    let comicArray;
    childnodes.forEach(child => {
        if (child.className == "comic") {
            comicArray = child;
            return;
        }
    });
    let slindex = parseInt(comicArray.dataset.slideIndex);
    slindex -= 1;
    if (slindex >= 0) {
        comicArray.dataset.slideIndex = slindex;
        comicDisplay(classname);
    }
}

function submitHandler() {
    let forms = document.forms["contact"];
    console.log(forms["email"]);
    console.log(forms["message"]);
    if (forms["email"].value.includes("@") && forms["message"].value != "") {
        let contactform = document.querySelector("#contact");
        let sub_message = document.querySelector("#submission_message");
        sub_message.style.display = "inline-block";
        contactform.style.display = "none";
    }
    else {
        console.log("email and message are empty")
    }
}

function returntoTop() {
    let topbuttons = Array.from(document.querySelectorAll(".to-top"));
    topbuttons.forEach(top => {
        top.addEventListener("click", () => {
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
        });
    });
}