print("----------DICIONÁRIO ESCOLAR----------")
escola = {
    
}
for i in range(3):
    nome = input("qual é seu nome: ")
    nota1 = int(input("qual foi sua nota: "))
    notas += nota1
    escola[nome] = nota1
    media = notas/3
print(F"são essas pessoas ({nome}), essa são as notas dos alunos ({nota1}) e agora essa é a média da turma {media}")
