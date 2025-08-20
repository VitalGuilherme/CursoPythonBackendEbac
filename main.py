#print("Hello World")

# 1. PIP
# 2. Poetry
# 3. Poetry-Plugin
# 4. "poetry init"
# 5. "poetry shell"
#loop = " "
#loop = input("Digite S para realizar outra operação, ou N para finalizar.")
#while loop == "S" and loop == "N":
    #loop = input("Digite S para realizar outra operação, ou N para finalizar.")
 #   if loop == "S":
  #      print("Digite o número da operação desejada:")
   # elif loop == "N":
    #    break

def process_data(data):
    processed_data = []
    for item in data:
        if isinstance(item, int) and item > 0:
            processed_data.append(item * 2)
        elif isinstance(item, str):
            processed_data.append(item.upper())
    return processed_data

data = [1, 'hello', -3, 'world', 5]
result = process_data(data)
print(result)
