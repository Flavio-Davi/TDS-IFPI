from pessoa import Pessoa

def test_casamento_sucesso():
    a = Pessoa("Maria", 30, 65, 1.7, 'F')
    b = Pessoa("João", 32, 75, 1.8, 'M')
    a.casar(b)
    esperado = b
    saida = a.conjuge
    
    assert saida == esperado


def test_casamento_falha_ja_casado():
    a = Pessoa("Maria", 30, 65, 1.7, 'F')
    b = Pessoa("João", 32, 75, 1.8, 'M')
    c = Pessoa("Ana", 28, 55, 1.65, 'F')
    a.casar(b)
    b.casar(c)
    esperado = None
    saida = c.conjuge

    assert saida == esperado


def test_morte_encerra_casamento():
    a = Pessoa("Maria", 30, 65, 1.7, 'F')
    b = Pessoa("João", 32, 75, 1.8, 'M')
    a.casar(b)
    a.morrer()
    esperado = None
    saida = b.conjuge

    assert saida == esperado


def test_casamento_apos_morte_conjuge():
    a = Pessoa("Maria", 30, 65, 1.7, 'F')
    b = Pessoa("João", 32, 75, 1.8, 'M')
    c = Pessoa("Ana", 28, 55, 1.65, 'F')
    a.casar(b)
    a.morrer()
    b.casar(c)
    esperado = c
    saida = b.conjuge

    assert saida == esperado


def test_divorcio_funciona():
    a = Pessoa("Maria", 30, 65, 1.7, 'F')
    b = Pessoa("João", 32, 75, 1.8, 'M')
    a.casar(b)
    a.divorciar()
    esperado = None
    saida = a.conjuge

    assert saida == esperado


def test_adocao_sucesso():
    a = Pessoa("Pedro", 10, 30, 1.4, 'M')
    b = Pessoa("Carla", 35, 60, 1.65, 'F')
    a.adocao(b)
    esperado = b
    saida = a.mae_adotiva

    assert saida == esperado


def test_adocao_falha_por_menor():
    a = Pessoa("Pedro", 10, 30, 1.4, 'M')
    b = Pessoa("Jovem", 16, 50, 1.6, 'F')
    a.adocao(b)
    esperado = None
    saida = a.mae_adotiva

    assert saida == esperado


def test_adocao_falha_ja_adotado():
    a = Pessoa("Pedro", 10, 30, 1.4, 'M')
    b = Pessoa("Carla", 35, 60, 1.65, 'F')
    c = Pessoa("Laura", 40, 58, 1.6, 'F')
    a.adocao(b)
    a.adocao(c)
    esperado = b
    saida = a.mae_adotiva

    assert saida == esperado
