from collections import defaultdict, deque

# Função para calcular a diferença de tempo
def diferenca_tempo(hora_inicio, hora_fim):
    dif_tempo = hora_fim - hora_inicio
    if dif_tempo < 0:
        dif_tempo += 24
    return dif_tempo

# Função para realizar a BFS
def rota_mais_curta_bfs(grafo, cidade_inicio, cidade_fim):
    visitado = set()
    fila = deque([(cidade_inicio, 18, 0)])  # Começa às 18:00 e sem sangue inicial

    while fila:
        cidade_atual, hora_partida, sangue = fila.popleft()
        visitado.add(cidade_atual)

        if cidade_atual == cidade_fim:
            return sangue  # Vladimir chegou ao destino

        for vizinho, partida, tempo_viagem in grafo[cidade_atual]:
            dif_tempo = diferenca_tempo(hora_partida, partida)
            if 6 <= dif_tempo <= 18:  # Verifica se está dentro do período permitido
                nova_hora_partida = (partida + tempo_viagem) % 24
                if nova_hora_partida < 18:
                    novo_sangue = sangue + (nova_hora_partida - 12)
                else:
                    novo_sangue = sangue + (nova_hora_partida - 24 + 12)
                if novo_sangue < 0:
                    novo_sangue = 0  # Não pode ser negativo
                if vizinho not in visitado:
                    fila.append((vizinho, nova_hora_partida, novo_sangue))

    return None

# Função principal
def main():
    num_casos_teste = int(input())

    for caso_teste in range(1, num_casos_teste + 1):
        num_rotas = int(input())

        # Criar um dicionário para armazenar as rotas para cada cidade
        rotas = defaultdict(list)

        for _ in range(num_rotas):
            cidade1, cidade2, partida, tempo_viagem = input().split()
            partida = int(partida)
            tempo_viagem = int(tempo_viagem)
            rotas[cidade1].append((cidade2, partida, tempo_viagem))

        cidade_inicio, cidade_fim = input().split()

        # Realizar a BFS para encontrar a rota mais curta
        resultado = rota_mais_curta_bfs(rotas, cidade_inicio, cidade_fim)

        # Imprimir o resultado
        print(f"Test Case {caso_teste}.")
        if resultado is not None:
            print(f"Vladimir needs {resultado} litre(s) of blood.")
        else:
            print("There is no route Vladimir can take.")

if __name__ == "__main__":
    main()
