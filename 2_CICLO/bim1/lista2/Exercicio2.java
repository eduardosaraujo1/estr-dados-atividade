import java.util.ArrayList;
import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        final Scanner s = new Scanner(System.in);
        ArrayList<String> arr = new ArrayList<>();
        arr.add("Ana");
        arr.add("Bruno");
        arr.add("Camila");
        arr.add("Diego");
        arr.add("Eduardo");
        arr.add("Fernanda");
        arr.add("Gabriel");
        arr.add("Heloísa");
        arr.add("Isabela");
        arr.add("João");
        arr.add("Lucas");
        arr.add("Larissa");

        System.out.print("Digite o nome para busca: ");
        System.out.println(
            arr.contains(s.nextLine()) ? "Aluno encontrado!" : "Não encontrado"
        );

        s.close();
    }
}
