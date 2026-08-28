using System;

class Node
{
    private int value;
    private Node? next;

    public Node(int value)
    {
        this.value = value;
        this.next = null;
    }

    public Node(int value, Node? next)
    {
        this.value = value;
        this.next = next;
    }

    public int Value()
    {
        return value;
    }

    public Node? Next()
    {
        return next;
    }

    public void SetNext(Node? next)
    {
        this.next = next;
    }
}

class LinkedList
{
    private Node? head;

    public LinkedList()
    {
    }

    public LinkedList(Node head)
    {
        this.head = head;
    }

    public Node? Head()
    {
        return head;
    }

    public Node? Get(int idx)
    {
        if (idx < 0)
        {
            return null;
        }

        Node? node = head;

        for (int i = 0; i < idx && node is not null; ++i)
        {
            node = node.Next();
        }

        return node;
    }

    public Node? Tail()
    {
        if (head is null)
        {
            return null;
        }

        Node current = head;
        Node? next = current.Next();

        while (next is not null)
        {
            current = next;
            next = current.Next();
        }

        return current;
    }

    public void Clear()
    {
        head = null;
    }

    // 1. Inserir número.
    public void Append(Node? node)
    {
        if (node is null)
        {
            return;
        }

        if (head is null)
        {
            head = node;
            return;
        }

        Node? tail = Tail();

        if (tail is not null)
        {
            tail.SetNext(node);
        }
    }

    // 3. Pesquisar número.
    public int Search(int value)
    {
        int pos = -1;
        Node? current = head;

        while (current is not null)
        {
            pos++;

            if (current.Value() == value)
            {
                return pos;
            }

            current = current.Next();
        }

        return -1;
    }
}

class Program
{
    private static void Pause()
    {
        Console.WriteLine("[Enter] Ok");
        Console.ReadLine();
    }

    private static void Clear()
    {
        Console.Clear();
    }

    private static int ReadInt(string message)
    {
        while (true)
        {
            Console.Write(message);

            if (int.TryParse(Console.ReadLine(), out int value))
            {
                return value;
            }

            Console.WriteLine("Digite um número válido.");
        }
    }

    private static void FluxoInserir(LinkedList list)
    {
        int qtde = ReadInt("Digite a quantidade de números a inserir: ");

        for (int i = 0; i < qtde; ++i)
        {
            list.Append(
                new Node(
                    ReadInt($"Digite o {i + 1}º número: ")
                )
            );
        }

        Console.WriteLine("Registros inseridos com sucesso!");
        Pause();
    }

    private static void FluxoListar(LinkedList list)
    {
        Node? current = list.Head();

        if (current is null)
        {
            Console.WriteLine("Nenhum registro inserido.");
            Pause();
            return;
        }

        while (current is not null)
        {
            Console.WriteLine(current.Value());
            current = current.Next();
        }

        Console.WriteLine("NULL");
        Console.WriteLine();
        Pause();
    }

    private static void FluxoPesquisa(LinkedList list)
    {
        int num = ReadInt("Digite o número para pesquisar: ");
        int index = list.Search(num);

        if (index == -1)
        {
            Console.WriteLine("Número não encontrado");
        }
        else
        {
            Console.WriteLine(
                $"Número '{num}' encontrado no índice '{index}'."
            );
        }

        Pause();
    }

    public static void Main()
    {
        LinkedList list = new();
        int choice;

        do
        {
            Clear();

            choice = ReadInt(
                """
                Escolha uma opção:
                - 1. Inserir número.
                - 2. Listar números.
                - 3. Pesquisar número.
                - 4. Sair.
                >
                """
            );

            Clear();

            switch (choice)
            {
                case 1:
                    FluxoInserir(list);
                    break;

                case 2:
                    FluxoListar(list);
                    break;

                case 3:
                    FluxoPesquisa(list);
                    break;

                case 4:
                    break;

                default:
                    Console.WriteLine("Posição inválida");
                    Pause();
                    break;
            }
        }
        while (choice != 4);
    }
}
