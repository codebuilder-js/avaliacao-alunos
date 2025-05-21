alunos = []

for _ in range(3):
    nome = input("Nome do aluno: ")
    email = input("E-mail: ")

    if "@" not in email or "." not in email:
        print("E-mail inválido. Ignorando aluno.")
        continue

    notas = []

    for i in range(3):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    media = sum(notas) / 3

    alunos.append({"nome": nome, "media": media})

print("\nAnálise de desempenho:")

for aluno in alunos:
    match aluno["media"]:
        case m if m >= 9:
            status = "Excelente"
        case m if m >= 7:
            status = "Bom"
        case m if m >= 5:
            status = "Regular"
        case _:
            status = "Insuficiente"
    
    print(f"{aluno['nome']} - Média: {aluno['media']:.1f} - Status: {status}")
