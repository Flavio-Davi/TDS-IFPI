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
    
