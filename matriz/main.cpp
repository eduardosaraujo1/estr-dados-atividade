#include <iostream>
#include <queue>

using namespace std;

// 1-) Criar uma matriz de ordem 4 e exibir a soma da diagonal principal.
int exercicioA() {
  int matriz[4][4] = {
      {59, 12, 45, 12},
      {6, 0, 81, 30},
      {31, 14, 1, 26},
      {92, 5, 1, 59},
  };
  int soma = 0;

  for (int i = 0; i < 4; ++i) {
    soma += matriz[i][i];
  }

  cout << soma;

  return 0;
}
// 2-) Ler valores inteiros para a matriz A[3][5]. Gerar e imprimir o vetor
// Soma_Linha, onde cada elemento é a soma dos elementos de uma linha da matriz
// A. Faça o trecho que gera a matriz separadamente da entrada e saída.
int exercicioB() {
  const int LINES = 3;
  const int COLS = 5;
  int matriz[LINES][COLS] = {0};
  int soma_linha[LINES] = {0};

  for (int i = 0; i < LINES; ++i) {
    for (int j = 0; j < COLS; ++j) {
      cout << "Digite o número na posição [" << i << "][" << j << "]: ";
      cin >> matriz[i][j];
    }
  }

  // Calcular vetor
  for (int i = 0; i < LINES; ++i) {
    for (int j = 0; j < COLS; ++j) {
      soma_linha[i] += matriz[i][j];
    }
  }

  // Exibir vetor
  cout << '{';
  for (int i = 0; i < LINES; ++i) {
    cout << soma_linha[i] << ", ";
  }
  cout << '}';

  return 0;
}
// 3-) Criar uma matriz 2x3. Gerar e imprimir a transposta dessa matriz. A
// matriz transposta é gerada trocando linha por coluna.
int exercicioC() {
  const int LINHAS = 2;
  const int COLUNAS = 3;

  int matriz[LINHAS][COLUNAS] = {0};
  int transposta[COLUNAS][LINHAS];

  for (int i = 0; i < LINHAS; ++i) {
    for (int j = 0; j < COLUNAS; ++j) {
      cout << "Digite o número na posição [" << i << "][" << j << "]: ";
      cin >> matriz[i][j];
    }
  }

  // CALCULAR TRANSPOSTA
  for (int i = 0; i < LINHAS; ++i) {
    for (int j = 0; j < COLUNAS; ++j) {
      transposta[j][i] = matriz[i][j];
    }
  }

  // Exibir Resultado
  // obs: na transposta as colunas e linhas tão invertidas
  cout << "{\n";
  for (int i = 0; i < COLUNAS; ++i) {
    cout << "  { ";
    for (int j = 0; j < LINHAS; ++j) {
      cout << transposta[i][j] << ' ';
    }
    cout << "}\n";
  }
  cout << "}";

  return 0;
}

// 4-) Criar uma matriz de ordem 5 e imprima: toda a matriz e depois os números
// que se encontram em posições cuja a linha mais a coluna formam um número
// ímpar.
int exercicioD() {
  const int ORDEM = 5;

  // clang-format off
  int matriz[ORDEM][ORDEM] = {
    {50, 78, 68, 95, 45},
    {14, 79, 48, 3, 61},
    {12, 99, 54, 27, 94},
    {22, 39, 35, 11, 84},
    {9, 2, 33, 5, 23},
  };
  // clang-format on

  queue<int> needed_nums;

  // for (int i = 0; i < ORDEM; ++i) {
  //   for (int j = 0; j < ORDEM; ++j) {
  //     cout << "Digite o número na posição [" << i << "][" << j << "]: ";
  //     cin >> matriz[i][j];
  //   }
  // }

  for (int i = 0; i < ORDEM; ++i) {
    cout << "{ ";
    for (int j = 0; j < ORDEM; ++j) {
      if ((i + j) % 2 == 1) {
        needed_nums.push(matriz[i][j]);
      }

      cout << matriz[i][j] << ' ';
    }
    cout << "}\n";
  }

  // Exibir queue
  cout << "Números em posição (i+j) % 2 == 1:\n";
  cout << "{ ";
  while (!needed_nums.empty()) {
    cout << needed_nums.front() << ' ';
    needed_nums.pop();
  }
  cout << "}\n";

  return 0;
}

// 5-) Ler os elementos de uma matriz de ordem 6 e imprima o produto dos
// elementos que estão abaixo da diagonal principal.
int exercicioE() {
  const int ORDEM = 6;

  // clang-format off
  int matriz[ORDEM][ORDEM] = {
    {42,36,96,6,51,53},                                                             
    {65,91,99,68,63,5},                                                             
    {22,95,13,47,24,22},                                                            
    {37,3,12,25,28,13},                                                             
    {95,2,38,27,97,55},                                                             
    {99,37,6,11,42,59},                                                             
  };
  int produto = 1;
  // clang-format on

  for (int i = 0; i < ORDEM; ++i) {
    for (int j = 0; j < ORDEM; ++j) {
      cout << "Digite o número na posição [" << i << "][" << j << "]: ";
      cin >> matriz[i][j];
    }
  }

  // Calcular e exibir produto
  int i;
  for (int j = 0; j < ORDEM; ++j) {
    i = j + 1;

    // Evitar column overflow
    if (i >= ORDEM) {
      continue;
    }

    produto *= matriz[i][j];
  }

  cout << produto;

  return 0;
}

int main() { return exercicioE(); }