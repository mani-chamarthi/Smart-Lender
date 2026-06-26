//Format Indian Currency

function formatIndianCurrency(value){

    if(value === "" || isNaN(value))
        return "";

    value = Number(value);

    if(value >= 10000000){

        return "₹" + (value/10000000).toFixed(2) + " Crores";

    }

    if(value >= 100000){

        return "₹" + (value/100000).toFixed(2) + " Lakhs";

    }

    if(value >= 1000){

        return "₹" + (value/1000).toFixed(2) + " Thousand";

    }

    return "₹" + value;

}

//Loan Term
function convertLoanTerm(months){

    if(months === "" || isNaN(months))
        return "";

    let years = months / 12;

    return years + " Years";

}