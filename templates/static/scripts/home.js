function iniciarContador(isoDate) {
    console.log("Data recebida do Flask:", isoDate);
    
    // Converte a data ISO para milissegundos
    const tempoCarregamento = new Date(isoDate).getTime();

    function atualizarContador() {
        const agora = new Date().getTime();
        
        // Diferença em segundos e minutos
        const diffEmSegundos = Math.floor((agora - tempoCarregamento) / 1000);
        const minPassados = Math.floor(diffEmSegundos / 60);

        console.log("Segundos passados:", diffEmSegundos);

        let texto = "";
        
        if (minPassados < 1) {
            texto = "That was a few seconds ago.";
        } else if (minPassados === 1) {
            texto = "That was 1 minute ago.";
        } else {
            texto = `That was ${minPassados} minutes ago.`;
        }

        const elemento = document.getElementById("contador-tempo");
        if (elemento) {
            elemento.innerText = texto;
        }
    }

    // Executa imediatamente na primeira vez
    atualizarContador();
    
    // Atualiza a cada 3 segundos
    setInterval(atualizarContador, 3000);
}