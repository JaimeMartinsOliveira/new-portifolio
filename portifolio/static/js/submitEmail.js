export default function submitEmail() {
    const formElement = document.getElementById('contactForm');

    const handleFormSubmit = (event) => {
        event.preventDefault(); 

        const data = new FormData(formElement);

        fetch(formElement.action, {
            method: formElement.method,
            body: data,
            headers: {
                'Accept': 'application/json'
            },
        }).then(response => {
            if (response.ok) {
                
                formElement.reset(); 
                alert("Formulário enviado com sucesso!");
            } else {
                response.json().then(data => {
                    if (data.errors) {
                        alert(data.errors.map(e => e.message).join(", "));
                    } else {
                        alert("Oops! Não foi possível enviar o formulário.");
                    }
                });
            }
        }).catch(error => {
            alert("Erro ao enviar o formulário: " + error);
        });
    };

    formElement.addEventListener('submit', handleFormSubmit);
}