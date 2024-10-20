despesas = []

def adicionar_despesas():
    while True:
        print('Bem vindo ao seu Gerenciador de despesas')
        despesa = input('Digite sua nova despesa: ')
        categorias = [
            'Alimentação',
            'Transporte',
            'Moradia',
            'Saúde',
            'Lazer',
            'Educação',
            'Vestuário',
            'Serviços',
            'Investimentos',
            'Outros'
        ]
        print('Escolha uma das categorias abaixo: ')
        for i, categoria in enumerate(categorias, 1):
            print(f'{i}. {categoria}')

        escolha_categoria = int(input('Digite o número correspondente à categoria: ')) -1
        valor = float(input('Agora digite o valor da despesa: R$'))

        if 0 <= escolha_categoria < len(categorias):
            nome_categoria = categorias[escolha_categoria]
            print(f'Despesa: {despesa} | Categoria: {nome_categoria} | Valor: R${valor}')

            despesas.append({
                'Despesa': despesa,
                'Categoria': nome_categoria,
                'Valor': valor
            })

        else:
            print("Opção inválida. Tente novamente.")

        nova_despesa = input('Você quer adicionar uma nova despesa? (Sim/Não) ').strip().lower()

        if nova_despesa != 'sim':
            break

def listar_despesas():
    print('\nLista de Despesas: ')
    if despesas:
        for d in despesas:
            print(f"Despesa: {d['Despesa']} | Categoria: {d['Categoria']} | Valor: R${d['Valor']}") 
        
    else:
        print("Nenhuma despesa registrada.")


def editar_despesas():
    while True:
        editar = input('Você deseja editar alguma despesa? (Sim/Não) ').strip().lower()

        if editar != 'sim':
            break

        nome_despesa = input('Digite o nome da despesa para edição: ')

        # Verifica se a despesa existe na lista
        for despesa in despesas:
            if despesa['Despesa'].lower() == nome_despesa.lower():
                print(f"Despesa encontrada: {despesa['Despesa']} | Categoria: {despesa['Categoria']} | Valor: R${despesa['Valor']}")

                # Pergunta o que deseja editar
                novo_nome = input('Deseja alterar o nome da despesa? Deixe em branco para manter o mesmo: ').strip()
                if novo_nome:
                    despesa['Despesa'] = novo_nome

                nova_categoria = input('Deseja alterar a categoria? Deixe em branco para manter a mesma: ').strip()
                if nova_categoria:
                    categorias = [
                        'Alimentação',
                        'Transporte',
                        'Moradia',
                        'Saúde',
                        'Lazer',
                        'Educação',
                        'Vestuário',
                        'Serviços',
                        'Investimentos',
                        'Outros'
                    ]
                    print('Escolha uma das categorias abaixo: ')
                    for i, categoria in enumerate(categorias, 1):
                        print(f'{i}. {categoria}')
                    
                    escolha_categoria = int(input('Digite o número correspondente à nova categoria: ')) - 1
                    if 0 <= escolha_categoria < len(categorias):
                        despesa['categoria'] = categorias[escolha_categoria]
                    else:
                        print("Opção de categoria inválida, mantendo a categoria anterior.")

                novo_valor = input('Deseja alterar o valor? Deixe em branco para manter o mesmo: ').strip()
                if novo_valor:
                    despesa['valor'] = float(novo_valor)

                print("Despesa atualizada com sucesso!")
                break
        else:
            print("Despesa não encontrada. Tente novamente.")


def apagar_despesa():
    while True:
        apagar = input('Você deseja apagar alguma despesa? (Sim/Não) ').strip().lower()

        if apagar != 'sim':
            break

        despesa_apagar = input('Digite o nome da despesa que deseja apagar: ')

        for despesa in despesas:
            if despesa['Despesa'].lower() == despesa_apagar.lower():
                print(f'Despesa encontrada: {despesa['Despesa']} | Categoria: {despesa['Categoria']} | Valor: {despesa['Valor']}')

            confirmacao = input('Você tem certeza que deseja apagar essa despesa? (Sim/Não)').strip().lower()

            if confirmacao == 'sim':
                despesas.remove(despesa)
                print('Despesa apagada com sucesso!')
            else:
                print('Operação cancelada.')
            break
        else:
            print('Despesa não encontrada')

def valor_total():
    total = 0 
    
    for despesa in despesas:
        print(f"Despesa: {despesa['Despesa']} | Categoria: {despesa['Categoria']} | Valor: R${despesa['Valor']}")
        total += despesa['Valor'] 
    
    print('\nEsse é o valor total de todas as suas despesas:')
    print(f'Valor total: R${total:.2f}')

              
adicionar_despesas()
listar_despesas()
editar_despesas()
apagar_despesa()
valor_total()