def obter_entrada_vendas():
    entrada = input()
    return list(map(int, entrada.split(',')))

def calcular_total_e_media(vendas):
    total = sum(vendas)
    media = total / len(vendas)
    return total, media

def main():
    vendas = obter_entrada_vendas()
    total, media = calcular_total_e_media(vendas)
    print(f"{total}, {media:.2f}")

if __name__ == "__main__":
    main()