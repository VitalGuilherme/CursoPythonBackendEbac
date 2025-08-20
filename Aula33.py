# Aula instanciação de objetos.git log

# Nome -> Charizard
# Hp -> 450
# Tipo -> Fogo
# Ataque -> Lança Chamas 
# Peso -> 1500 kg

class MoldePokemon:
    def __init__(self, nome, altura, hp, tipo, ataque, peso):
        self.nome = nome
        self.altura = altura
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.peso = peso

    def mostrar_nome_pokemon(self):
        print(f"O nome do meu pokemon é: {self.nome}")

    def mostrar_altura_pokemon(self):
        print(f"A altura do meu pokemon é: {self.altura}")

    def mostrar_peso_pokemon(self):
        print(f"O peso do meu pokemon é: {self.peso}")

pikachu = MoldePokemon("Pikachu", 50, 15, 400, "Choque do trovão", "Elétrico")
charizard = MoldePokemon("Charizard", 200, 1500, 500, "Lança chamas", "Fogo")
miau = MoldePokemon("Miau", 50, 15, 100, "Unhada", "Terra")

pikachu.mostrar_nome_pokemon()
charizard.mostrar_nome_pokemon()
miau.mostrar_nome_pokemon()
