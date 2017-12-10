// -----------------------------------------------------------------------------
// subscription form

function subText() {

    var sub_selected = document.getElementById('id_select_sub');
    
    var sub_para = document.getElementById('sub_selection_para');
    var sub_button = document.getElementById('sub_selection_button');
    
    var selected_value = sub_selected.value;
    var selected_text = sub_selected.options[sub_selected.selectedIndex].text;
    
    var sub_form = document.forms['subscription_form'];
 
    if (selected_value != '') {
        console.log(sub_form.elements['name'].value)
        sub_form.elements['name'].value = 'Month';
        console.log(sub_form.elements['name'].value)
        
        sub_para.innerHTML = selected_text
        sub_para.style.display = 'block';
        // sub_button.style.display = 'block';
    }else{
        sub_para.style.display = 'none';
        // sub_button.style.display = 'none';
    }
}

function showCheckout(){
    var select = document.getElementById('select');
    var checkout = document.getElementById('checkout');
    select.style.display = 'none';
    checkout.style.display = 'block';
}

// -----------------------------------------------------------------------------

