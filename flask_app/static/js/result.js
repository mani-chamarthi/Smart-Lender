document.addEventListener("DOMContentLoaded", () => {

    const bar = document.getElementById("confidence-bar");

    if(!bar) return;

    const confidence = Number(bar.dataset.confidence);

    bar.style.width = confidence + "%";

});