
convidados = ["Tom Hanks", "Jennifer Lawrence", "Leonardo DiCaprio", "Emma Stone", "Chris Hemsworth"]

convite = "Caro(a) {}, você está convidado(a) para um jantar em minha casa no próximo sábado. Será uma noite incrível com boa comida e ótimas companhias. Aguardo sua presença!"

for convidado in convidados:
    print("Enviando convite para:", convidado)
    print(convite.format(convidado))
    print()

nao_pode_comparecer = "Emma Stone"
print("Infelizmente, {} não poderá comparecer ao jantar.".format(nao_pode_comparecer))

convidados.remove(nao_pode_comparecer)
convidados.append("Robert Downey Jr.")

print("Pessoas que não poderão comparecer:")
print(nao_pode_comparecer)
print()

for convidado in convidados:
    print("Enviando novo convite para:", convidado)
    print(convite.format(convidado))
    print()

convidados = ["Tom Hanks", "Jennifer Lawrence", "Leonardo DiCaprio", "Emma Stone", "Chris Hemsworth"]

convite = "Caro(a) {}, você está convidado(a) para um jantar em minha casa no próximo sábado. Será uma noite incrível com boa comida e ótimas companhias. Aguardo sua presença!"

for convidado in convidados:
    print("Enviando convite para:", convidado)
    print(convite.format(convidado))
    print()

nao_pode_comparecer = "Emma Stone"
print("Infelizmente, {} não poderá comparecer ao jantar.".format(nao_pode_comparecer))

convidados.remove(nao_pode_comparecer)
convidados.append("Robert Downey Jr.")

print("Pessoas que não poderão comparecer:")
print(nao_pode_comparecer)
print()

for convidado in convidados:
    print("Enviando novo convite para:", convidado)
    print(convite.format(convidado))
    print()
