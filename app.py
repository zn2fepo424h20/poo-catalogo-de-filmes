from classeprincipalcatalogo import Catalogo
from csusuario2 import Usuario
from csfilme1 import Filme
from csserie1 import Serie


# ==========================================
# CRIANDO O CATÁLOGO
# ==========================================

catalogo = Catalogo()


# ==========================================
# CRIANDO FILMES
# ==========================================

filme1 = Filme(
    1, "Dabbe", "Terror", 233, "16 anos"
)

filme2 = Filme(
    2, "Rapunzel", "Animação", 100, "Livre"
)


# ==========================================
# CRIANDO SÉRIES
# ==========================================

serie1 = Serie(
    3, "Breaking Bad", "Drama", 5, 13, "18 anos"
)


# ==========================================
# ADICIONANDO MÍDIAS AO CATÁLOGO
# ==========================================

catalogo.adicionarMidia(filme1)
catalogo.adicionarMidia(filme2)
catalogo.adicionarMidia(serie1)


# ==========================================
# CRIANDO USUÁRIO
# ==========================================

usuario = Usuario(
    1,
    "Aninha",
    "aninha@email.com",
    catalogo
)


# ==========================================
# MOSTRAR CATÁLOGO
# ==========================================

def mostrarCatalogo():
    print("\n===== CATÁLOGO COMPLETO =====")

    midias = catalogo.listarMidias()

    if not midias:
        print("Nenhuma mídia cadastrada.")
        return

    for midia in midias:
        print(midia.obterDetalhes())
        print("-" * 40)


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n" + "=" * 40)
    print("       CATÁLOGO DE FILMES E SÉRIES")
    print("=" * 40)

    print("1 - Listar catálogo")
    print("2 - Assistir mídia")
    print("3 - Favoritar mídia")
    print("4 - Avaliar mídia")
    print("5 - Alterar senha")
    print("6 - Ver recomendações")
    print("7 - Buscar por título")
    print("8 - Filtrar por gênero")
    print("9 - Listar mais vistos")
    print("10 - Informações da série")
    print("11 - Classificação indicativa")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")


    # ======================================
    # LISTAR CATÁLOGO
    # ======================================

    if opcao == "1":
        mostrarCatalogo()


    # ======================================
    # ASSISTIR MÍDIA
    # ======================================

    elif opcao == "2":
        mostrarCatalogo()

        try:
            idMidia = int(input("Digite o ID da mídia: "))
            usuario.assistirMidia(idMidia)
        except ValueError:
            print("Digite um ID numérico válido.")


    # ======================================
    # FAVORITAR MÍDIA
    # ======================================

    elif opcao == "3":
        mostrarCatalogo()

        try:
            idMidia = int(input("Digite o ID da mídia: "))
            usuario.favoritarMidia(idMidia)
        except ValueError:
            print("Digite um ID numérico válido.")


    # ======================================
    # AVALIAR MÍDIA
    # ======================================

    elif opcao == "4":
        mostrarCatalogo()

        try:
            idMidia = int(input("Digite o ID da mídia: "))
            nota = float(input("Digite uma nota de 0 a 10: "))
            usuario.avaliarMidia(idMidia, nota)
        except ValueError:
            print("Digite valores numéricos válidos.")


    # ======================================
    # ALTERAR SENHA
    # ======================================

    elif opcao == "5":
        usuario.alterarSenha()


    # ======================================
    # RECOMENDAÇÕES
    # ======================================

    elif opcao == "6":
        print("\n===== RECOMENDAÇÕES =====")

        recomendacoes = usuario.obterRecomendacoes()

        if recomendacoes:
            for midia in recomendacoes:
                print(midia.obterDetalhes())
                print("-" * 40)
        else:
            print("Nenhuma recomendação disponível.")


    # ======================================
    # BUSCAR POR TÍTULO
    # ======================================

    elif opcao == "7":
        titulo = input("Digite o título que deseja buscar: ")

        resultados = catalogo.buscarPorTitulo(titulo)

        if resultados:
            for midia in resultados:
                print(midia.obterDetalhes())
        else:
            print("Nenhuma mídia encontrada.")


    # ======================================
    # FILTRAR POR GÊNERO
    # ======================================

    elif opcao == "8":
        genero = input("Digite o gênero desejado: ")

        resultados = catalogo.filtrarPorGenero(genero)

        if resultados:
            for midia in resultados:
                print(midia.obterDetalhes())
        else:
            print("Nenhuma mídia encontrada para esse gênero.")


    # ======================================
    # MAIS VISTOS
    # ======================================

    elif opcao == "9":
        print("\n===== MÍDIAS MAIS VISTAS =====")

        maisVistos = catalogo.listarMaisVistos()

        if maisVistos:
            for midia in maisVistos:
                print(
                    f"{midia._titulo}: "
                    f"{midia._visualizacoes} visualização(ões)"
                )
        else:
            print("Nenhuma mídia cadastrada.")


    # ======================================
    # INFORMAÇÕES DA SÉRIE
    # ======================================

    elif opcao == "10":
        print("\n===== INFORMAÇÕES DA SÉRIE =====")

        serie1.reproduzirEpisodio()
        serie1.avancarProximoEpisodio()

        print(serie1.obterResumoTemporada())

        print(
            "Episódios restantes:",
            serie1.calcularTempoRestante()
        )


    # ======================================
    # CLASSIFICAÇÃO INDICATIVA
    # ======================================

    elif opcao == "11":
        print("\n===== CLASSIFICAÇÃO INDICATIVA =====")

        print(
            filme1._titulo,
            "- idade mínima:",
            filme1.calcularIdadeMinima()
        )


    # ======================================
    # SAIR
    # ======================================

    elif opcao == "0":
        print("Encerrando o catálogo. Até logo!")
        break


    else:
        print("Opção inválida. Tente novamente.")
