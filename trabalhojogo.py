import random
CAPACIDADE = 4

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    valores: list
    topo: int

    def __init__(self) -> None:
        '''
        Cria uma nova pilha com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.valores = []
        self.topo = -1

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> p = Pilha()
        >>> for i in range(CAPACIDADE):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.desempilha() == str(CAPACIDADE - 1)
        True
        '''
        if self.topo >= CAPACIDADE - 1:
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores.append(item)

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha()
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
        '''
        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores.pop()
        self.topo = self.topo - 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha()
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1
    
    def __iter__(self):
        '''
        Permite a iteração sobre os elementos da pilha.
        '''
        return iter(self.valores)

def main() -> None:
    print('Bem-vindo ao jogo de gerenciamento de pilhas!')
    print('Com quantos números você deseja jogar este jogo? Escolha um número entre 1 e 7.\n')
    n = input('- ')
    try:
        n_convertido = int(n)
        n_convertido = converte_n(n_convertido)
        comecarjogo(n_convertido)
    except ValueError:
        print('Entrada inválida! Por favor, insira um número válido.')

def comecarjogo(n: int) -> None:
    pilhas = criarpilhas(n)
    imprimir_pilhas(pilhas)
    print(f'Jogo iniciado com {n + 2} pilhas.')
    
def converte_n(n: int) -> int:
    while n < 2 or n > 6:
        print('\nValor inválido! Tente novamente, por favor')
        n = input('- ')
        try:
            n = int(n)
        except ValueError:
            print('Entrada inválida! Por favor, insira um número válido.')
            continue
    print('\nVocê selecionou ', n, ', prepare-se para o jogo!')
    return n
    
def criarpilhas(n: int) -> list:
    pilhas = []
    lista_aleatoria = lista_auxiliar(n)
    for _ in range(n + 2):
        pilhas.append(Pilha())
    j = 0
    for i in range(n):
        pilhas[i].empilha(lista_aleatoria[j])
        pilhas[i].empilha(lista_aleatoria[j + 1])
        pilhas[i].empilha(lista_aleatoria[j + 2])
        pilhas[i].empilha(lista_aleatoria[j + 3])
        j = j + 4
    return pilhas

def lista_auxiliar(n: int) -> list:
    l = []
    for i in range(1, n + 1):
        l.append(i)
        l.append(i)
        l.append(i)
        l.append(i)
    random.shuffle(l)
    return l

def imprimir_pilhas(pilhas: list) -> None:
    altura = max(len(pilha.valores) for pilha in pilhas)
    for i in range(altura - 1, -1, -1):
        for pilha in pilhas:
            if len(pilha.valores) > i:
                print(f'{pilha.valores[i]:<5}', end=' ')
            else:
                 print('     ', end=' ')
        print()
    print('___   ' * len(pilhas))

if __name__ == '__main__':
    main()