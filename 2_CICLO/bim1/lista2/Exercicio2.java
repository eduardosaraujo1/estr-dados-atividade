package org.example;

import java.util.ArrayList;
import java.util.Scanner;

public class App {

    public static void main(String[] args) {
        final Scanner s = new Scanner(System.in);
        ArrayList<String> arr = new ArrayList<>(
            List.of("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
        );

        // for (int i = 0; i < 10; ++i) {
        //     System.out.printf("Digite o %dº nome: ", i + 1);
        //     arr.add(s.nextLine());
        // }

        System.out.print("Digite o nome para busca: ");
        System.out.println(
            arr.contains(s.nextLine()) ? "Aluno encontrado!" : "Não encontrado"
        );
        s.close();
    }
}
