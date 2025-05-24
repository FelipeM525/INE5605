from alimentos.alimento import Alimento
from avaliacoes.avaliacao import Avaliacao
from usuarios.model.cliente import Cliente
from usuarios.model.nutricionista import Nutricionista
from model.objetivo import Objetivo
from model.plano_alimentar import PlanoAlimentar
from refeicoes.refeicao import Refeicao


arroz = Alimento("Arroz", 130, 28, 0, 2)
frango = Alimento("Frango", 165, 0, 3, 31)
salada = Alimento("Salada", 20, 4, 0, 1)

almoco = Refeicao([arroz, frango], "Almoço")
almoco.adicionar_alimento(salada)

print(f" Calorias totais: {almoco.calorias_totais()} kcal")
print(f" Proteínas totais: {almoco.proteinas_totais()}g")

objetivo = Objetivo("Perda de peso", 5, 60)

nutri = Nutricionista("Dra. Ana", "ana@nutri.com", "password", "193.840.780-69", "Clínica Nutri+", "CRN-3: 88143/P", [])

cliente = Cliente("João", "joao@email.com", "password", "104.864.510-03", 30, "masculino", 75.0, 1.75, objetivo, [])


plano = PlanoAlimentar([almoco], nutri, cliente)
cliente.add_plano_alimentar(plano)


imc_cliente = cliente.calcular_imc()
tmb_cliente = cliente.calcular_tmb()
avaliacao1 = Avaliacao(cliente, nutri, "11/05/2021", imc_cliente, tmb_cliente)


nutri.adicionar_avaliacao(avaliacao1)


print(f" IMC de {cliente.nome}: {imc_cliente}")
print(f" TMB de {cliente.nome}: {tmb_cliente}")
print(f"Nutricionista {nutri.nome} avaliou {avaliacao1.cliente.nome} em {avaliacao1.data}")
print(f"IMC da avaliacao_1: {avaliacao1.imc}, TMB da avaliacao_1: {avaliacao1.taxa_mb} kcal")

