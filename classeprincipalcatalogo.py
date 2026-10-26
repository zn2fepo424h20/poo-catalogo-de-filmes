class Catalogo:
    def __init__(self):
        self._listaMidias = []
        self._totalItens = 0

    def adicionarMidia(self, midia):
        for item in self._listaMidias:
            if item._id == midia._id:
                print("Já existe uma mídia com esse ID.")
                return

        self._listaMidias.append(midia)
        self._totalItens = len(self._listaMidias)

        print(f"'{midia._titulo}' adicionado ao catálogo.")

    def removerMidia(self, id):
        for midia in self._listaMidias:
            if midia._id == id:
                self._listaMidias.remove(midia)
                self._totalItens = len(self._listaMidias)

                print(f"'{midia._titulo}' removido do catálogo.")
                return

        print("Mídia não encontrada.")

    def buscarPorTitulo(self, titulo):
        termo = titulo.casefold()

        return [
            midia for midia in self._listaMidias
            if termo in midia._titulo.casefold()
        ]

    def filtrarPorGenero(self, genero):
        termo = genero.casefold()

        return [
            midia for midia in self._listaMidias
            if midia._genero.casefold() == termo
        ]

    def listarMaisVistos(self):
        return sorted(
            self._listaMidias,
            key=lambda midia: midia._visualizacoes,
            reverse=True
        )

    def listarMidias(self):
        return self._listaMidias.copy()

