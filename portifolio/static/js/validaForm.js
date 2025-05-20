export default function validaForm() {
    const form = document.getElementById('contactForm')
    function handleChange(event) {
        const target = event.target

        if(!target.checkValidity()) {
            target.classList.add('invalido')
            target.nextElementSibling.innerText = target.validationMessage;
        } else {
            target.classList.remove("invalido")
            target.nextElementSibling.innerText = "";
        }
    }
    form.addEventListener('change', handleChange)
}