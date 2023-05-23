import 'dart:io';
import 'dart:math';

void main() {
  //a. La primera lista debe ser generada de forma aleatoria y tener 5 elementos
  List<int> lista_1 = ListaRandom(5);
  print('Lista random: $lista_1');

  //b. La segunda se debe ingresar por teclado (Debe tener 5 elementos enteros)
  List<int> lista_2 = ListaPorTeclado(
      5); //el nº 5 pide que se ingresen 5 elementos ¿¿¿¿enteros???
  print('Lista ingresada por teclado: $lista_2');

  //c. Concatenar las dos listas anteriores
  List<int> lista_Concatenada = [];
  lista_Concatenada.addAll(lista_1);
  lista_Concatenada.addAll(lista_2);
  print('Lista concatenada: $lista_Concatenada');

  // d. Insertar en la 7°,8° y 9° posición los elementos 14,20,7 (agregando todos
  //los elementos de una sola vez, utilizando un método en específico)
  lista_Concatenada.insertAll(6, [14, 20, 7]);
  print('Lista con elementos insertados: $lista_Concatenada');

  // Ordenar lista de forma descendente
  lista_Concatenada.sort((a, b) => b.compareTo(a));
  print('Lista ordenada de forma descendente: $lista_Concatenada');
}

List<int> ListaRandom(int cantidadElementos) {
  Random random = Random();
  List<int> lista = [];
  for (int i = 0; i < cantidadElementos; i++) {
    lista.add(random.nextInt(100)); // Genera números aleatorios entre 0 y 99
  }
  return lista;
}

List<int> ListaPorTeclado(int cantidadElementos) {
  List<int> lista = [];
  for (int i = 0; i < cantidadElementos; i++) {
    stdout.write('Ingrese el elemento ${i + 1}: ');
    int elemento = int.parse(stdin.readLineSync()!);
    lista.add(elemento);
  }
  return lista;
}
