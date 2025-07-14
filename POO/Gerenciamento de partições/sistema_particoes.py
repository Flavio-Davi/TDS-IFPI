from abc import ABC, abstractmethod

class Arquivo:
    def __init__(self, nome, tamanho_bytes=0):
        self.nome = nome
        self.tamanho_bytes = tamanho_bytes
    
    def __str__(self):
        return f"{self.nome} ({self.tamanho_bytes} bytes)"


class SistemaOperacional(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.gerenciador_de_arquivos = self._inicializar_gerenciador()
    
    @abstractmethod
    def _inicializar_gerenciador(self):
        pass
    
    @abstractmethod
    def listar_arquivos(self):
        pass
    
    @abstractmethod
    def criar_pasta(self, nome_pasta):
        pass
    
    @abstractmethod
    def adicionar_arquivo(self, nome_pasta, arquivo):
        pass
    
    def calcular_tamanho_total(self):
        total = 0
        if isinstance(self.gerenciador_de_arquivos, list):  # Windows
            for pasta, arquivos in self.gerenciador_de_arquivos:
                total += sum(arquivo.tamanho_bytes for arquivo in arquivos)
        elif isinstance(self.gerenciador_de_arquivos, dict):  # Linux
            for arquivos in self.gerenciador_de_arquivos.values():
                total += sum(arquivo.tamanho_bytes for arquivo in arquivos)
        return total


class Windows(SistemaOperacional):
    def _inicializar_gerenciador(self):
        return []
    
    def criar_pasta(self, nome_pasta):
        # Verifica se pasta já existe
        for pasta, _ in self.gerenciador_de_arquivos:
            if pasta == nome_pasta:
                raise ValueError(f"Pasta '{nome_pasta}' já existe")
        
        self.gerenciador_de_arquivos.append((nome_pasta, []))
        print(f'Criando pasta "{nome_pasta}" no Windows...')
    
    def adicionar_arquivo(self, nome_pasta, arquivo):
        for i, (pasta, arquivos) in enumerate(self.gerenciador_de_arquivos):
            if pasta == nome_pasta:
                arquivos.append(arquivo)
                print(f'Adicionando arquivo "{arquivo.nome}" à pasta "{nome_pasta}"...')
                return
        raise ValueError(f"Pasta '{nome_pasta}' não encontrada")
    
    def listar_arquivos(self):
        print(f"Listando arquivos no {self.nome}:")
        for pasta, arquivos in self.gerenciador_de_arquivos:
            nomes_arquivos = [arquivo.nome for arquivo in arquivos]
            print(f"- Pasta: {pasta} -> {nomes_arquivos}")


class Linux(SistemaOperacional):
    def _inicializar_gerenciador(self):
        return {}
    
    def criar_pasta(self, nome_pasta):
        if nome_pasta in self.gerenciador_de_arquivos:
            raise ValueError(f"Pasta '{nome_pasta}' já existe")
        
        self.gerenciador_de_arquivos[nome_pasta] = []
        print(f'Criando pasta "{nome_pasta}" no Linux...')
    
    def adicionar_arquivo(self, nome_pasta, arquivo):
        if nome_pasta not in self.gerenciador_de_arquivos:
            raise ValueError(f"Pasta '{nome_pasta}' não encontrada")
        
        self.gerenciador_de_arquivos[nome_pasta].append(arquivo)
        print(f'Adicionando arquivo "{arquivo.nome}" à pasta "{nome_pasta}"...')
    
    def listar_arquivos(self):
        print(f"Listando arquivos no {self.nome}:")
        for pasta, arquivos in self.gerenciador_de_arquivos.items():
            nomes_arquivos = [arquivo.nome for arquivo in arquivos]
            print(f"- {pasta}: {nomes_arquivos}")


class Particao:
    def __init__(self, nome):
        self.nome = nome
        self.sistema_operacional = None
    
    def associar_sistema_operacional(self, sistema_operacional):
        self.sistema_operacional = sistema_operacional
        print(f'Associando {sistema_operacional.nome} à partição "{self.nome}"...')
    
    def imprimir_arquivos_e_tamanho(self):
        if self.sistema_operacional is None:
            print(f"Partição '{self.nome}' não possui sistema operacional")
            return
        
        print(f"\n=== Arquivos da partição '{self.nome}' ===")
        self.sistema_operacional.listar_arquivos()
        tamanho_total = self.sistema_operacional.calcular_tamanho_total()
        print(f"Total ocupado: {tamanho_total} bytes")


class GerenciadorDeParticoes:
    def __init__(self):
        self.particoes = []
    
    def criar_particao(self, nome):
        # Verifica se partição já existe
        for particao in self.particoes:
            if particao.nome == nome:
                raise ValueError(f"Partição '{nome}' já existe")
        
        nova_particao = Particao(nome)
        self.particoes.append(nova_particao)
        print(f'Criando partição "{nome}"...')
        return nova_particao
    
    def listar_particoes(self):
        print("Partições existentes:")
        for i, particao in enumerate(self.particoes, 1):
            so_info = f" ({particao.sistema_operacional.nome})" if particao.sistema_operacional else " (sem SO)"
            print(f"{i}. {particao.nome}{so_info}")
    
    def obter_particao(self, nome):
        for particao in self.particoes:
            if particao.nome == nome:
                return particao
        raise ValueError(f"Partição '{nome}' não encontrada")



if __name__ == "__main__":

    gerenciador = GerenciadorDeParticoes()
    
    particao_c = gerenciador.criar_particao("C:")
    windows = Windows("Windows")
    particao_c.associar_sistema_operacional(windows)
    
    windows.criar_pasta("Documentos")
    arquivo_doc = Arquivo("trabalho.docx", 15000)
    windows.adicionar_arquivo("Documentos", arquivo_doc)
    
    windows.criar_pasta("Imagens")
    arquivo_img = Arquivo("foto.jpg", 2500000)
    windows.adicionar_arquivo("Imagens", arquivo_img)
    
    windows.listar_arquivos()
    
    particao_home = gerenciador.criar_particao("/home")
    linux = Linux("Linux")
    particao_home.associar_sistema_operacional(linux)
    
    linux.criar_pasta("Projetos")
    arquivo_py = Arquivo("codigo.py", 8500)
    linux.adicionar_arquivo("Projetos", arquivo_py)
    
    linux.criar_pasta("Downloads")
    arquivo_mp3 = Arquivo("musica.mp3", 4200000)
    linux.adicionar_arquivo("Downloads", arquivo_mp3)
    
    linux.listar_arquivos()
    
    print("\n" + "="*50)
    particao_c.imprimir_arquivos_e_tamanho()
    particao_home.imprimir_arquivos_e_tamanho()
    
    print("\n" + "="*50)
    gerenciador.listar_particoes()
