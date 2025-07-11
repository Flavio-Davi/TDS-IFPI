import pytest
from Universidade import *

def test_matricular_adiciona_aluno_na_lista():
    uni = Universidade("UFPI",1)
    Maria = Aluno("Maria","516516516", 20251001)
    tam = len(uni.alunos)

    resultado = uni.matricular(Maria)

    assert resultado is True
    assert Maria in uni.alunos
    assert len(uni.alunos) == tam+1

def test_matricular_aluno_publica_cpf_duplicado():
    uni1 = Universidade("UFPI",1)
    uni2 = Universidade("UESPI",1)
    aluno1 = Aluno("Maria","123456789", 20251001)
    aluno2 = Aluno("João","123456789", 20251002)
    
    uni1.matricular(aluno1)
    resultado = uni2.matricular(aluno2)
    
    assert resultado is False
    assert aluno2 not in uni2.alunos

def test_matricular_aluno_particular_cpf_duplicado():
    uni_publica = Universidade("UFPI",1)
    uni_particular = Universidade("FACID",2)
    aluno1 = Aluno("Maria","123456789", 20251001)
    aluno2 = Aluno("João","123456789", 20251002)
    
    uni_publica.matricular(aluno1)
    resultado = uni_particular.matricular(aluno2)
    
    assert resultado is True
    assert aluno2 in uni_particular.alunos

def test_matricular_objeto_nao_aluno():
    uni = Universidade("UFPI",1)
    objeto_invalido = "não é um aluno"
    
    resultado = uni.matricular(objeto_invalido)
    
    assert resultado is False

def test_remover_aluno_da_lista():
    uni = Universidade("UFPI",1)
    aluno = Aluno("Maria","123456789", 20251001)
    uni.matricular(aluno)
    
    uni.remover(aluno)
    
    assert aluno not in uni._alunos_publicas

def test_remover_aluno_publica_remove_da_lista_global():
    uni = Universidade("UFPI",1)
    aluno = Aluno("Maria","123456789", 20251001)
    uni.matricular(aluno)
    
    uni.remover(aluno)
    
    assert aluno not in Universidade._alunos_publicas

def test_propriedades_universidade():
    uni = Universidade("UFPI",1)
    
    assert uni.nome == "UFPI"
    assert uni.tipo == 1
    assert isinstance(uni.alunos, list)

def test_propriedades_aluno():
    aluno = Aluno("Maria","123456789", 20251001)
    
    assert aluno.nome == "Maria"
    assert aluno.cpf == "123456789"
    assert aluno.matricula == 20251001

def test_multiplas_particulares_mesmo_cpf():
    uni1 = Universidade("FACID",2)
    uni2 = Universidade("UNINOVAFAPI",2)
    aluno1 = Aluno("Maria","123456789", 20251001)
    aluno2 = Aluno("João","123456789", 20251002)
    
    resultado1 = uni1.matricular(aluno1)
    resultado2 = uni2.matricular(aluno2)
    
    assert resultado1 is True
    assert resultado2 is True
    assert aluno1 in uni1.alunos
    assert aluno2 in uni2.alunos
