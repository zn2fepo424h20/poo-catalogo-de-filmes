class Serie:
    def __init__(
        self, id, titulo, genero,
        totalTemporadas, episodios,
        classificacaoIndicativa
    ):
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._totalTemporadas = totalTemporadas
        self._episodios = episodios
        self._classificacaoIndicativa = classificacaoIndicativa

        self._temporadaAtual = 1
        self._episodioAtual = 1
        self._visualizacoes = 0
        self._disponivel = True

    def reproduzirEpisodio(self):
        if not self._disponivel:
            print("Série indisponível.")
            return

        self._visualizacoes += 1

        print(
            f"Reproduzindo {self._titulo} - "
            f"Temporada {self._temporadaAtual}, "
            f"Episódio {self._episodioAtual}"
        )

    def avancarProximoEpisodio(self):
        if self._episodioAtual < self._episodios:
            self._episodioAtual += 1

        elif self._temporadaAtual < self._totalTemporadas:
            self._temporadaAtual += 1
            self._episodioAtual = 1

        else:
            print("Você chegou ao último episódio.")
            return

        print(
            f"Próximo episódio: T{self._temporadaAtual} "
            f"E{self._episodioAtual}"
        )

    def obterResumoTemporada(self):
        return (
            f"Série: {self._titulo}\n"
            f"Total de temporadas: {self._totalTemporadas}\n"
            f"Episódios por temporada: {self._episodios}\n"
            f"Temporada atual: {self._temporadaAtual}\n"
            f"Episódio atual: {self._episodioAtual}"
        )

    def calcularTempoRestante(self):
        total = self._totalTemporadas * self._episodios

        assistidos = (
            (self._temporadaAtual - 1) * self._episodios
            + self._episodioAtual - 1
        )

        return max(0, total - assistidos)

    def Atualizar(self):
        print(f"Série '{self._titulo}' atualizada.")

    def obterDetalhes(self):
        return (
            f"ID: {self._id}\n"
            f"Título: {self._titulo}\n"
            f"Gênero: {self._genero}\n"
            f"Total de temporadas: {self._totalTemporadas}\n"
            f"Episódios por temporada: {self._episodios}\n"
            f"Classificação indicativa: "
            f"{self._classificacaoIndicativa}"
        )

