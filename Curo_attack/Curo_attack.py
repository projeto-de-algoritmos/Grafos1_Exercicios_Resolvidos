def pode_alcancar(u, anterior, k, t):
    if t == k:
        return True
    ret = False
    for v in adj[u]:
        if v == anterior:
            continue
        ret |= pode_alcancar(v, u, k, t + 1)
    return ret

def contar_caminhos(u, anterior, k, t):
    ret = 1
    if t == k:
        return ret
    for v in adj[u]:
        if v == anterior:
            continue
        ret += contar_caminhos(v, anterior, k, t + 1)
    return ret

while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break

    if n == 0 and k == 0:
        break

    adj = [[] for _ in range(n + 1)]
    edg = []

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edg.append((u, v))

    ans = -1
    for i in range(len(edg)):
        u, v = edg[i]
        if k % 2:
            metade_superior = k // 2
            metade_inferior = k // 2
            if pode_alcancar(u, v, metade_superior, 0) and pode_alcancar(v, u, metade_inferior, 0):
                ans = max(ans, contar_caminhos(u, v, metade_superior, 0) + contar_caminhos(v, u, metade_inferior, 0))
        else:
            metade_superior = (k - 1) // 2
            metade_inferior = k // 2
            if pode_alcancar(u, v, metade_superior, 0) and pode_alcancar(v, u, metade_inferior, 0):
                ans = max(ans, contar_caminhos(u, v, metade_superior, 0) + contar_caminhos(v, u, metade_inferior, 0))
            u, v = v, u
            if pode_alcancar(u, v, metade_superior, 0) and pode_alcancar(v, u, metade_inferior, 0):
                ans = max(ans, contar_caminhos(u, v, metade_superior, 0) + contar_caminhos(v, u, metade_inferior, 0))

    if ans == -1:
        print("Impossible revenge!")
    else:
        print(ans)
