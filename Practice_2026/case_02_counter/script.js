const result = document.getElementById("result");
const plusButton = document.getElementById("plusButton");
const minusButton = document.getElementById("minusButton");
const message = document.getElementById("message");

let counterValue = 0;

function updateInterface() {
    result.textContent = counterValue;
    result.classList.remove("positive", "negative", "zero");

    if (counterValue > 0) {
        result.classList.add("positive");
    } else if (counterValue < 0) {
        result.classList.add("negative");
    } else {
        result.classList.add("zero");
    }

    plusButton.disabled = counterValue === 10;
    minusButton.disabled = counterValue === -10;

    if (counterValue === 10 || counterValue === -10) {
        message.textContent = "Вы достигли экстремального значения";
    } else {
        message.textContent = "";
    }
}

plusButton.addEventListener("click", () => {
    if (counterValue < 10) {
        counterValue += 1;
        updateInterface();
    }
});

minusButton.addEventListener("click", () => {
    if (counterValue > -10) {
        counterValue -= 1;
        updateInterface();
    }
});

updateInterface();
