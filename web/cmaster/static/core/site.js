document.addEventListener("DOMContentLoaded", () => {
    // Particles
    const particlesContainer = document.getElementById("hero-particles");
    if (particlesContainer) {
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement("div");
            particle.className = "particle";
            particle.style.left = Math.random() * 100 + "%";
            particle.style.animationDuration = (Math.random() * 10 + 10) + "s";
            particle.style.animationDelay = Math.random() * 10 + "s";
            particle.style.width = (Math.random() * 4 + 2) + "px";
            particle.style.height = particle.style.width;
            particlesContainer.appendChild(particle);
        }
    }

    // Calculator
    const categorySelect = document.querySelector("#calculator-category");
    const total = document.querySelector("#calculator-total");
    const options = Array.from(document.querySelectorAll(".option-row"));
    const formatPrice = new Intl.NumberFormat("ru-RU", {
        maximumFractionDigits: 0,
    });

    const updateCalculator = () => {
        if (!categorySelect || !total) return;
        const selected = categorySelect.selectedOptions[0];
        if (!selected || !selected.dataset.price) {
            total.textContent = "Уточняйте";
            return;
        }

        const categoryId = categorySelect.value;
        let price = Number(selected.dataset.price);
        options.forEach((row) => {
            const visible = row.dataset.category === categoryId;
            row.hidden = !visible;
            const checkbox = row.querySelector("input");
            if (!visible) checkbox.checked = false;
            if (visible && checkbox.checked) price += Number(checkbox.dataset.price);
        });
        total.textContent = `${formatPrice.format(price)} ₽`;
    };

    categorySelect?.addEventListener("change", updateCalculator);
    options.forEach((row) => {
        row.querySelector("input")?.addEventListener("change", updateCalculator);
    });
    updateCalculator();

    // Pickup address
    const pickup = document.querySelector("#id_is_pickup");
    const addressField = document.querySelector(".address-field");
    const addressInput = document.querySelector("#id_address");
    const updateAddress = () => {
        if (!pickup || !addressField) return;
        addressField.hidden = !pickup.checked;
        if (addressInput) addressInput.required = pickup.checked;
    };
    pickup?.addEventListener("change", updateAddress);
    updateAddress();
});
