// Company Form Color Picker JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Función para inicializar los color pickers
    function initializeColorPickers() {
        const colorInputs = document.querySelectorAll('.color-picker');
        
        colorInputs.forEach(function(input) {
            // Agregar evento de cambio para actualizar preview en tiempo real
            input.addEventListener('input', function() {
                updateColorPreview(this);
                updateLivePreview();
            });
            
            // Crear un preview visual
            createColorPreview(input);
        });
        
        // Crear preview en tiempo real si no existe
        createLivePreview();
    }
    
    // Función para crear preview visual junto al input
    function createColorPreview(input) {
        const container = input.parentElement;
        
        // Verificar si ya existe un preview
        if (container.querySelector('.color-preview')) {
            return;
        }
        
        const preview = document.createElement('span');
        preview.className = 'color-preview';
        preview.style.backgroundColor = input.value || '#ffffff';
        preview.title = 'Vista previa del color';
        
        container.appendChild(preview);
    }
    
    // Función para actualizar el preview visual
    function updateColorPreview(input) {
        const preview = input.parentElement.querySelector('.color-preview');
        if (preview) {
            preview.style.backgroundColor = input.value;
        }
    }
    
    // Función para crear preview en tiempo real de los cambios
    function createLivePreview() {
        const form = document.querySelector('form');
        if (!form || document.querySelector('.color-preview-demo')) {
            return;
        }
        
        const previewContainer = document.createElement('div');
        previewContainer.className = 'color-preview-demo';
        previewContainer.innerHTML = `
            <h6><i class="fas fa-eye"></i> Vista previa de colores</h6>
            <div class="preview-main">
                <strong>Color principal</strong> - Usado en la barra lateral y header
            </div>
            <div class="preview-content">
                <span class="preview-font">Color de fuente</span> - Usado para el texto en navegación
            </div>
            <div style="padding: 10px; border: 1px solid #ddd; border-radius: 3px;">
                <span class="preview-font">Área de contenido</span> - Fondo del área de trabajo
            </div>
        `;
        
        // Insertar antes del primer campo de color
        const firstColorField = document.querySelector('.field-main_color, [name="main_color"]')?.closest('.form-group, .field, .form-row');
        if (firstColorField) {
            firstColorField.parentNode.insertBefore(previewContainer, firstColorField);
        }
        
        // Actualizar preview inicial
        updateLivePreview();
    }
    
    // Función para actualizar preview en tiempo real
    function updateLivePreview() {
        const mainColorInput = document.querySelector('[name="main_color"]');
        const contentColorInput = document.querySelector('[name="content_wrapper_color"]');
        const fontColorInput = document.querySelector('[name="font_color"]');
        
        const previewMain = document.querySelector('.preview-main');
        const previewContent = document.querySelector('.preview-content');
        const previewFonts = document.querySelectorAll('.preview-font');
        
        if (previewMain && mainColorInput) {
            previewMain.style.backgroundColor = mainColorInput.value || '#563D7C';
        }
        
        if (previewContent && contentColorInput) {
            previewContent.style.backgroundColor = contentColorInput.value || '#f4f6f9';
            previewContent.parentElement.style.backgroundColor = contentColorInput.value || '#f4f6f9';
        }
        
        if (previewFonts && fontColorInput) {
            previewFonts.forEach(function(element) {
                element.style.color = fontColorInput.value || '#cbbde2';
            });
        }
    }
    
    // Función para agregar tooltips informativos
    function addTooltips() {
        const tooltipData = {
            'main_color': 'Color principal usado en la barra lateral, header y elementos de navegación',
            'content_wrapper_color': 'Color de fondo del área principal de contenido',
            'font_color': 'Color del texto en la navegación y elementos principales'
        };
        
        Object.keys(tooltipData).forEach(function(fieldName) {
            const input = document.querySelector(`[name="${fieldName}"]`);
            if (input && !input.getAttribute('title')) {
                input.setAttribute('title', tooltipData[fieldName]);
                input.setAttribute('data-toggle', 'tooltip');
                input.setAttribute('data-placement', 'top');
            }
        });
        
        // Inicializar tooltips de Bootstrap si está disponible
        if (typeof $ !== 'undefined' && $.fn.tooltip) {
            $('[data-toggle="tooltip"]').tooltip();
        }
    }
    
    // Función para validar colores hexadecimales
    function validateHexColor(color) {
        return /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/.test(color);
    }
    
    // Función para convertir color a hexadecimal si es necesario
    function ensureHexColor(input) {
        let value = input.value;
        if (value && !value.startsWith('#')) {
            value = '#' + value;
            input.value = value;
        }
        return value;
    }
    
    // Agregar validación en tiempo real
    function addValidation() {
        const colorInputs = document.querySelectorAll('.color-picker');
        
        colorInputs.forEach(function(input) {
            input.addEventListener('blur', function() {
                const color = ensureHexColor(this);
                if (color && !validateHexColor(color)) {
                    alert('Por favor, introduce un color válido en formato hexadecimal (ej: #FF0000)');
                    this.focus();
                }
            });
        });
    }
    
    // Inicializar todo
    try {
        initializeColorPickers();
        addTooltips();
        addValidation();
        
        console.log('Color pickers inicializados correctamente');
    } catch (error) {
        console.error('Error al inicializar color pickers:', error);
    }
});

// Función global para restablecer colores por defecto
function resetColorsToDefault() {
    const defaults = {
        'main_color': '#563D7C',
        'content_wrapper_color': '#f4f6f9',
        'font_color': '#cbbde2'
    };
    
    Object.keys(defaults).forEach(function(fieldName) {
        const input = document.querySelector(`[name="${fieldName}"]`);
        if (input) {
            input.value = defaults[fieldName];
            input.dispatchEvent(new Event('input'));
        }
    });
}

// Función global para aplicar un tema predefinido
function applyColorTheme(themeName) {
    const themes = {
        'default': {
            'main_color': '#563D7C',
            'content_wrapper_color': '#f4f6f9',
            'font_color': '#cbbde2'
        },
        'blue': {
            'main_color': '#026AA7',
            'content_wrapper_color': '#f4f6f9',
            'font_color': '#CCE1ED'
        },
        'dark': {
            'main_color': '#01363D',
            'content_wrapper_color': '#f4f6f9',
            'font_color': '#30AABC'
        },
        'green': {
            'main_color': '#28a745',
            'content_wrapper_color': '#f8f9fa',
            'font_color': '#b8e6c1'
        },
        'red': {
            'main_color': '#dc3545',
            'content_wrapper_color': '#f8f9fa',
            'font_color': '#f5c6cb'
        }
    };
    
    const theme = themes[themeName];
    if (theme) {
        Object.keys(theme).forEach(function(fieldName) {
            const input = document.querySelector(`[name="${fieldName}"]`);
            if (input) {
                input.value = theme[fieldName];
                input.dispatchEvent(new Event('input'));
            }
        });
    }
}