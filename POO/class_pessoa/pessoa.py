class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, mae=None, estado="vivo", est_civil="solteiro"):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__est_civil = est_civil
        self.__mae = mae
        self.__pai = None
        self.__mae_adotiva = None
        self.__pai_adotivo = None
        self.__conjuge = None

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def estado(self):
        return self.__estado

    @property
    def est_civil(self):
        return self.__est_civil

    @property
    def conjuge(self):
        return self.__conjuge

    @property
    def mae_adotiva(self):
        return self.__mae_adotiva

   
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome


    def casar(self, parceiro):
        if self.__estado != "vivo":
            print(f"{self.__nome} está morto(a) e não pode casar.")
            return
        if parceiro.estado != "vivo":
            print(f"{parceiro.nome} está morto(a) e não pode casar.")
            return
        if self.__conjuge or self.__est_civil == "casado":
            print(f"{self.__nome} já está casado(a).")
            return
        if parceiro.conjuge or parceiro.est_civil == "casado":
            print(f"{parceiro.nome} já está casado(a).")
            return

        self.__conjuge = parceiro
        self.__est_civil = "casado"
        parceiro.__conjuge = self
        parceiro.__est_civil = "casado"
        print(f"{self.__nome} e {parceiro.nome} agora estão casados.")

  
    def morrer(self):
        if self.__estado == "morto":
            print(f"{self.__nome} já está morto(a).")
        else:
            self.__estado = "morto"
            if self.__conjuge:
                self.__conjuge.__conjuge = None
                self.__conjuge.__est_civil = "viúvo"
                self.__conjuge = None
            self.__est_civil = "falecido"
            print(f"{self.__nome} faleceu.")

   
    def divorciar(self):
        if self.__conjuge:
            ex = self.__conjuge
            self.__conjuge.__conjuge = None
            self.__conjuge.__est_civil = "divorciado"
            self.__conjuge = None
            self.__est_civil = "divorciado"
            print(f"{self.__nome} e {ex.nome} agora estão divorciados.")
        else:
            print(f"{self.__nome} não está casado(a).")

 
    def adocao(self, mae):
        if self.__mae is None and self.__mae_adotiva is None and self.__pai is None and self.__pai_adotivo is None:
            if mae.idade >= 18:
                self.__mae_adotiva = mae
                print(f"{mae.nome} adotou {self.__nome}.")
            else:
                print(f"{mae.nome} não tem idade suficiente para adotar.")
        else:
            print(f"{self.__nome} já tem responsáveis e não pode ser adotado.")

   
    def __str__(self):
        return (
            f"Nome: {self.__nome}\n"
            f"Idade: {self.__idade}\n"
            f"Peso: {self.__peso}\n"
            f"Altura: {self.__altura}\n"
            f"Sexo: {self.__sexo}\n"
            f"Estado: {self.__estado}\n"
            f"Estado Civil: {self.__est_civil}\n"
            f"Mãe biológica: {self.__mae.nome if self.__mae else 'Desconhecida'}\n"
            f"Mãe adotiva: {self.__mae_adotiva.nome if self.__mae_adotiva else 'Nenhuma'}\n"
            f"Cônjuge: {self.__conjuge.nome if self.__conjuge else 'Nenhum'}"
        )
