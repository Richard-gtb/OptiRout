# Importa a biblioteca Matplotlib para visualização de gráficos
import matplotlib.pyplot as plt

# Importa a biblioteca NetworkX para trabalhar com grafos
import networkx as nx

# Cria um grafo vazio
G = nx.Graph()


# Adiciona arestas ao grafo G com peso 1
G.add_edges_from(
    [
        (1, 2, {"weight": 1}),
        (2, 3, {"weight": 10}),
        (3, 4, {"weight": 4}),
        (4, 5, {"weight": 1}),
        (3, 6, {"weight": 5}),
        (3, 10, {"weight": 5}),
        (6, 7, {"weight": 6}),
        (7, 8, {"weight": 9}),
        (8, 9, {"weight": 9}),
        (9, 10, {"weight": 10}),
        (10, 11, {"weight": 9}),
        (11, 12, {"weight": 2}),
        (12, 13, {"weight": 5}),
        (13, 14, {"weight": 10}),
        (14, 15, {"weight": 1}),
        (15, 16, {"weight": 9}),
        (15, 17, {"weight": 5}),
        (15, 19, {"weight": 7}),
        (19, 18, {"weight": 9}),
        (17, 18, {"weight": 8}),
        (7, 20, {"weight": 6}),
        (20, 21, {"weight": 1}),
        (21, 9, {"weight": 8}),
        (21, 22, {"weight": 7}),
        (22, 23, {"weight": 7}),
        (23, 24, {"weight": 9}),
        (24, 25, {"weight": 8}),
        (25, 26, {"weight": 7}),
        (26, 27, {"weight": 7}),
        (26, 28, {"weight": 7}),
        (26, 32, {"weight": 9}),
        (28, 29, {"weight": 3}),
        (29, 30, {"weight": 2}),
        (30, 31, {"weight": 8}),
        (31, 32, {"weight": 10}),
        (32, 35, {"weight": 7}),
        (32, 33, {"weight": 8}),
        (33, 34, {"weight": 2}),
        (35, 36, {"weight": 2}),
        (35, 37, {"weight": 1}),
        (36, 37, {"weight": 4}),
        (36, 37, {"weight": 7}),
        (37, 38, {"weight": 8}),
        (37, 38, {"weight": 1}),
        (37, 43, {"weight": 9}),
        (43, 44, {"weight": 4}),
        (44, 45, {"weight": 10}),
        (45, 46, {"weight": 1}),
        (45, 47, {"weight": 10}),
        (47, 36, {"weight": 10}),
        (38, 42, {"weight": 2}),
        (38, 40, {"weight": 6}),
        (38, 39, {"weight": 9}),
        (40, 41, {"weight": 6}),
        (40, 39, {"weight": 3}),
        (39, 24, {"weight": 4}),
        (25, 48, {"weight": 9}),
        (48, 49, {"weight": 7}),
        (48, 50, {"weight": 4}),
        (50, 51, {"weight": 5}),
        (51, 24, {"weight": 9}),
        (51, 52, {"weight": 2}),
        (51, 55, {"weight": 5}),
        (52, 53, {"weight": 3}),
        (53, 54, {"weight": 5}),
        (54, 55, {"weight": 6}),
        (55, 56, {"weight": 7}),
        (55, 57, {"weight": 4}),
        (55, 58, {"weight": 5}),
        (58, 57, {"weight": 5}),
        (57, 56, {"weight": 8}),
    ]
)

# Define a posição (coordenadas x, y) de cada nó para visualização
pos = {
    1: (5.3, 11.4),
    2: (3.8, 10.5),
    3: (2.3, 8.4),
    4: (3.8, 6.5),
    5: (4.5, 5.7),
    6: (4.4, 9.5),
    7: (5.3, 7.7),
    8: (6.2, 6.8),
    9: (7, 5.7),
    10: (9.4, 3.4),
    11: (8, 3.3),
    12: (6.9, 2.2),
    13: (6.1, 2.8),
    14: (5.5, 2),
    15: (4.5, 2.7),
    16: (3.9, 1.7),
    17: (5.3, 3.7),
    18: (4.5, 4.7),
    19: (3.5, 3.7),
    20: (5.3, 9.1),
    21: (7.6, 6.7),
    22: (11.3, 2.4),
    23: (8.6, 6.8),
    24: (10.2, 8),
    25: (11.4, 9.2),
    26: (12.9, 10.2),
    27: (12.2, 11.1),
    28: (14, 9.7),
    29: (15, 9.8),
    30: (15, 8.6),
    31: (14.8, 7.7),
    32: (13, 9.1),
    33: (12.4, 8.1),
    34: (10.9, 7),
    35: (13.7, 7.3),
    36: (14.8, 6.5),
    37: (13, 5.3),
    38: (11.7, 5.5),
    39: (10, 6.4),
    40: (10.6, 4.5),
    41: (13, 2),
    42: (13.6, 2.6),
    43: (13.9, 3.8),
    44: (15, 2.1),
    45: (15.8, 2.4),
    46: (14.8, 4.5),
    47: (16.5, 3),
    48: (10.6, 9.8),
    49: (10.7, 10.8),
    50: (8, 9.1),
    51: (8, 7.6),
    52: (7, 8.2),
    53: (6.3, 9),
    54: (5.2, 10.2),
    55: (7, 9.4),
    56: (9.3, 10),
    57: (8.6, 11),
    58: (7, 11.5),
}

############################################################################################

# Loop principal para entrada de dados do usuário
while True:
    # Solicita ao usuário a quantidade de rotas para simular (1 a 3)
    numero_de_rotas = int(
        input("Quantas rotas você gostaria de simular?(digite um número de 1 a 3)")
    )
    # Caso o usuário selecione uma rota para simular
    if numero_de_rotas == 1:
        # Solicita ao usuário o nó de partida e o nó de destino
        no_inicial = int(input("Informe o ponto de partida: "))
        no_final = int(input("Informe o ponto de destino: "))
        # Calcula o caminho mínimo entre o nó inicial e o nó final
        caminho_minimo = nx.dijkstra_path(G, no_inicial, no_final, weight="weight")

        # Cria uma lista de arcos (arestas) no caminho mínimo
        arcos = [
            (caminho_minimo[i], caminho_minimo[i + 1])
            for i in range(len(caminho_minimo) - 1)
        ]

        # Adiciona cada arco também na direção oposta
        for i in range(0, len(arcos)):
            arcos.append((arcos[i][1], arcos[i][0]))

        # Inicializa listas para as cores dos nós e das arestas
        cor_dos_nos = []
        cor_dos_arcos = []

        # Define a cor das arestas dependendo se estão no caminho mínimo
        for arco in G.edges:
            if arco in arcos:
                cor_dos_arcos.append("green")
            else:
                cor_dos_arcos.append("lightgray")

        # Define a cor dos nós dependendo se estão no caminho mínimo
        for node in G.nodes:
            if node in caminho_minimo:
                cor_dos_nos.append("green")
            else:
                cor_dos_nos.append("white")

    ################################################################################################

    # Caso o usuário escolha simular duas rotas
    elif numero_de_rotas == 2:

        # Solicita entrada dos pontos de partida e destino para duas rotas
        no_inicial1 = int(input("Informe o ponto de partida 1: "))
        no_final1 = int(input("Informe o ponto de destino 1: "))
        no_inicial2 = int(input("Informe o ponto de partida 2: "))
        no_final2 = int(input("Informe o ponto de destino 2: "))
        x = 0

        # Laço para calcular e ajustar o caminho mínimo entre as rotas
        while x == 0:
            # Calcula o caminho mínimo para cada rota usando Dijkstra
            caminho_minimo1 = nx.dijkstra_path(
                G, no_inicial1, no_final1, weight="weight"
            )
            caminho_minimo2 = nx.dijkstra_path(
                G, no_inicial2, no_final2, weight="weight"
            )

            # Cria listas de arestas para cada caminho mínimo
            arcos1 = [
                (caminho_minimo1[i], caminho_minimo1[i + 1])
                for i in range(len(caminho_minimo1) - 1)
            ]
            arcos2 = [
                (caminho_minimo2[i], caminho_minimo2[i + 1])
                for i in range(len(caminho_minimo2) - 1)
            ]

            # Define as cores dos nós e arestas
            cor_dos_nos = []
            cor_dos_arcos = []

            # Adiciona arcos em ambas as direções para ambos os caminhos
            for i in range(0, len(arcos1)):
                arcos1.append((arcos1[i][1], arcos1[i][0]))

            for i in range(0, len(arcos2)):
                arcos2.append((arcos2[i][1], arcos2[i][0]))

            # Ajusta o peso das arestas onde os caminhos se sobrepõem
            for arco in G.edges:
                if arco in arcos1 and arco in arcos2:
                    if arcos2.index(arco) == (arcos1.index(arco)):

                        # Aumenta o peso para diferenciar rotas sobrepostas
                        G[arco[0]][arco[1]]["weight"] += 2

                        # Recalcula os caminhos mínimos com o peso atualizado
                        caminho_minimo1 = nx.dijkstra_path(
                            G, no_inicial1, no_final1, weight="weight"
                        )
                        caminho_minimo2 = nx.dijkstra_path(
                            G, no_inicial2, no_final2, weight="weight"
                        )

                        # Atualiza as listas de arestas após recalcular o caminho
                        arcos1 = [
                            (caminho_minimo1[i], caminho_minimo1[i + 1])
                            for i in range(len(caminho_minimo1) - 1)
                        ]
                        arcos2 = [
                            (caminho_minimo2[i], caminho_minimo2[i + 1])
                            for i in range(len(caminho_minimo2) - 1)
                        ]
                        for i in range(0, len(arcos1)):
                            arcos1.append((arcos1[i][1], arcos1[i][0]))

                        for i in range(0, len(arcos2)):
                            arcos2.append((arcos2[i][1], arcos2[i][0]))
            x = 1

        # Define a cor das arestas dependendo das rotas que passam por elas
        for arco in G.edges:
            if arco in arcos1 and arco in arcos2:
                if arcos2.index(arco) == (arcos1.index(arco)):
                    cor_dos_arcos.append("red")
                else:
                    cor_dos_arcos.append("orange")
            elif arco in arcos2 and arco not in arcos1:
                cor_dos_arcos.append("green")
            elif arco in arcos1 and arco not in arcos2:
                cor_dos_arcos.append("orange")
            else:
                cor_dos_arcos.append("lightgray")

        # Define a cor dos nós dependendo se estão em um, ambos ou nenhum dos caminhos
        for node in G.nodes:
            if node in caminho_minimo1 and node in caminho_minimo2:
                if caminho_minimo1.index(node) == caminho_minimo2.index(node):
                    cor_dos_nos.append("red")
                else:
                    cor_dos_nos.append("green")
            elif node in caminho_minimo1 and node not in caminho_minimo2:
                cor_dos_nos.append("orange")
            elif node in caminho_minimo2 and node not in caminho_minimo1:
                cor_dos_nos.append("green")
            else:
                cor_dos_nos.append("white")

    #############################################################################################

    # Caso o usuário escolha simular três rotas
    elif numero_de_rotas == 3:
        # Solicita entrada dos pontos de partida e destino para três rotas
        no_inicial1 = int(input("Informe o ponto de partida 1: "))
        no_final1 = int(input("Informe o ponto de destino 1: "))
        no_inicial2 = int(input("Informe o ponto de partida 2: "))
        no_final2 = int(input("Informe o ponto de destino 2: "))
        no_inicial3 = int(input("Informe o ponto de partida 3: "))
        no_final3 = int(input("Informe o ponto de destino 3: "))
        x = 0

        # Laço para calcular e ajustar o caminho mínimo entre as rotas
        while x == 0:
            # Calcula o caminho mínimo para cada rota usando Dijkstra
            caminho_minimo1 = nx.dijkstra_path(
                G, no_inicial1, no_final1, weight="weight"
            )
            caminho_minimo2 = nx.dijkstra_path(
                G, no_inicial2, no_final2, weight="weight"
            )
            caminho_minimo3 = nx.dijkstra_path(
                G, no_inicial3, no_final3, weight="weight"
            )

            # Cria listas de arestas para cada caminho mínimo
            arcos1 = [
                (caminho_minimo1[i], caminho_minimo1[i + 1])
                for i in range(len(caminho_minimo1) - 1)
            ]
            arcos2 = [
                (caminho_minimo2[i], caminho_minimo2[i + 1])
                for i in range(len(caminho_minimo2) - 1)
            ]
            arcos3 = [
                (caminho_minimo3[i], caminho_minimo3[i + 1])
                for i in range(len(caminho_minimo3) - 1)
            ]

            # Define as cores dos nós e arestas
            cor_dos_nos = []
            cor_dos_arcos = []

            # Adiciona arcos em ambas as direções para ambos os caminhos
            for i in range(0, len(arcos1)):
                arcos1.append((arcos1[i][1], arcos1[i][0]))

            for i in range(0, len(arcos2)):
                arcos2.append((arcos2[i][1], arcos2[i][0]))

            for i in range(0, len(arcos3)):
                arcos3.append((arcos3[i][1], arcos3[i][0]))

            # Ajusta o peso das arestas onde os caminhos se sobrepõem
            for arco in G.edges:
                if arco in arcos1 or arco in arcos2 or arco in arcos3:
                    if arco in arcos1 and arco in arcos2 and arco not in arcos3:
                        # Aumenta o peso para diferenciar rotas sobrepostas
                        G[arco[0]][arco[1]]["weight"] += 2

                        # Recalcula os caminhos mínimos com o peso atualizado
                        caminho_minimo1 = nx.dijkstra_path(
                            G, no_inicial1, no_final1, weight="weight"
                        )
                        caminho_minimo2 = nx.dijkstra_path(
                            G, no_inicial2, no_final2, weight="weight"
                        )
                        caminho_minimo3 = nx.dijkstra_path(
                            G, no_inicial3, no_final3, weight="weight"
                        )

                        # Atualiza as listas de arestas após recalcular o caminho
                        arcos1 = [
                            (caminho_minimo1[i], caminho_minimo1[i + 1])
                            for i in range(len(caminho_minimo1) - 1)
                        ]
                        arcos2 = [
                            (caminho_minimo2[i], caminho_minimo2[i + 1])
                            for i in range(len(caminho_minimo2) - 1)
                        ]
                        arcos3 = [
                            (caminho_minimo3[i], caminho_minimo3[i + 1])
                            for i in range(len(caminho_minimo3) - 1)
                        ]
                        for i in range(0, len(arcos1)):
                            arcos1.append((arcos1[i][1], arcos1[i][0]))

                        for i in range(0, len(arcos2)):
                            arcos2.append((arcos2[i][1], arcos2[i][0]))

                        for i in range(0, len(arcos3)):
                            arcos3.append((arcos3[i][1], arcos3[i][0]))

                    elif arco in arcos3 and arco in arcos2 and arco not in arcos1:
                        # Aumenta o peso para diferenciar rotas sobrepostas
                        G[arco[0]][arco[1]]["weight"] += 2

                        # Recalcula os caminhos mínimos com o peso atualizado
                        caminho_minimo1 = nx.dijkstra_path(
                            G, no_inicial1, no_final1, weight="weight"
                        )
                        caminho_minimo2 = nx.dijkstra_path(
                            G, no_inicial2, no_final2, weight="weight"
                        )
                        caminho_minimo3 = nx.dijkstra_path(
                            G, no_inicial3, no_final3, weight="weight"
                        )

                        # Atualiza as listas de arestas após recalcular o caminho
                        arcos1 = [
                            (caminho_minimo1[i], caminho_minimo1[i + 1])
                            for i in range(len(caminho_minimo1) - 1)
                        ]
                        arcos2 = [
                            (caminho_minimo2[i], caminho_minimo2[i + 1])
                            for i in range(len(caminho_minimo2) - 1)
                        ]
                        arcos3 = [
                            (caminho_minimo3[i], caminho_minimo3[i + 1])
                            for i in range(len(caminho_minimo3) - 1)
                        ]
                        for i in range(0, len(arcos1)):
                            arcos1.append((arcos1[i][1], arcos1[i][0]))

                        for i in range(0, len(arcos2)):
                            arcos2.append((arcos2[i][1], arcos2[i][0]))

                        for i in range(0, len(arcos3)):
                            arcos3.append((arcos3[i][1], arcos3[i][0]))

                    elif arco in arcos1 and arco in arcos3 and arco not in arcos2:
                        # Aumenta o peso para diferenciar rotas sobrepostas
                        G[arco[0]][arco[1]]["weight"] += 2

                        # Recalcula os caminhos mínimos com o peso atualizado
                        caminho_minimo1 = nx.dijkstra_path(
                            G, no_inicial1, no_final1, weight="weight"
                        )
                        caminho_minimo2 = nx.dijkstra_path(
                            G, no_inicial2, no_final2, weight="weight"
                        )
                        caminho_minimo3 = nx.dijkstra_path(
                            G, no_inicial3, no_final3, weight="weight"
                        )

                        # Atualiza as listas de arestas após recalcular o caminho
                        arcos1 = [
                            (caminho_minimo1[i], caminho_minimo1[i + 1])
                            for i in range(len(caminho_minimo1) - 1)
                        ]
                        arcos2 = [
                            (caminho_minimo2[i], caminho_minimo2[i + 1])
                            for i in range(len(caminho_minimo2) - 1)
                        ]
                        arcos3 = [
                            (caminho_minimo3[i], caminho_minimo3[i + 1])
                            for i in range(len(caminho_minimo3) - 1)
                        ]
                        for i in range(0, len(arcos1)):
                            arcos1.append((arcos1[i][1], arcos1[i][0]))

                        for i in range(0, len(arcos2)):
                            arcos2.append((arcos2[i][1], arcos2[i][0]))

                        for i in range(0, len(arcos3)):
                            arcos3.append((arcos3[i][1], arcos3[i][0]))

                    if arco in arcos1 and arco in arcos2 and arco in arcos3:
                        # Aumenta o peso para diferenciar rotas sobrepostas
                        G[arco[0]][arco[1]]["weight"] += 3

                        # Recalcula os caminhos mínimos com o peso atualizado
                        caminho_minimo1 = nx.dijkstra_path(
                            G, no_inicial1, no_final1, weight="weight"
                        )
                        caminho_minimo2 = nx.dijkstra_path(
                            G, no_inicial2, no_final2, weight="weight"
                        )
                        caminho_minimo3 = nx.dijkstra_path(
                            G, no_inicial3, no_final3, weight="weight"
                        )

                        # Atualiza as listas de arestas após recalcular o caminho
                        arcos1 = [
                            (caminho_minimo1[i], caminho_minimo1[i + 1])
                            for i in range(len(caminho_minimo1) - 1)
                        ]
                        arcos2 = [
                            (caminho_minimo2[i], caminho_minimo2[i + 1])
                            for i in range(len(caminho_minimo2) - 1)
                        ]
                        arcos3 = [
                            (caminho_minimo3[i], caminho_minimo3[i + 1])
                            for i in range(len(caminho_minimo3) - 1)
                        ]
                        for i in range(0, len(arcos1)):
                            arcos1.append((arcos1[i][1], arcos1[i][0]))

                        for i in range(0, len(arcos2)):
                            arcos2.append((arcos2[i][1], arcos2[i][0]))

                        for i in range(0, len(arcos3)):
                            arcos3.append((arcos3[i][1], arcos3[i][0]))
            x = 1

        # Define a cor das arestas dependendo das rotas que passam por elas
        print(arcos1)
        print(arcos2)
        print(arcos3)
        for arco in G.edges:
            if arco in arcos1 or arco in arcos2 or arco in arcos3:
                if arco in arcos1 and arco in arcos2 and arco in arcos3:
                    x = arcos1.index(arco)
                    y = arcos2.index(arco)
                    z = arcos3.index(arco)
                    d = 0
                    if x == y:
                        c = x
                        if z == c: 
                            d = 1
                    if x == z:
                        c = x
                        if y == c: 
                            d = 1
                    if z == y:
                        c = z
                        if x == c: 
                            d = 1

                    if d == 1:
                        cor_dos_arcos.append("red")
                        print("ok")
                    else:
                        cor_dos_arcos.append("green")
                        print("not ok")
                elif arco in arcos1 and arco in arcos2:
                    if arcos1.index(arco) == arcos2.index(arco):
                        cor_dos_arcos.append("red")
                    else:
                        cor_dos_arcos.append("green")
                elif arco in arcos1 and arco in arcos3:
                    if arcos1.index(arco) == arcos3.index(arco):
                        cor_dos_arcos.append("red")
                    else:
                        cor_dos_arcos.append("green")
                elif arco in arcos3 and arco in arcos2:
                    if arcos3.index(arco) == arcos2.index(arco):
                        cor_dos_arcos.append("red")
                    else:
                        cor_dos_arcos.append("green")
                else:
                    cor_dos_arcos.append("green")
            else:
                cor_dos_arcos.append("lightgray")

        # Define a cor dos nós dependendo se estão em um, ambos ou nenhum dos caminhos
        for node in G.nodes:
            if (
                node in caminho_minimo1
                or node in caminho_minimo2
                or node in caminho_minimo3
            ):
                if (
                    node in caminho_minimo1
                    and node in caminho_minimo2
                    and node in caminho_minimo3
                ):
                    if (
                        caminho_minimo1.index(node) == caminho_minimo2.index(node)
                    ) == caminho_minimo3.index(node):
                        cor_dos_nos.append("red")
                    else:
                        cor_dos_nos.append("green")
                elif node in caminho_minimo1 and node in caminho_minimo2:
                    if caminho_minimo1.index(node) == caminho_minimo2.index(node):
                        cor_dos_nos.append("red")
                    else:
                        cor_dos_nos.append("green")
                elif node in caminho_minimo1 and node in caminho_minimo3:
                    if caminho_minimo1.index(node) == caminho_minimo3.index(node):
                        cor_dos_nos.append("red")
                    else:
                        cor_dos_nos.append("green")
                elif node in caminho_minimo3 and node in caminho_minimo2:
                    if caminho_minimo3.index(node) == caminho_minimo2.index(node):
                        cor_dos_nos.append("red")
                    else:
                        cor_dos_nos.append("green")
                else:
                    cor_dos_nos.append("green")
            else:
                cor_dos_nos.append("white")

    else:
        print("Número de rotas inválido!!!")
        exit()
    break

# Gera o gráfico utilizando as bibliotecas
nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_color=cor_dos_nos,
    node_size=300,
    font_color="black",
    font_size=12,
    font_family="Arial",
    font_weight="bold",
    edgecolors="black",
    edge_color=cor_dos_arcos,
    width=5,
)
plt.margins(0.2)
plt.show()
