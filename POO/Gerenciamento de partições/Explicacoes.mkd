# Conceitos de POO no Código de Gerenciamento de Partições

## Introdução
- **Código**: Um sistema com classes para arquivos, sistemas operacionais (Windows e Linux), partições e gerenciamento de partições.
- **Conceitos Explorados**: Classes, Encapsulamento, Herança, Polimorfismo e Abstração.
-  **Integrantes:** Italo Bruno, Flávio Davi, Marcos Renam (Grupo 3 - Trabalho 1) 
---

## Classes
- **Definição**: Definir os atributos (dados) e métodos (funções) que os objetos criados a partir dessa classe terão.
- **Exemplo no Código**:
  ```python
  class Arquivo:
      def __init__(self, nome, tamanho_bytes=0):
          self.nome = nome
          self.tamanho_bytes = tamanho_bytes
  ```
  ```python
  class SistemaOperacional(ABC):
      def __init__(self, nome):
          self.nome = nome
          self.gerenciador_de_arquivos = self._inicializar_gerenciador()
  ```
  ```python
  class Particao:
      def __init__(self, nome):
          self.nome = nome
          self.sistema_operacional = None
  ```
  ```python
  class GerenciadorDeParticoes:
      def __init__(self):
          self.particoes = []
  ```
- **Explicação**: As classes `Arquivo`, `SistemaOperacional`, `Particao` e `GerenciadorDeParticoes` definem objetos com atributos (ex.: `nome`, `tamanho_bytes`, `particoes`) e métodos para manipular arquivos e partições.

---

## Encapsulamento
- **Definição**: Restringe o acesso direto aos atributos de um objeto, usando métodos ou convenções (como `_` para atributos protegidos) para controlar a manipulação de dados.
- **Exemplo no Código**:
  ```python
  class SistemaOperacional(ABC):
      def __init__(self, nome):
          self.nome = nome
          self.gerenciador_de_arquivos = self._inicializar_gerenciador()  # Atributo protegido
  ```
  ```python
  class Particao:
      def __init__(self, nome):
          self.nome = nome
          self.sistema_operacional = None
    
      def associar_sistema_operacional(self, sistema_operacional):
          self.sistema_operacional = sistema_operacional  # Controle via método
  ```
- **Explicação**: O atributo `_inicializar_gerenciador` é protegido (convenção `_`), e o acesso a `sistema_operacional` em `Particao` é controlado pelo método `associar_sistema_operacional`, garantindo que a associação seja feita de forma controlada.

---

## Herança
- **Definição**: Permite que uma classe derivada herde atributos e métodos de uma classe base, promovendo reutilização de código.
- **Exemplo no Código**:
  ```python
  class SistemaOperacional(ABC):
      def __init__(self, nome):
          self.nome = nome
          self.gerenciador_de_arquivos = self._inicializar_gerenciador()
  ```
  ```python
  class Windows(SistemaOperacional):
      def _inicializar_gerenciador(self):
          return []
  ```
  ```python
  class Linux(SistemaOperacional):
      def _inicializar_gerenciador(self):
          return {}
  ```
- **Explicação**: As classes `Windows` e `Linux` herdam de `SistemaOperacional`, reutilizando o atributo `nome` e o método `calcular_tamanho_total`, enquanto implementam métodos específicos como `_inicializar_gerenciador`.

---

## Polimorfismo
- **Definição**: Permite que objetos de diferentes classes implementem o mesmo método de formas distintas, possibilitando comportamentos variados.
- **Exemplo no Código**:
  ```python
  class Windows(SistemaOperacional):
      def listar_arquivos(self):
          print(f"Listando arquivos no {self.nome}:")
          for pasta, arquivos in self.gerenciador_de_arquivos:
              nomes_arquivos = [arquivo.nome for arquivo in arquivos]
              print(f"- Pasta: {pasta} -> {nomes_arquivos}")
  ```
  ```python
  class Linux(SistemaOperacional):
      def listar_arquivos(self):
          print(f"Listando arquivos no {self.nome}:")
          for pasta, arquivos in self.gerenciador_de_arquivos.items():
              nomes_arquivos = [arquivo.nome for arquivo in arquivos]
              print(f"- {pasta}: {nomes_arquivos}")
  ```
- **Explicação**: O método `listar_arquivos` é implementado de forma diferente em `Windows` (usando lista de tuplas) e `Linux` (usando dicionário), mas ambos respondem à mesma chamada, demonstrando polimorfismo.

---

## Abstração
- **Definição**: Esconde detalhes de implementação, expondo apenas interfaces essenciais.
- **Exemplo no Código**:
  ```python
  from abc import ABC, abstractmethod

  class SistemaOperacional(ABC):
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
  ```
- **Explicação**: A classe `SistemaOperacional` é abstrata (herda de `ABC`) e define métodos abstratos (`_inicializar_gerenciador`, `listar_arquivos`, `criar_pasta`, `adicionar_arquivo`), forçando `Windows` e `Linux` a implementá-los.
