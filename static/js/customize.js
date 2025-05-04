document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const shoeSelect = document.getElementById('id_shoe');
    const baseColorSelect = document.getElementById('id_base_color');
    const accentColorSelect = document.getElementById('id_accent_color');
    const patternSelect = document.getElementById('id_sole_pattern');
    const quantityInput = document.getElementById('id_quantity');
    const priceDisplay = document.getElementById('total-price');
    const basePrice = document.getElementById('base-price');
    const customizationPrice = document.getElementById('customization-price');
    const shoeImage = document.getElementById('shoe-preview');

    // Function to update price
    function updatePrice() {
        const shoeId = shoeSelect.value;
        const baseColorId = baseColorSelect.value;
        const accentColorId = accentColorSelect.value;
        const patternId = patternSelect.value;
        const quantity = quantityInput.value;

        if (!shoeId) {
            return;
        }

        // Make AJAX request to get price
        fetch(`/api/calculate-customization-price/?shoe_id=${shoeId}&base_color_id=${baseColorId}&accent_color_id=${accentColorId}&pattern_id=${patternId}&quantity=${quantity}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error(data.error);
                    return;
                }

                // Update price displays
                basePrice.textContent = `$${data.base_price.toFixed(2)}`;
                customizationPrice.textContent = `$${data.customization_price.toFixed(2)}`;
                priceDisplay.textContent = `$${data.total_price.toFixed(2)}`;
            })
            .catch(error => {
                console.error('Error calculating price:', error);
            });
    }

    // Function to update shoe image
    function updateShoeImage() {
        const shoeId = shoeSelect.value;

        if (!shoeId) {
            shoeImage.src = '/static/img/placeholder.png';
            return;
        }

        // In a real application, you would fetch the image URL from the server
        // For now, we'll just use a placeholder
        shoeImage.src = `/static/img/shoes/${shoeId}.jpg`;
    }

    // Add event listeners
    shoeSelect.addEventListener('change', function() {
        updatePrice();
        updateShoeImage();
    });

    baseColorSelect.addEventListener('change', updatePrice);
    accentColorSelect.addEventListener('change', updatePrice);
    patternSelect.addEventListener('change', updatePrice);
    quantityInput.addEventListener('change', updatePrice);

    // Initialize
    if (shoeSelect.value) {
        updatePrice();
        updateShoeImage();
    }
});