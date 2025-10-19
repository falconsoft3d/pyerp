// Test para verificar que los widgets de color funcionan
console.log('Color widgets test loaded');

document.addEventListener('DOMContentLoaded', function() {
    console.log('Color widgets test DOM ready');
    
    // Agregar clase de test a los inputs de color
    const colorInputs = document.querySelectorAll('input[type="color"]');
    colorInputs.forEach(function(input) {
        input.classList.add('test-color-widget');
        console.log('Added test class to color input:', input.name);
    });
});