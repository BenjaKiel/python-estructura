
def contar_vocales(palabra):
	contador = 0
	for letra in palabra:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

palabra = input("Ingrese una palabra: ")

cantidad = contar_vocales(palabra)

print(f"En la cadena '{palabra}'' hay {cantidad} vocales")