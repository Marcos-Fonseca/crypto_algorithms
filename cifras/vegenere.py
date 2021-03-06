# Universidade Estadual do Rio Grande do Norte - Curso de Ciências da Computação
# Disciplina: Segurança em Redes de Computadores
# Alunos: Jefferson Ximenes, Marcos Fonseca

""" implementacao da cifra de vegenere

funcoes publicas:
 - encriptar
 - decriptar
"""

import string

def _criar_tabela():
    """retona uma tabela 26x26 contendo um alfabeto de ordem alternada em cada linha"""

    alfabeto = list(string.ascii_lowercase)
    tabela = []

    for x in range(len(string.ascii_lowercase)):
        linha = alfabeto[:] # [:] slice, faz com que a passagem do objeto seja por copia
        tabela.append(linha)

        alfabeto.append(alfabeto[0])
        del(alfabeto[0])

    return tabela

def _tratar_chave(chave: str, msg: str) -> str:
    """Aumenta o tamanho da chave pra que tenha o mesmo tamanho da mensagem"""

    chave = list(chave)
    nova_chave = []
    
    for caractere in msg:
        if caractere != ' ':
            nova_chave.append(chave[0])
            chave.append(chave[0])
            del(chave[0])
        else:
            nova_chave.append(' ')

    return ''.join(nova_chave)

# ===================== encriptar =====================

def encriptar(mensagem:str, chave: str) -> str:
    """codifica a mensagem a partir de uma chave usando a cifra de vegenere"""

    chave = _tratar_chave(chave, mensagem).split()
    msg = mensagem.split()

    msg_codificada = []
    for x in range(len(msg)):
        msg_codificada.append(_codificar(msg[x], chave[x]))

    return ' '.join(msg_codificada)

def _codificar(msg: str, chave: str) -> str:
    """mapea a linha referente a letra da chave e coluna referente a mensagem da chave"""

    tabela = _criar_tabela()
    msg_codificada = []

    for letra in range(len(msg)):
        x = 0
        while True:
            if chave[letra] == tabela[x][0]:
                linha = x
                coluna = tabela[0].index(msg[letra])

                msg_codificada.append(tabela[linha][coluna])
                break
            else:
                x += 1

    return ''.join(msg_codificada)

# ===================== decriptar =====================

def decriptar(mensagem:str, chave: str) -> str:
    """decodifica a mensagem a partir de uma chave usando a cifra de vegenere"""

    chave = _tratar_chave(chave, mensagem).split()
    msg = mensagem.split()

    msg_decodificada = []
    for x in range(len(msg)):
        msg_decodificada.append(_decodificar(msg[x], chave[x]))

    return ' '.join(msg_decodificada)

def _decodificar(msg: str, chave: str) -> str:
    """mapea a linha referente a letra da chave e coluna referente a mensagem da chave"""

    tabela = _criar_tabela()
    msg_decodificada = []

    for letra in range(len(msg)):
        x = 0
        while True:
            if chave[letra] == tabela[x][0]:
                linha = x
                coluna = tabela[x].index(msg[letra])

                msg_decodificada.append(tabela[0][coluna])
                break
            else:
                x += 1

    return ''.join(msg_decodificada)
    
if __name__ == '__main__':
    # testes
    assert encriptar('todo mundo odeia o chris', chave='sucodefruta') == 'lifc pysui hdwcc c flwzm'
    assert decriptar('lifc pysui hdwcc c flwzm', chave='sucodefruta') == 'todo mundo odeia o chris'