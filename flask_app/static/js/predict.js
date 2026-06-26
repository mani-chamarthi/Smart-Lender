const income =
    document.getElementById("income_annum");

if(income){
    income.addEventListener(
        "input",
        updateIncomeUI
    );
}


const loan =
    document.getElementById("loan_amount");

if(loan){
    loan.addEventListener(
        "input",
        updateLoanUI
    );
}


const term =
    document.getElementById("loan_term");

if(term){
    term.addEventListener(
        "input",
        updateLoanTermUI
    );
}