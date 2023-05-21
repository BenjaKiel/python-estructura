import 'dart:math';
  List<int> listaA = [4, 3, 2, 2, 1];
  List<int> listaB = [-3, 2, 8, 0, 1];

  List<int> resultado = multiplicarListas(listaA, listaB);
  List<int> nuevaLista = generarListaAleatoria(5, -5, -1);

  List<int> listaConcatenada = [...resultado, ...nuevaLista];
void main() {


  listaConcatenada.sort((a, b) => b.compareTo(a));

  print("Resultado: $listaConcatenada");
}


List<int> multiplicarListas(List<int> listaA, List<int> listaB) {
  List<int> resultado = [];
  
  for (int i = 0; i < listaA.length; i++) {
    resultado.add(listaA[i] * listaB[i]);
  }

  return resultado;
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
