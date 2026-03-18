void insert(int idx_src, int idx_dst, int *arr) {
  // Esse algorítmo não foi projetado para
  // quando o destino está a frente da fonte
  if (idx_src >= idx_dst)
    return;

  int tmp = arr[idx_src];
  for (int p = idx_src - 1; p >= idx_dst; --p) {
    arr[p] = arr[p + 1];
  }

  arr[idx_dst] = tmp;
}

void insertionsort(int *arr, int len) {
  // Comparar do segundo valor em diante e ir verificando qual número deve ser
  // trocado
  // 20, 50, 79, 46, 100, 76, 70, 11, 19, 10
  for (int i = 1; i < len; ++i) {
    for (int j = i - 1; j >= 0; --j) {
      if (arr[i] < arr[j]) {
        insert(i, j + 1, arr);
      }
    }
  }
}