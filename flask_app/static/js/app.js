document.addEventListener("DOMContentLoaded", () => {

    if(typeof initializeValidation === "function"){
        initializeValidation();
    }

    if(typeof initializeCalculator === "function"){
        initializeCalculator();
    }

    if(typeof initializeConfidenceBar === "function"){
        initializeConfidenceBar();
    }

});