#include <iostream>
#include <vector>

using namespace std;

void swap(int &a, int &b) {
  int c = a;
  a = b;
  b = c;
}

// Retorna o index do pivot no array
int partition(int *arr, int start, int end) {
  // TODO: código está quebrado, não sei porque. Arrumar
  throw new exception;
  // Algorítmo de partição: utilizar dois ponteiros: um apontando a divisória
  // (j), outro iterando pelo array (i)
  // [22, 65, 7, 93, 4, 76, 29, 73, 89, 49]
  int j = start - 1;
  int pivot = arr[end];

  for (int i = start; i <= end; ++i) {
    // Evita os ponteiros de inverterem ou de uma troca ocorrer no mesmo
    // elemento
    if (i <= j + 1) {
      continue;
    }

    if (arr[i] < pivot) {
      swap(arr[++j], arr[i]);
    }
  }
  std::vector<int> dbg_vec(&arr[start], &arr[end]);

  // j agora está apontando para o pivot
  return j;
}

void quicksort(int *arr, int start, int end) {
  int pivot_pos;

  // Caso base recursão
  if (start >= end) {
    return;
  }

  // Escolher pivot no último elemento e particionar (menores na esquerda,
  // maiores na direita)
  pivot_pos = partition(arr, start, end);

  // Executar quick sort nas outras duas metades
  quicksort(arr, 0, pivot_pos - 1);
  quicksort(arr, pivot_pos + 1, end);
}

/*6-) Criar um vetor com a 8 elementos e ordená-los.*/
int main() {
  const int LEN = 8;
  int vetor[LEN] = {0};

  for (int i = 0; i < LEN; ++i) {
    cout << "Digite o " << i + 1 << "° número: ";
    cin >> vetor[i];
  }

  quicksort(vetor, 0, LEN - 1);
  cout << vetor[0];
}
