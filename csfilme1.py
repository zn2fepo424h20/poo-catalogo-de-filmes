class Filme:
    def __init__(
        self, id, titulo, genero,
        duracaoMinutos, classificacaoIndicativa
    ):
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._duracaoMinutos = duracaoMinutos
        self._classificacaoIndicativa = classificacaoIndicativa
        self._visualizacoes = 0
        self._disponivel = True

    def Reproduzir(self):
        if self.verificarDisponibilidade():
            self._visualizacoes += 1
            print(f"Reproduzindo o filme: {self._titulo}")
        else:
            print("Filme indisponível.")

    def Pausar(self):
        print(f"Filme '{self._titulo}' pausado.")

    def obterDetalhes(self):
        return (
            f"ID: {self._id}\n"
            f"Título: {self._titulo}\n"
            f"Gênero: {self._genero}\n"
            f"Duração: {self._duracaoMinutos} minutos\n"
            f"Classificação indicativa: "
            f"{self._classificacaoIndicativa}"
        )

    def calcularIdadeMinima(self):
        classificacao = self._classificacaoIndicativa.lower()

        if "livre" in classificacao:
            return 0

        numeros = "".join(
            caractere for caractere in classificacao
            if caractere.isdigit()
        )

        return int(numeros) if numeros else 0

    def verificarDisponibilidade(self):
        return self._disponivel

