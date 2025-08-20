# Aula Decorators

def meu_decorators(func):
    def wrapper():
        print("Antes da execução da minha função!")
        func()
        print("Depois da minha execução da minha função!")
    return wrapper
@meu_decorators
def despedida():
    print("Tchau!")
@meu_decorators
def cheguei():
    print("Oiiii")


cheguei()
despedida()