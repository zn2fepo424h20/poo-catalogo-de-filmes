class Usuario:
    def __init__(self, id, nome, email, catalogo):
        self._id = id
        self._nome = nome
        self._email = email
        self._catalogo = catalogo
        self._historicoVisualizacao = []
        self._favoritos = []
        self._avaliacoes = {}
        self._senha = ""

    def assistirMidia(self, idMidia):
        midia = next(
            (
                item for item in self._catalogo.listarMidias()
                if item._id == idMidia
            ),
            None
        )

        if midia is None:
            print("Mídia não encontrada.")
            return

        if not midia.verificarDisponibilidade():
            print("Mídia indisponível.")
            return

        if hasattr(midia, "reproduzirEpisodio"):
            midia.reproduzirEpisodio()
        else:
            midia.Reproduzir()

        self._historicoVisualizacao.append(midia)

    def favoritarMidia(self, idMidia):
        midia = next(
            (
                item for item in self._catalogo.listarMidias()
                if item._id == idMidia
            ),
            None
        )

        if midia is None:
            print("Mídia não encontrada.")
        elif midia in self._favoritos:
            print("Essa mídia já está nos favoritos.")
        else:
            self._favoritos.append(midia)
            print(f"'{midia._titulo}' adicionado aos favoritos.")

    def avaliarMidia(self, idMidia, nota):
        midia = next(
            (
                item for item in self._catalogo.listarMidias()
                if item._id == idMidia
            ),
            None
        )

        if midia is None:
            print("Mídia não encontrada.")
            return

        if not isinstance(nota, (int, float)) or not 0 <= nota <= 10:
            print("A nota deve estar entre 0 e 10.")
            return

        self._avaliacoes[idMidia] = nota
        print(f"Nota {nota} registrada para '{midia._titulo}'.")

    def alterarSenha(self):
        novaSenha = input("Digite a nova senha: ")

        if len(novaSenha) < 6:
            print("A senha deve ter pelo menos 6 caracteres.")
            return

        self._senha = novaSenha
        print("Senha alterada com sucesso.")

    def obterRecomendacoes(self):
        if not self._historicoVisualizacao:
            return self._catalogo.listarMidias()

        generos = {}

        for midia in self._historicoVisualizacao:
            genero = midia._genero
            generos[genero] = generos.get(genero, 0) + 1

        generoPreferido = max(generos, key=generos.get)

        return [
            midia for midia in self._catalogo.listarMidias()
            if midia._genero.casefold() == generoPreferido.casefold()
            and midia not in self._historicoVisualizacao
        ]