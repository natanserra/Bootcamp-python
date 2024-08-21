def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    
    # Extraia o ano de cada data e cria uma nova lista com os anos
    anos = [data.split("-")[0] for data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


# Capturar a entrada do usuário
entrada = input()


# Processar a entrada e obter a saída
saida = extrair_anos(entrada)


# Exibir o resultado
print(saida)