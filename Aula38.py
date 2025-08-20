# Aula Yield

def counter_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

contador = counter_function()

print(next(contador))
print(next(contador))
print(contador)
print(contador)
print(contador)