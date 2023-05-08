import 'dart:io';

void main() {
  print('Ingrese una números enteros:');
  String? input = stdin.readLineSync()!;
  List<String> strList = input.split(',');
  List<int> intLista = strList.map(int.parse).toList();

  int suma = 0;

  for (int numero in intLista) {
    suma += numero;
  }

  // Imprimir la suma de los elementos de la lista
  print('La suma de los números ingresados es: $suma');
}
