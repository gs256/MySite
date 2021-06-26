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

    // Toggle hidden fields (email and repeat password)
    let emailField = document.getElementById("auth-modal-email");
    emailField.classList.toggle("hidden");
    emailField.required = !emailField.required;

    let confirmPasswordField = document.getElementById("auth-modal-repeat");
    confirmPasswordField.classList.toggle("hidden");
    confirmPasswordField.required = !confirmPasswordField.required;

    let actionTxts = {
        login: "Login",
        reg: "Create account",
        changeToLogin: "Already have an accoun? Login!",
        changeToReg: "No account? Create new!"
    };

    if (authForm.getAttribute("action") == "account/register/") {
        // Change to login form
        authForm.setAttribute("action", "account/login/");

        authArticle.innerText = actionTxts.login;
        authLink.innerText = actionTxts.changeToReg;
    } else { 
        // Change to register form
        authForm.setAttribute("action", "account/register/");

        authArticle.innerText = actionTxts.reg;
        authLink.innerText = actionTxts.changeToLogin;
    }

};
// 

