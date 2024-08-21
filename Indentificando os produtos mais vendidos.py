from collections import Counter

def obter_entrada_produtos():
    entrada = input()
    return [produto.strip() for produto in entrada.split(',')]

def encontrar_produto_mais_vendido(produtos):
    contagem = Counter(produtos)
    max_count = 0
    max_produto = ''
    
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def main():
    produtos = obter_entrada_produtos()
    produto_mais_vendido = encontrar_produto_mais_vendido(produtos)
    print(produto_mais_vendido)

if __name__ == "__main__":
    main()