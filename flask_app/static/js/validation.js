function getCibilStatus(score){

    score = Number(score);

    if(score >= 750){

        return{
            text:"Excellent",
            color:"green"
        };

    }

    if(score >= 650){

        return{
            text:"Good",
            color:"blue"
        };

    }

    if(score >= 550){

        return{
            text:"Average",
            color:"orange"
        };

    }

    return{

        text:"Poor",
        color:"red"

    };

}

function initializeValidation(){

    const cibilInput =
        document.getElementById("cibil_score");

    if(cibilInput){

        cibilInput.addEventListener(
            "input",
            updateCibilUI
        );

    }

}