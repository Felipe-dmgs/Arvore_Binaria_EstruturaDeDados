PRIMEIRA ETAPA
desenvolver a base do projeto, importei as bibliotecas que usamos na aula de grafos Matplotlib e Networkx

Usei o código da aula de grafos como base

percebi que para começarmos no networkx temos que criar um graph e que permitisse loops em si mesmo, graphs que fazem parte dessa categoria são o Graph básico e o DiGraph,
sendo o Graph a classe base dos gráficos indiretos ele permite Self loops, ou seja loops em si mesmo, mas não permite múltiplos "cantos" edges.
Já o DiGraph é a classe base dos gráficos diretos, ele guarda nós e vértices com data e/ou atributos opcionais. Basicamente o Graph não é direcionado
então suas conexões arestas tem uma relação mútua então o nó A esta conectado nó B assim como o B está conectado ao A, enquanto o DiGraph por ser direcionado 
tem uma relação origem e destino, ou seja, uma conexão de A para B não força uma conexão de B para A. e é assim que uma árvore deve funcionar os nós filhos não sobem na arvore

Verificamos se a lista esta vazia se estiver ela retorna o gráfico e o dicionário
em seguida criamos uma função dentro a função pois nela que acontecera a recursividade.

Dentro dessa função pedimos como parâmetro a lista, o x e o y e a layer_width a layer sera o nível da arvore e o x e y são para a posição que cada item devera ficar na hora da plotagem.

então verificamos se a lista esta vazia, pegaremos o meio da lista e o valor que esta nessa posição. ele será o nó base e adicionaremos ele ao gráfico chamando o gráfico e
adicionando o nó com o valor que pegamos e a sua posição no gráfico é o x e y, em seguida criamos uma variável que ira receber a recursividade dessa função, onde iremos mandar a
lista recortada, e mudaremos o x e y dimuindo 1 no Y  e o X sera a layer width pela metade sendo esse o filho da esquerda.

Verificamos se ele é nulo se não for adicionamos uma vértice entre o valor do meio e ele,em seguida fazemos o mesmo para o filho da direita e vai indo assim pois a lista 
vai sendo recortada no meio as conexões entre seus números são criadas e as vértices são feitas. no final retornamos o valor. e fechamos essa função logo abaixo já chamamos
ela com o x e y = 0 e layer_width = 10, depois criamos a variável pos e atribuímos um nx.get_node_attributes(G,'pos'), onde ele olha o gráfico G verifica para cada nó se ele 
tem uma pos, que no caso é o x e y, se tiver cria um dicionário com eles, onde a chave é o valor da posição e o valor é a posição. depois disso retornamos esse gráfico completo
que é a própria arvore binária pronta e um dicionário com valor e posição para cada elemento.

Em seguida desenvolvemos a função da pesquisa binaria que será como o professor nos mostrou na ultima aula que ele jogou no ava e que tentamos desenvolver. essa função pede 
uma lista, o elemento a ser encontrado, um inicio que o default é 0 e um fim que o default é none. verificamos se o fim = None se sim quer dizer que é a primeira vez que 
essa função esta sendo chamada ai atribuímos ao fim o len do vetor -1 para pegar o index do ultimo item da lista, verificamos se o inicio é menor ou igual ao fim se for, quer
dizer que a lista não esta se ultrapassando, e ai pegamos uma variável chamada índice e atribuímos a ela o meio da lista que vai ser o inicio + fim //2 onde vai retornar o index 
inteiro do item que esta no meio da lista. verificamos se o item que esta nesse índice é o valor que queremos encontrar se for retornamos o índice se não, vemos se esse valor é 
menor ou maior assim podemos saber se ele está a esquerda na árvore ou a direita se for menor iremos retornar a função com recursividade onde entregamos todos os valores iguais 
exceto o fim,pois já que valor é menor que o que encontramos ele ira esta a esquerda na lista logo será o meio -1 terminando antes da metade e no else quer dizer que o valor é 
maior que o que encontramos então retornamos o fim como está e o inicio será o índice +1 assim ele começara depois da metade. Se no final desseas recursividades não encontrarmos 
retornamos None.

em seguida criamos algumas variáveis uma chamada fig, uma chamada ax e outra chamada plt onde a fig é a figura ou seja o papel do matplotlib é onde iremos plotar nosso projeto,
já é ax são os eixos é a área interna onde tudo irá acontecer separando a parte onde ficará o projeto da "borda" do papel, ai usamos o plt.subplots(figsize=(10,7)) onde criamos 
esses itens e atribuímos que a janela terá 10 polegadas de largura e 7 de altura. Em seguida chamamos a função plt.subplots_adjust(bottom=0.25), isso irá empurrar a parte da 
arvore um pouco para cima no "papel" assim terá mais espaço embaixo para adicionarmos os botões.
depois criamos um titulo usando a função ax.set_title("xxxxxxx") onde setamos o titulo do projeto e usamos o ax.axis("off") para escondermos os valores das codernadas,
pois por padrão o matplotlib mostra essas informações.

Agora iremos criar a função atualizar_plot que recebe como parâmetro um destaque com default None

limpamos o ax com um ax.clear e setamos um titulo diferente 
pegamos a lista e a ordenamos
chamamos a função de criar a arvore e atribuímos a arvore a variável G e o dicionário de posições a variável pos. Usamos a função G.number_of_nodes() para verifarmos a 
quantidade de nós que temos no gráfico se isso for maior que 0 se sim, criamos uma lista chamada cores e fazemos um for com os nós. se algum dos nós for um destaque ele irá ter a
cor vermelha se não irá manter a cor de sempre

em seguida usamos o nx.draw para desenharmos tudo na tela passando o gráfico e as posições, passamos o ax como onde tudo deve ser desenhado, passamos a lista de cores como as
cores que devem ser usadas e arrows = True para aparecerem as conexões entre os nós, colocamos um tamanho de 800 nos nós e o tipo de font. Se o número de nós for menor que 0 então 
desenhamos um texto no meio da tela indicando que a lista/Arvore está vazia, e após esse if reafirmamos que não precisa mostrar as cordenadas com axis off e damos um plt.draw
para jogar na tela

A próxima função será a base de tudo iremos criar uma variável global chamada lista atual, que ira poder ser acessada de qlq lugar. e tentamos criar a lista verificamos se 
ele é um digito separamos os números susando a virgual damos um strip para tirarmos qualquer espaço em branco que tenha entre o numero e as virgulas e criamos uma lista com
cada um desses números se estiver tudo certo iremos setar ela para não termos números repetidos e daremos um sort para organizamos ela chamamos a função atualizar_plot para 
renderizar a tela e printamos no terminal que a lista foi criada para qlq bug se algum erro acontecer como ter uma letra na lista ou ter numero separados por muitos espaços ou
outras coisas iremos printar que devem ser separados por virgulas

Abaixo será os eventos de click

Primeiro o de inserir
criamos a função evento inserir que recebe como parâmetro um event

verificamos se o numero que esta no input para inserir é valido se sim verificamos se ele não esta na lista se sim apenddamos ele a lista e renderizamos a lista novamente se já 
estiver na lista ou não for um numero valido ira ser printado no temrinal

Agora o evento de encontrar
Esse já esta praticamente pronto 
iremos criar a função e assim como na ultima verifaceremos se é um numero valido se for iremos chamar a função pesquisa_binaria passando a lista e o valor se encontrado
vamos atualizar o plot passando o valor como destaque assim sua cor sera alterada se não iremos printar que não esta na lista e atualizaremos o plot.


Agora o evento para excluir no geral é semelhante única diferença e que daremos um pop no valor  para finalizar criaremos o botões da aplicação passando suas posições,
valores e eventos que serão chamados depois chamamos a função evento criar passando o texto da textoBox como lista e damos um plt.show() para iniciarmos a aplicação
