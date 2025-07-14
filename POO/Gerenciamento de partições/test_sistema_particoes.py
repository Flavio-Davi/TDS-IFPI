import pytest
from sistema_particoes import *


def test_criar_arquivo():
    arquivo = Arquivo("teste.txt", 100)
    assert arquivo.nome == "teste.txt"
    assert arquivo.tamanho_bytes == 100


def test_windows_criar_pasta():
    windows = Windows("Windows")
    windows.criar_pasta("Documentos")
    assert len(windows.gerenciador_de_arquivos) == 1


def test_windows_adicionar_arquivo():
    windows = Windows("Windows")
    windows.criar_pasta("Documentos")
    arquivo = Arquivo("teste.txt", 100)
    windows.adicionar_arquivo("Documentos", arquivo)
    assert len(windows.gerenciador_de_arquivos[0][1]) == 1


def test_windows_calcular_tamanho():
    windows = Windows("Windows")
    windows.criar_pasta("Documentos")
    arquivo = Arquivo("teste.txt", 100)
    windows.adicionar_arquivo("Documentos", arquivo)
    assert windows.calcular_tamanho_total() == 100


def test_linux_criar_pasta():
    linux = Linux("Linux")
    linux.criar_pasta("home")
    assert "home" in linux.gerenciador_de_arquivos


def test_linux_adicionar_arquivo():
    linux = Linux("Linux")
    linux.criar_pasta("home")
    arquivo = Arquivo("teste.py", 200)
    linux.adicionar_arquivo("home", arquivo)
    assert len(linux.gerenciador_de_arquivos["home"]) == 1


def test_linux_calcular_tamanho():
    linux = Linux("Linux")
    linux.criar_pasta("home")
    arquivo = Arquivo("teste.py", 200)
    linux.adicionar_arquivo("home", arquivo)
    assert linux.calcular_tamanho_total() == 200


def test_particao_criar():
    particao = Particao("C:")
    assert particao.nome == "C:"
    assert particao.sistema_operacional is None


def test_particao_associar_so():
    particao = Particao("C:")
    windows = Windows("Windows")
    particao.associar_sistema_operacional(windows)
    assert particao.sistema_operacional == windows


def test_gerenciador_criar_particao():
    gerenciador = GerenciadorDeParticoes()
    particao = gerenciador.criar_particao("C:")
    assert len(gerenciador.particoes) == 1
    assert particao.nome == "C:"


def test_gerenciador_obter_particao():
    gerenciador = GerenciadorDeParticoes()
    particao_original = gerenciador.criar_particao("C:")
    particao_obtida = gerenciador.obter_particao("C:")
    assert particao_obtida == particao_original


def test_windows_pasta_duplicada():
    windows = Windows("Windows")
    windows.criar_pasta("Documentos")
    try:
        windows.criar_pasta("Documentos")
        assert False  # Não deveria chegar aqui
    except ValueError:
        assert True  # Esperado


def test_linux_pasta_duplicada():
    linux = Linux("Linux")
    linux.criar_pasta("home")
    try:
        linux.criar_pasta("home")
        assert False  # Não deveria chegar aqui
    except ValueError:
        assert True  # Esperado


def test_gerenciador_particao_duplicada():
    gerenciador = GerenciadorDeParticoes()
    gerenciador.criar_particao("C:")
    try:
        gerenciador.criar_particao("C:")
        assert False  # Não deveria chegar aqui
    except ValueError:
        assert True  # Esperado


def test_sistema_completo():
    # Teste de integração simples
    gerenciador = GerenciadorDeParticoes()
    
    # Windows
    particao_c = gerenciador.criar_particao("C:")
    windows = Windows("Windows")
    particao_c.associar_sistema_operacional(windows)
    windows.criar_pasta("Documentos")
    arquivo = Arquivo("teste.txt", 100)
    windows.adicionar_arquivo("Documentos", arquivo)
    
    # Linux
    particao_home = gerenciador.criar_particao("/home")
    linux = Linux("Linux")
    particao_home.associar_sistema_operacional(linux)
    linux.criar_pasta("Projetos")
    arquivo2 = Arquivo("codigo.py", 200)
    linux.adicionar_arquivo("Projetos", arquivo2)
    
    assert len(gerenciador.particoes) == 2
    assert windows.calcular_tamanho_total() == 100
    assert linux.calcular_tamanho_total() == 200
    
