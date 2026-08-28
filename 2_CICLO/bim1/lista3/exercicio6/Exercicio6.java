import java.util.Optional;
import java.util.OptionalInt;
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

    public boolean isEmpty() {
        return head().isEmpty();
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

    public void prepend(Node node) {
        if (node == null) return;

        if (head().isEmpty()) {
            head = node;
            return;
        }

        node.setNext(head);
        head = node;
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

    public boolean remove(int num) {
        if (head == null) return false;

        if (head.value() == num) {
            head = head.next().orElse(null);
            return true;
        }

        Node previous = head;
        Optional<Node> current = head.next();

        while (current.isPresent()) {
            Node currentNode = current.get();

            if (currentNode.value() == num) {
                previous.setNext(currentNode.next().orElse(null));
                return true;
            }

            previous = currentNode;
            current = currentNode.next();
        }

        return false;
    }

    public int count() {
        int count = 0;

        Optional<Node> cur = head();

        while (cur.isPresent()) {
            ++count;
            cur = cur.get().next();
        }

        return count;
    }

    public OptionalInt min() {
        Optional<Node> cur = head();

        if (cur.isEmpty()) {
            return OptionalInt.empty();
        }

        int minimum = cur.get().value();
        cur = cur.get().next();

        while (cur.isPresent()) {
            int value = cur.get().value();

            if (value < minimum) {
                minimum = value;
            }

            cur = cur.get().next();
        }

        return OptionalInt.of(minimum);
    }

    public OptionalInt max() {
        Optional<Node> cur = head();

        if (cur.isEmpty()) {
            return OptionalInt.empty();
        }

        int maximum = cur.get().value();
        cur = cur.get().next();

        while (cur.isPresent()) {
            int value = cur.get().value();

            if (value > maximum) {
                maximum = value;
            }

            cur = cur.get().next();
        }

        return OptionalInt.of(maximum);
    }
}

public class Exercicio6 {

    static final Scanner scanner = new Scanner(System.in);

    private static void pause() {
        System.out.print("[Enter] Ok");
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

    private static void fluxoInserir(LinkedList list, boolean inserirInicio) {
        int qtde = readInt("Digite a quantidade de números a inserir: ");

        for (int i = 0; i < qtde; ++i) {
            Node n = new Node(
                readInt("Digite o %dº número: ".formatted(i + 1))
            );
            if (inserirInicio) {
                list.prepend(n);
            } else {
                list.append(n);
            }
        }

        System.out.println("Registros inseridos com sucesso!");
        pause();
    }

    private static void fluxoListar(LinkedList list) {
        if (list.isEmpty()) {
            System.out.println("Nenhum registro inserido.");
            pause();
            return;
        }

        Optional<Node> atual = list.head();

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

    private static void fluxoRemover(LinkedList list) {
        int num = readInt("Digite o número para remover: ");

        if (list.remove(num)) {
            System.out.println("Número removido com sucesso!");
        } else {
            System.out.println("Número não encontrado.");
        }

        pause();
    }

    private static void fluxoContar(LinkedList list) {
        System.out.println("Quantidade de registros: " + list.count());
        pause();
    }

    private static void fluxoExibirMaior(LinkedList list) {
        OptionalInt maximum = list.max();

        if (maximum.isPresent()) {
            System.out.println("Maior número: " + maximum.getAsInt());
        } else {
            System.out.println("A lista está vazia. Não há maior elemento.");
        }

        pause();
    }

    private static void fluxoExibirMenor(LinkedList list) {
        OptionalInt minimum = list.min();

        if (minimum.isPresent()) {
            System.out.println("Menor número: " + minimum.getAsInt());
        } else {
            System.out.println("A lista está vazia. Não há menor elemento.");
        }

        pause();
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        int choice = -1;

        do {
            clear();
            choice = readInt(
                """
                ================================
                LISTA ENCADEADA
                ================================
                1 - Inserir no início
                2 - Inserir no final
                3 - Exibir lista
                4 - Pesquisar elemento
                5 - Remover elemento
                6 - Contar elementos
                7 - Exibir maior valor
                8 - Exibir menor valor
                0 - Sair
                Escolha:\s"""
            );
            clear();

            switch (choice) {
                case 1 -> fluxoInserir(list, true);
                case 2 -> fluxoInserir(list, false);
                case 3 -> fluxoListar(list);
                case 4 -> fluxoPesquisa(list);
                case 5 -> fluxoRemover(list);
                case 6 -> fluxoContar(list);
                case 7 -> fluxoExibirMaior(list);
                case 8 -> fluxoExibirMenor(list);
                case 0 -> {
                }
                default -> {
                    System.out.println("Posição inválida");
                    pause();
                }
            }
        } while (choice != 0);
    }
}
