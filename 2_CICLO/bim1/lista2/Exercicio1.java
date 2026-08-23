import java.util.ArrayList;
import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        final Scanner s = new Scanner(System.in);
        ArrayList<String> arr = new ArrayList<>();

        for (int i = 0; i < 10; ++i) {
            System.out.printf("Digite o %dº nome: ", i + 1);
            arr.add(s.nextLine());
        }

        System.out.println("Alunos cadastrados:");

        for (String aluno : arr) {
            System.out.println(aluno);
        }

        s.close();
    }
}
