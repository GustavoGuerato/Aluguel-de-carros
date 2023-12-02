class Aluguel:
    def __init__(self):
        self.carros = {}

    def adicionar_carro(self, modelo, ano):
        self.carros[modelo] = {"ano": ano, "disponivel": True}

    def mostrar_carros_disponiveis(self):
        print('Esses são os carros dissponiveis')

        for modelo, info in self.carros.items():
            if info["disponivel"]:
                print(f"{modelo} ({info['ano']}) - Disponível")
            else:
                print(f'{modelo} ({info['ano']})- Não está disponivel')

    def alugar_carro(self, modelo):
        if modelo in self.carros:
            if self.carros[modelo]['disponivel']:
                self.carros[modelo]['disponível'] = False
                print(f'voce alugou o {modelo}({self.carros[modelo]['ano']})')
            else:
                print('esse carro está indisponível')
        else:
            print('Carro não localizado em nosso banco de dados')


if __name__ == "__main__":
    aluguel = Aluguel()

    aluguel.adicionar_carro("Toyota Corolla", 2022)
    aluguel.adicionar_carro("Honda Civic", 2021)
    aluguel.adicionar_carro("Ford Focus", 2020)

    while True:
        print("\nEscolha uma opção:")
        print("1. Mostrar carros disponíveis")
        print("2. Alugar um carro")
        print("3. Sair")

        escolha = input("Digite o número da opção: ")

        if escolha == "1":
            aluguel.mostrar_carros_disponiveis()
        elif escolha == "2":
            modelo = input("Digite o modelo do carro que deseja alugar: ")
            aluguel.alugar_carro(modelo)
        elif escolha == "3":
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")
