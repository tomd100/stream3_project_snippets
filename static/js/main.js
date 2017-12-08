// -----------------------------------------------------------------------------
// subscription form

function subText() {
    var sub_selected = document.getElementById('id_sub_type');
    var sub_para = document.getElementById('sub_selection_para');
    var sub_button = document.getElementById('sub_selection_button');
    
    var selected_value = sub_selected.value
    var selected_text = sub_selected.options[sub_selected.selectedIndex].text;
    
    sub_para.innerHTML = selected_text
    
    if (selected_value > 0){
        sub_para.style.display = 'block'
        sub_button.style.display = 'block'
    }else{
        sub_para.style.display = 'none'
        sub_button.style.display = 'none'
    }
}

function showCheckout(){
    var select = document.getElementById('select');
    var checkout = document.getElementById('checkout');
    select.style.display = 'none'
    checkout.style.display = 'block'
}

// -----------------------------------------------------------------------------

