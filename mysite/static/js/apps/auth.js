// Authentication modal window
let authModal =  document.getElementById("auth-modal");
let accountBtn = document.getElementById("header-account-btn");
let cancelBtn = document.getElementById("auth-cancel-btn");
let authLink = document.getElementById("auth-modal-link");

cancelBtn.onclick = () => authModal.classList.remove("show");
accountBtn.onclick = () => authModal.classList.add("show");
authLink.onclick = () => ToggleLoginOrRegister(authLink);

function ToggleLoginOrRegister(authLink) {
    let authArticle = document.getElementById("auth-modal-article");
    let authForm = document.getElementById("auth-modal-form");
    
    // Exchange texts between article and link below
    let temp = authLink.innerText;
    authLink.innerText = authArticle.innerText;
    authArticle.innerText = temp;

    // Toggle hidden fields (username and repeat password)
    document.getElementById("auth-modal-username").classList.toggle("hidden");
    document.getElementById("auth-modal-repeat").classList.toggle("hidden");

    let actionTxts = {
        login: "Login",
        reg: "Create account",
        changeToLogin: "Already have an accoun? Login!",
        changeToReg: "No account? Create new!"
    };

    if (authForm.getAttribute("action") == "register") {
        // Change to login form
        authForm.setAttribute("action", "login");
        //authForm.classList.remove("reg");
        //authForm.classList.add("login");

        authArticle.innerText = actionTxts.login;
        authLink.innerText = actionTxts.changeToReg;
    } else { 
        // Change to register form
        authForm.setAttribute("action", "register");
        //authForm.classList.remove("login");
        //authForm.classList.add("reg");

        authArticle.innerText = actionTxts.reg;
        authLink.innerText = actionTxts.changeToLogin;
    }

};
// 

