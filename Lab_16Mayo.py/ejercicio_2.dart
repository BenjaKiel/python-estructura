import 'dart:math';

List<int> lista_1 = [3, 4, 7, 9, 8, 5, 1, 2, 5, 7];

List<int> lista_2 = List.generate(10, (index) => -Random().nextInt(5));
void main() {
  print('Lista 1: $lista_1');

  print('Lista 2: $lista_2');

  List<int> listaSumada = [];
  for (int i = 0; i < lista_1.length; i++) {
    listaSumada.add(lista_1[i] + lista_2[i]);
  }

  print('lista suma: $listaSumada');

  listaSumada.removeRange(6, 8);

  print('lista final: $listaSumada');
}
