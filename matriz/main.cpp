#include <iostream>

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

    for (int i=0; i<4; ++i) {
        soma += matriz[i][i];
    }

    cout << soma;

    return 0;
}
// 2-) Ler valores inteiros para a matriz A[3][5]. Gerar e imprimir o vetor Soma_Linha, onde cada elemento é a soma dos elementos de uma linha da matriz A. Faça o trecho que gera a matriz separadamente da entrada e saída.
// 3-) Criar uma matriz 2x3. Gerar e imprimir a transposta dessa matriz. A matriz transposta é gerada trocando linha por coluna.
// 4-) Criar uma matriz de ordem 5 e imprima: toda a matriz e depois os números que se encontram em posições cuja a linha mais a coluna formam um número ímpar.
// 5-) Ler os elementos de uma matriz de ordem 6 e imprima o produto dos elementos que estão abaixo da diagonal principal.


int main() {
    return exercicioA();
}