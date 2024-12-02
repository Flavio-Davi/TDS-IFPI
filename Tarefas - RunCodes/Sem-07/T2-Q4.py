def signo(dia, mes):
    signos = {
        "Áries": "21/03 a 19/04",
        "Touro": "20/04 a 20/05",
        "Gêmeos": "21/05 a 21/06",
        "Câncer": "22/06 a 22/07",
        "Leão": "23/07 a 22/08",
        "Virgem": "23/08 a 22/09",
        "Libra": "23/09 a 22/10",
        "Escorpião": "23/10 a 21/11",
        "Sagitário": "22/11 a 21/12",
        "Capricórnio": "22/12 a 19/01",
        "Aquário": "20/01 a 18/02",
        "Peixes": "19/02 a 20/03"
    }

    data = f"{dia:02d}/{mes:02d}"  # Formata a data como dd/mm

    for key, value in signos.items():
        inicio, fim = value.split(" a ")
        dia_inicio, mes_inicio = int(inicio[:2]), int(inicio[3:5])
        dia_fim, mes_fim = int(fim[:2]), int(fim[3:5])

        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fim and dia <= dia_fim):
            return key
        if (mes_inicio > mes_fim) and (mes == mes_inicio or mes == mes_fim):
            if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fim and dia <= dia_fim):
                return key

    return "Data de nascimento fora do intervalo dos signos conhecidos."

# Leitura dos dados do usuário
userDia = int(input().strip())
userMes = int(input().strip())

# Impressão do signo
print(signo(userDia, userMes))
