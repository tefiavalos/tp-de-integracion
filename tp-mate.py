# También se podría hacer con bin, que es una función propia de python. 
# Quedaría así: print(bin(int(input("Ingresá un número: ")))[2:])
# Lo hacemos de ésta forma para mostrar el proceso que hay que hacer para pasar de decimal a binario

numero = int(input("Por favor ingrese un número: "))


def decimalABinario(num):
    binario = ""
    while (num > 0): 
        if int(num) % 2 == 0:
            binario = "0" + str(binario)
        else:
            binario = "1" + str(binario)
        num = num // 2
    return binario


print(decimalABinario(numero))

