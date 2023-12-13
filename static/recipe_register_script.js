var suggestions = null;

function addIngredient(){
    const container = document.getElementById('ingredients');
    const index = container.children.length;

    const newIngredient = `
        <div class="ingredient input-group mb-3 grid-3">
                <input type="text" name="ingredients-${index}-ingredient_name" class="form-control ingredient-name" placeholder="Nome" required>
                <input type="text" name="ingredients-${index}-quantity" class="form-control quantity" placeholder="Quantidade" required>
                <button type="button" class="btn btn-remove btn-sm" onclick="removeIngredient(this)">
                    <span>-</span>
                </button>
        </div>
    `;

    container.insertAdjacentHTML('beforeend', newIngredient);

    $(`[name="ingredients-${index}-ingredient_name"]`).autocomplete({
        source: suggestions,
        minLength: 2
    })
}

function removeIngredient(button) {
    const ingredient = button.closest('.ingredient');
    ingredient.parentNode.removeChild(ingredient);
}

$(document).ready(function() {
    $.ajax({
        url: '/ingredients',
        dataType: 'json'
    }).done(function(data){
        suggestions = data.suggestions;
    })
})