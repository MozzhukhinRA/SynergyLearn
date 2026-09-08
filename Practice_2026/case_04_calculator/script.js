const firstNumberInput = document.getElementById("firstNumber");
const secondNumberInput = document.getElementById("secondNumber");
const result = document.getElementById("result");
const buttons = document.querySelectorAll("[data-operation]");

function sum(a, b) { return a + b; }
function difference(a, b) { return a - b; }
function product(a, b) { return a * b; }

function division(a, b) {
    if (b === 0) {
        throw new Error("Деление на ноль невозможно.");
    }
    return a / b;
}

function prepareNumber(value) {
    return value.trim().replace(",", ".");
}

function readNumbers() {
    const firstValue = prepareNumber(firstNumberInput.value);
    const secondValue = prepareNumber(secondNumberInput.value);

    if (firstValue === "" || secondValue === "") {
        throw new Error("Введите два числа.");
    }

    const firstNumber = Number(firstValue);
    const secondNumber = Number(secondValue);

    if (!Number.isFinite(firstNumber) || !Number.isFinite(secondNumber)) {
        throw new Error("Ошибка: в поля необходимо вводить цифры.");
    }

    return [firstNumber, secondNumber];
}

function showResult(value) {
    result.classList.remove("error");
    result.textContent = `Результат: ${value}`;
}

function showError(message) {
    result.classList.add("error");
    result.textContent = message;
}

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        try {
            const [firstNumber, secondNumber] = readNumbers();
            const operation = button.dataset.operation;
            let answer;

            if (operation === "sum") answer = sum(firstNumber, secondNumber);
            else if (operation === "difference") answer = difference(firstNumber, secondNumber);
            else if (operation === "product") answer = product(firstNumber, secondNumber);
            else if (operation === "division") answer = division(firstNumber, secondNumber);

            showResult(answer);
        } catch (error) {
            showError(error.message);
        }
    });
});
