#Parte 1: Convertir numeros decimales a binarios

#funcion
def decimalABinario(num):
    if num == 0: 
        return "0"
    binario = ""
    while (num > 0): 
        if int(num) % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        num = num // 2
    return binario

# También se podría hacer con bin, que es una función propia de python. 
# Quedaría así: print(bin(int(input("Ingresá un número: ")))[2:])
# Lo hacemos de ésta forma para mostrar el proceso que hay que hacer para pasar de decimal a binario


#Parte 2: Operaciones Logicas 

num1 = int(input("Por favor ingrese un número decimal: "))
num2 = int(input("Por favor ingrese un número decimal: "))

#Imprime los binarios con la funcion decimalABinario

print(f"{num1} en binario es: {decimalABinario(num1)}")
print(f"{num2} en binario es: {decimalABinario(num2)}")

#El usuario elije la operacion logica

operacion = input("Que operacion logica quiere realizar? (AND, OR, XOR): ").upper() 

#agrego un bucle while para que sea valido lo que el usuario ingresa    
while operacion not in ["AND", "OR", "XOR"]:
    print("Operacion no valida. Intente nuevamente.")
    operacion = input("Que operacion logica quiere realizar? (AND, OR, XOR): ").upper()

if operacion == "AND":
    resultado = num1 & num2
elif operacion == "OR":
    resultado = num1 | num2
else: 
    resultado = num1 ^ num2 
    
#Parte 3: Imprime el resultado de la operacion 
print(f"Resultado en decimal: {resultado}")
print(f"Resultado en binario: {decimalABinario(resultado)}")
