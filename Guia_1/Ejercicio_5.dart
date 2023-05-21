import 'dart:math';

  List<int> lista1 = generarListaAleatoria(7, 30, 100);
  List<int> lista2 = generarListaAleatoria(7, 30, 100);
  List<int> lista3 = generarListaAleatoria(7, 30, 100);


  double promedio1 = calcularPromedio(lista1);
  double promedio2 = calcularPromedio(lista2);
  double promedio3 = calcularPromedio(lista3);

void main() {


  List<double> listaPromedios = [promedio1, promedio2, promedio3];

  // PRINTS
  print("Lista 1: $lista1");
  print("Promedio de la lista 1: $promedio1");
  print("Lista 2: $lista2");
  print("Promedio de la lista 2: $promedio2");
  print("Lista 3: $lista3");
  print("Promedio de la lista 3: $promedio3");
  print("Lista de promedios: $listaPromedios");
}

List<int> generarListaAleatoria(int length, int min, int max) {
  Random random = Random();
  List<int> lista = [];

  for (int i = 0; i < length; i++) {
    int elemento = min + random.nextInt(max - min + 1);
    lista.add(elemento);
  }

  return lista;
}

double calcularPromedio(List<int> lista) {
  int suma = lista.reduce((a, b) => a + b);
  return suma / lista.length;
}
