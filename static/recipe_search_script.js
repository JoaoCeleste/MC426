window.onload = function(e){ 
    var input = document.querySelector('input'),
        tagify = new Tagify(input, {whitelist:[], enforceWhitelist: true}),
        controller; // for aborting the call

    tagify.on('input', onInput);

    function onInput(e){
        let value = e.detail.value
        controller && controller.abort()
        controller = new AbortController()
    
        tagify.loading(false).dropdown.show(value)
    }
    
    fetch('/ingredients')
    .then(RES => RES.json())
    .then(function(newWhitelist){
        console.log(newWhitelist)
        tagify.whitelist = newWhitelist.suggestions // update whitelist Array in-place
        tagify.addTags(["Alho"])
    })

    let ingredientForm = document.getElementById('ingredients-form');
    ingredientForm.onsubmit = function(e){
        let input = document.getElementById('ingredients-form-ingredients');
        value = tagify.value.map(item => item.value)

        const container = document.getElementById('ingredients-search-bar');
        for(let i = 0; i < value.length; i++){
            let field = `<input type="text" name="ingredients-${i}" placeholder="Nome" style="display:none;">`
            container.insertAdjacentHTML('beforeend', field);
            document.querySelector(`input[name="ingredients-${i}"]`).value = value[i]
        }
    }
}
