const API_URL = "http://localhost:8030/livros";

const listaLivros = document.getElementById("livrosList");

const formLivro = document.getElementById("formLivro");

async function carregarLivros() {
    const response = await fetch(API_URL);
    const livros = await response.json();
    listaLivros.innerHTML = "";

    livros.forEach((livro) => {
        listaLivros.innerHTML += `
            <div class="livro">
                <div>
                    <strong>Título:</strong> ${livro.titulo}<br>
                    <strong>Autor:</strong> ${livro.autor}<br>
                    <strong>Ano de Publicação:</strong> ${livro.ano_publicacao}
                </div>
                <div class="acoes">
                    <button onclick="removerLivro(${livro.id})">Remover</button>
                </div>
            </div>
        `;
    });

}
async function removerLivro(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE",
    });
    carregarLivros();
}



formLivro.addEventListener("submit", async(event) => {
    event.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;
    const ano_publicacao = Number(document.getElementById("ano_publicacao").value);

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
            titulo, 
            autor, 
            ano_publicacao
        })
    });
    formLivro.reset();

    carregarLivros();
}
);

carregarLivros();