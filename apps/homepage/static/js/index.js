const form   = document.querySelector('#form');
const inputs = document.querySelectorAll('#form input');


const e = user;

const expresions = {
    reguser: /^[a-zA-Z0-9\_\-]{4,16}$/,
    regpass: /^.{4,12}$/,
}

const fields = {
    user: false,
    pass: false,
}

//`expresions.reg${e.target.name}`
const validateForm = (e) => {
    if ( e.target.name == 'user') {
        validateField( expresions.reguser, e.target, e.target.name );
    } else {
        validateField( expresions.regpass, e.target, e.target.name );
    }
}

const validateField = ( expresions, input, camp ) => {
    if ( expresions.test( input.value )) {
        document.querySelector(`#group_${camp}`).classList.remove('form_group_incorrect');
        document.querySelector(`#group_${camp}`).classList.add('form_group_correct');
        document.querySelector(`#group_${camp} .form_input_error`).classList.remove('form_input_error_active');
        document.querySelector('#form_message').classList.remove('form_message_active');
        fields[camp] = true;
    } else {
        document.querySelector(`#group_${camp}`).classList.add('form_group_incorrect');
        document.querySelector(`#group_${camp}`).classList.remove('form_group_correct');
        document.querySelector(`#group_${camp} .form_input_error`).classList.add('form_input_error_active');
        fields[camp] = false;
    }
}

inputs.forEach( ( input ) => {
    input.addEventListener('keyup', validateForm);
    input.addEventListener('blur', validateForm);
});

form.addEventListener('submit', (e) => {


    if ( fields.user && fields.pass ) {
        form.reset()
        document.querySelector('#form_message_succes').classList.add('form_message_succes_active')
        setTimeout( () => {
            document.querySelector('#form_message_succes').classList.remove('form_message_succes_active')
        }, 5000); 

        document.querySelectorAll('.form_group_correct').forEach(( icon ) => {
            icon.classList.remove('form_group_correct');
        });
    } else {
        document.querySelector('#form_message').classList.add('form_message_active');
    }
});