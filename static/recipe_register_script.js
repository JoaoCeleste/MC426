var suggestions = null;

function addIngredient(){
    const container = document.getElementById('ingredients');
    const index = container.children.length;

    const newIngredient = `
        <div class="ingredient input-group mb-3 row">
            <div class="col">
                <input type="text" name="${index}-ingredient_name" class="form-control ingredient-name" placeholder="Nome" required>
            </div>
            <div class="col">
                <input type="text" name="${index}-quantity" class="form-control" placeholder="Quantidade" required>
            </div>
            <div class="col align-self-center">
                <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeIngredient(this)">-</button>
            </div>
        </div>
    `;

    container.insertAdjacentHTML('beforeend', newIngredient);

    $(`[name="${index}-ingredient_name"]`).autocomplete({
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