import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button, TextBox

lista_atual = []

def criar_arvore_balanceada(lista_ordenada):
    G = nx.DiGraph()
    if not lista_ordenada:
        return G, {}
    def adicionar_nos_recursivo(sublista, x, y, layer_width):
        if not sublista:
            return None
        
        meio = len(sublista) // 2
        no_valor = sublista[meio]
        
        G.add_node(no_valor, pos=(x, y))
        
        filho_esq = adicionar_nos_recursivo(
            sublista[:meio], 
            x - layer_width, 
            y - 1, 
            layer_width / 2
        )
        if filho_esq is not None:
            G.add_edge(no_valor, filho_esq)
            
        filho_dir = adicionar_nos_recursivo(
            sublista[meio+1:], 
            x + layer_width, 
            y - 1, 
            layer_width / 2
        )
        if filho_dir is not None:
            G.add_edge(no_valor, filho_dir)
            
        return no_valor

    adicionar_nos_recursivo(lista_ordenada, x=0, y=0, layer_width=10)
    
    pos = nx.get_node_attributes(G, 'pos')
    return G, pos

def pesquisa_binaria(vetor, item, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1
    if inicio <= fim:
        indice = (inicio + fim) // 2
        if vetor[indice] == item:
            return indice
        if item < vetor[indice]:
            return pesquisa_binaria(vetor, item, inicio, indice - 1)
        else:
            return pesquisa_binaria(vetor, item, indice + 1, fim)
    return None

fig, ax = plt.subplots(figsize=(10, 7))
plt.subplots_adjust(bottom=0.25) 
ax.set_title("Árvore Binária de Busca Balanceada")
ax.axis('off')

def atualizar_plot(destaque=None):
    ax.clear()
    ax.set_title(f"Árvore Balanceada (Lista: {len(lista_atual)} itens)")
    
    lista_atual.sort()
    
    G, pos = criar_arvore_balanceada(lista_atual)
    
    if G.number_of_nodes() > 0:
        
        cores = []
        for node in G.nodes():
            if node == destaque:
                cores.append('#FF5733') 
            else:
                cores.append('#A7D0E8')
        
        nx.draw(G, pos, ax=ax, with_labels=True, node_size=800, 
                node_color=cores, font_weight='bold', arrows=True)
    else:
        ax.text(0.5, 0.5, "Árvore Vazia", ha='center', transform=ax.transAxes)

    ax.axis('off')
    plt.draw()

def evento_criar(texto):
    global lista_atual
    try:
        numeros = [int(x.strip()) for x in texto.split(',') if x.strip().isdigit()]
        lista_atual = sorted(list(set(numeros)))
        atualizar_plot()
        print(f"Lista criada: {lista_atual}")
    except ValueError:
        print("Erro: Insira números separados por vírgula.")

def evento_inserir(event):
    global lista_atual
    try:
        val = int(text_box_operacao.text)
        if val not in lista_atual:
            lista_atual.append(val)
            atualizar_plot(destaque=val) 
            print(f"Inserido: {val}")
        else:
            print(f"O número {val} já existe na árvore.")
    except ValueError:
        print("Erro: Digite um número válido na caixa de operação.")

def evento_encontrar(event):
    try:
        val = int(text_box_operacao.text)
        idx = pesquisa_binaria(lista_atual, val)
        
        if idx is not None:
            print(f"ENCONTRADO: O número {val} está no índice {idx} da lista ordenada.")
            atualizar_plot(destaque=val)
        else:
            print(f"O número {val} não está na lista.")
            atualizar_plot(destaque=None)
    except ValueError:
        print("Erro: Digite um número válido.")

def evento_excluir(event):
    global lista_atual
    try:
        val = int(text_box_operacao.text)
        idx = pesquisa_binaria(lista_atual, val)
        
        if idx is not None:
            lista_atual.pop(idx)
            print(f"REMOVIDO: O número {val} foi deletado. Rebalanceando...")
            atualizar_plot()
        else:
            print(f"O número {val} não existe para ser excluído.")
    except ValueError:
        print("Erro: Digite um número válido.")

axbox_lista = plt.axes([0.15, 0.15, 0.5, 0.05])
text_box_lista = TextBox(axbox_lista, 'Lista Inicial\n(sep. vírgula)', initial="1,3,5,7,8,9,10,15,23,43,67,89")
text_box_lista.on_submit(evento_criar)

axbtn_criar = plt.axes([0.7, 0.15, 0.15, 0.05])
btn_criar = Button(axbtn_criar, 'Criar / Resetar', color='lightgreen')
btn_criar.on_clicked(lambda x: evento_criar(text_box_lista.text))

axbox_operacao = plt.axes([0.15, 0.05, 0.2, 0.05])
text_box_operacao = TextBox(axbox_operacao, 'Número:', initial="")

axbtn_ins = plt.axes([0.4, 0.05, 0.15, 0.05])
btn_ins = Button(axbtn_ins, 'Inserir', hovercolor='0.975')
btn_ins.on_clicked(evento_inserir)

axbtn_enc = plt.axes([0.56, 0.05, 0.15, 0.05])
btn_enc = Button(axbtn_enc, 'Encontrar', hovercolor='0.975')
btn_enc.on_clicked(evento_encontrar)

axbtn_exc = plt.axes([0.72, 0.05, 0.15, 0.05])
btn_exc = Button(axbtn_exc, 'Excluir', hovercolor='#ffaaaa')
btn_exc.on_clicked(evento_excluir)

evento_criar(text_box_lista.text)

plt.show()