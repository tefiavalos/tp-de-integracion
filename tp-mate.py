# También se podría hacer con bin, que es una función propia de python. 
# Quedaría así: print(bin(int(input("Ingresá un número: ")))[2:])
# Lo hacemos de ésta forma para mostrar el proceso que hay que hacer para pasar de decimal a binario
def decimalABinario(num, longitud=8):
    # En caso de ser 0 el binario es 0
    if num == 0: 
        return "0"

    # En caso de ser negativo usamos complemento a 2
    if num < 0:
        complemento_a_1 = ""
        # Necesitamos que sea positivo para hacer el proceso de traspaso de decimal a binario
        positivo = abs(num)

        # Hacemos las divisiones por 2 y vemos el resto para reconocer los bits que van a componer el número (como si el número fuera positivo)
        while positivo > 0:
            if positivo % 2 == 0:
                complemento_a_1 = "1" + complemento_a_1  # Complemento a 1: En este caso si fuera positivo sería 0, pero en complemento a 1 invertimos
            else:
                complemento_a_1 = "0" + complemento_a_1  # Complemento a 1: En este caso si fuera positivo sería 1, pero en complemento a 1 invertimos
            positivo = positivo // 2

        # Dependiendo de la cantidad de bits que queramos, agregamos unos (que en positivo serian 0) para completar los bits que faltan
        complemento_a_1 = "1" * (longitud - len(complemento_a_1)) + complemento_a_1 

        # Complemento a 2: sumamos 1 
        acarreo = 1 # empieza en 1 porque sumamos 1
        complemento_a_2 = ""
        for bit in reversed(complemento_a_1):  # Reversed para recorrer el complemento a 1 de derecha a izquierda
            # En este punto la suma funciona similar a la suma decimal salvo cuando es 1+1 que da 0 con acarreo de 1 (por eso el if)
            suma = int(bit) + acarreo 
            if suma == 2:
                complemento_a_2 = "0" + complemento_a_2
                acarreo = 1
            else:
                complemento_a_2 = str(suma) + complemento_a_2
                acarreo = 0
        
        # Si queda un acarreo al final, lo agregamos al principio del complemento_a_2
        if acarreo == 1:
            complemento_a_2 = "1" + complemento_a_2
        
        return complemento_a_2
    # Números positivos
    else:
        binario = ""
        # Dividimos por 2 hasta llegar a 0, si el resto es 0 ponemos 0 sino 1 (derecha a izquierda)
        while (num > 0): 
            if int(num) % 2 == 0:
                binario = "0" + binario
            else:
                binario = "1" + binario
            num = num // 2
    return binario

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