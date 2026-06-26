function calculateTotalAssets(){

    let residential =
        Number(document.getElementById("residential_assets_value").value) || 0;

    let commercial =
        Number(document.getElementById("commercial_assets_value").value) || 0;

    let luxury =
        Number(document.getElementById("luxury_assets_value").value) || 0;

    let bank =
        Number(document.getElementById("bank_asset_value").value) || 0;

    return residential +
           commercial +
           luxury +
           bank;
}


function initializeCalculator(){

    const ids = [
        "residential_assets_value",
        "commercial_assets_value",
        "luxury_assets_value",
        "bank_asset_value"
    ];

    ids.forEach(id => {

        const element =
            document.getElementById(id);

        if(element){

            element.addEventListener(
                "input",
                updateAssetUI
            );

        }

    });

}