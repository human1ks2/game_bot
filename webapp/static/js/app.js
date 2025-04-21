function startAnimation() {
    const button = document.getElementById("start-button");
    const coefficient = document.getElementById("coefficient");

    if (button.disabled) return;

    button.disabled = true;
    button.style.backgroundColor = "#6b7280"; // Серая
    coefficient.textContent = "0.0x";

    let current = 0.0;
    const target = (Math.random() * (10 - 1.2) + 1.2).toFixed(2);

    const interval = setInterval(() => {
        current += 0.1;

        if (current >= target) {
            current = parseFloat(target);
            clearInterval(interval);
            button.disabled = false;
            button.style.backgroundColor = "#e63946"; // Снова красная
        }

        coefficient.textContent = current.toFixed(2) + "x";
    }, 50);
}
