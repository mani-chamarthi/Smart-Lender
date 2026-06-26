//Update CIBIL message
function updateCibilUI(){

    let score =
        document.getElementById("cibil_score").value;

    let status =
        getCibilStatus(score);

    let output =
        document.getElementById("cibil-status");

    output.innerHTML = status.text;

    output.style.color = status.color;

}

//Update Total Assets
function updateAssetUI(){

    let total =
        calculateTotalAssets();

    document.getElementById("total-assets").innerHTML =
        formatIndianCurrency(total);

}

//confidence bar
function initializeConfidenceBar(){

    const bar = document.getElementById("confidence-bar");

    if(!bar) return;

    const confidence = Number(bar.dataset.confidence);

    bar.style.width = confidence + "%";

}

//update Income
function updateIncomeUI(){

    let value =
        document.getElementById(
            "income_annum"
        ).value;

    document.getElementById(
        "income-display"
    ).innerHTML =
        formatIndianCurrency(value);

}

//update loan
function updateLoanUI(){

    let value =
        document.getElementById(
            "loan_amount"
        ).value;

    document.getElementById(
        "loan-display"
    ).innerHTML =
        formatIndianCurrency(value);

}

//update loan term
function updateLoanTermUI(){

    let value =
        document.getElementById(
            "loan_term"
        ).value;

    document.getElementById(
        "loan-term-display"
    ).innerHTML =
        convertLoanTerm(value);

}