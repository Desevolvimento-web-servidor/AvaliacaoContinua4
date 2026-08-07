function iniciarContador(isoDate) {
    const dataModificacao = new Date(isoDate);

    function atualizarContador() {
        const agora = new Date();
        const minPassados = Math.floor((agora - dataModificacao) / (1000 * 60));

        let texto = "";
        if (minPassados < 1) {
            texto = "That was 0 minutes ago.";
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

    atualizarContador();
    setInterval(atualizarContador, 30000);
}