import java.util.Optional;
import java.util.Scanner;

class Node {

    private int value;
    private Node next;

    public Node(int value) {
        this.value = value;
        this.next = null;
    }

    public Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }

    public int value() {
        return value;
    }

    public Optional<Node> next() {
        return Optional.ofNullable(next);
    }

    public void setNext(Node next) {
        this.next = next;
    }
}

class LinkedList {

    private Node head;

    public LinkedList() {}

    public LinkedList(Node head) {
        this.head = head;
    }

    public Optional<Node> head() {
        return Optional.ofNullable(head);
    }

    public Optional<Node> get(int idx) {
        if (idx < 0) {
            return Optional.empty();
        }

        Optional<Node> node = Optional.ofNullable(head);

        for (int i = 0; i < idx && node.isPresent(); ++i) {
            node = node.get().next();
        }

        return node;
    }

    public Optional<Node> tail() {
        if (head == null) {
            return Optional.empty();
        }

        Node current = head;
        Optional<Node> next = current.next();

        while (next.isPresent()) {
            current = next.get();
            next = current.next();
        }

        return Optional.ofNullable(current);
    }

    public void clear() {
        head = null;
    }

    // - 1. Inserir número.
    public void append(Node node) {
        if (node == null) return;

        if (head().isEmpty()) {
            head = node;
            return;
        }

        Optional<Node> tail = this.tail();

        if (tail.isPresent()) {
            tail.get().setNext(node);
        }
    }

    // - 3. Pesquisar número.
    public int search(int value) {
        int pos = -1;
        Optional<Node> atual = head();

        while (atual.isPresent()) {
            Node cur = atual.get();
            pos++;

            if (cur.value() == value) {
                return pos;
            }

            atual = cur.next();
        }

        return -1;
    }
}

public class Exercicio1 {

    static final Scanner scanner = new Scanner(System.in);

    private static void pause() {
        System.out.println("[Enter] Ok");
        scanner.nextLine();
    }

    public static void clear() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private static int readInt(String message) {
        while (true) {
            try {
                System.out.print(message);
                return Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException _) {
                System.out.println("Digite um número válido.");
            }
        }
    }

    private static void fluxoInserir(LinkedList list) {
        int qtde = readInt("Digite a quantidade de números a inserir: ");

        for (int i = 0; i < qtde; ++i) {
            list.append(
                new Node(readInt("Digite o %dº número: ".formatted(i + 1)))
            );
        }

        System.out.println("Registros inseridos com sucesso!");
        pause();
    }

    private static void fluxoListar(LinkedList list) {
        Optional<Node> atual = list.head();

        if (atual.isEmpty()) {
            System.out.println("Nenhum registro inserido.");
            pause();
            return;
        }

        while (atual.isPresent()) {
            System.out.println(atual.get().value());
            atual = atual.get().next();
        }

        System.out.println("NULL");
        System.out.println();
        pause();
    }

    private static void fluxoPesquisa(LinkedList list) {
        int num = readInt("Digite o número para pesquisar: ");
        int index = list.search(num);

        if (index == -1) {
            System.out.println("Número não encontrado");
        } else {
            System.out.printf(
                "Número '%d' encontrado no índice '%d'.\n".formatted(num, index)
            );
        }

        pause();
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        int choice = 0;

        do {
            clear();
            choice = readInt(
                """
                Escolha uma opção:
                - 1. Inserir número.
                - 2. Listar números.
                - 3. Pesquisar número.
                - 4. Sair.
                >\s"""
            );
            clear();

            switch (choice) {
                case 1 -> fluxoInserir(list);
                case 2 -> fluxoListar(list);
                case 3 -> fluxoPesquisa(list);
                case 4 -> {
                }
                default -> {
                    System.out.println("Posição inválida");
                    pause();
                }
            }
        } while (choice != 4);
    }
}
