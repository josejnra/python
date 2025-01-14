"""
Maneiras de ser ler e escrever em arquivos
"""

# ler arquivo
f = open("nome_arquivo.txt")
for linha in f:
    print(linha, end="")
f.close()

# outra maneira de ser ler arquivos_e_graficos
with open("nome_arquivo.txt") as f:
    for linha in f.readlines():
        print(linha, end="")

# variação da segunda forma, imprime todo conteudo de uma vez
with open("nome_arquivo.txt") as f:
    conteudo = f.read()
    print(conteudo)

"""
Com with o arquivo é fechado automaticamente, mesmo que ocorra exceções
"""
