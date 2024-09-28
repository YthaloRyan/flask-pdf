async function handleSubmit(event) {
    console.log('entrei aqui');
    event.preventDefault();  // Evita o reload da página
    
    finalizarNumeros();

    // Coletando os dados do formulário
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    // Enviando dados via fetch
    const response = await fetch('/submit_form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    // Manipulando a resposta
    const result = await response;
    //document.getElementById('result').innerText = `Response: ${result.message}`;
    const pdfUrl = '/static/nota.pdf';
    const iframe = document.getElementById('notaPdf');
    iframe.src = pdfUrl;
    
    
    setTimeout(() => {
        iframe.contentWindow.print(); // Chama a função de impressão do conteúdo do iframe
        
    }, 100);
  }