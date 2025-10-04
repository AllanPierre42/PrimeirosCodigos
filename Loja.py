#1 Controle de Estoque – Cadastro de produtos (nome + quantidade). Aviso de produtos com
#estoque abaixo de 5. Aviso de produtos zerados: 'Fazer pedido urgente'.
#2 Simulação de Vendas – Registrar vendas (produto + valor). Calcular faturamento total do dia.
#Mostrar produto mais caro e mais barato vendido.
#3 Relatório Final – Exibir no console: • Lista de produtos e quantidades finais no estoque. •
#Faturamento total do dia. • Quantidade de produtos acima de R$100. • Data de geração do
#relatório.
#1 O código deve estar organizado em funções.
#2 O programa principal deve chamar as funções e exibir o relatório no console.
#3 Não será cobrada a entrega. O repositório no GitHub será apenas um treino opcional para
#praticar:
#4 git init → git add . → git commit -m 'primeira versão' → git push origin main
#• Use listas de dicionários para guardar produtos e vendas.
#• Exemplo: estoque = [{'nome': 'Arroz', 'quantidade': 10}], vendas = [{'produto': 'Arroz', 'valor':
#25.0}]
#• Funções sugeridas: cadastrar_produto(), registrar_venda(), estoque_baixo(),
#calcular_faturamento(), relatorio_final().
#• Organização sugerida: main.py (código principal), README.md (explicação do projeto), pasta
#data/ (opcional para simular arquivos externos).

estoque = [
    ["Banana", "Caderno", "Camaro Amarelo", "Peruca", "Computador", "Cenoura"],
    [8, 25, 500000, 39, 5000, 4],
    [20, 3, 0, 6, 5, 15],
]

def listar_estoque(lista):
    for i in range(len(lista[0])):
        print(f"{lista[0][i]} R${lista[1][i]}.00 {lista[2][i]} Unidades")

def controle(lista):
    menos5 = []
    zerado = []
    for i in range(len(lista[0])):
        if lista[2][i-1] <= 5:
            menos5.append(lista[0][i-1])
            menos5.append(lista[1][i-1])
            menos5.append(lista[2][i-1])
        if lista[2][i-1] <= 0:
            zerado.append(lista[0][i-1])
            zerado.append(lista[1][i-1])
            zerado.append(lista[2][i-1])
    print(f"{menos5}\n{zerado}")
        
def carrinho(lista):
    carrinho = []
    while True:
        comando = int(input("1- Ver carrinho\n2- Adicionar produto\n3- Remover produto\n4- Cancelar\n~ "))
        if comando == 1:
            if len(carrinho) == 0:
                print("Zero produtos no carrinho")
            else:
                for i in range(len(carrinho[0])):
                    print(f"{carrinho[0][i]} R${carrinho[1][i]}.00 {carrinho[2][i]} Unidades\n")
        if comando == 2:
            while True:
                print("Ecolha um produto dentre:")
                for i in range(len(lista[0])):
                    print(f"{i+1}- {lista[0][i]}")
                comando2 = input("~ ")




#selecionar produtos que quer comprar

#calcular faturamento total

#relatório final
 

carrinho(estoque)