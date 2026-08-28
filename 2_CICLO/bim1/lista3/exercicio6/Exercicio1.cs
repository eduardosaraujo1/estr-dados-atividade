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

    public Node(int value, Node next)
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

        for (int i = 0; i < idx && node != null; ++i)
        {
            node = node.Next();
        }

        return node;
    }

    public Node? Tail()
    {
        if (head == null)
        {
            return null;
        }

        Node current = head;
        Node? next = current.Next();

        while (next != null)
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

    public bool IsEmpty()
    {
        return head == null;
    }

    public void Append(Node? node)
    {
        if (node == null)
        {
            return;
        }

        if (head == null)
        {
            head = node;
            return;
        }

        Node? tail = Tail();

        if (tail != null)
        {
            tail.SetNext(node);
        }
    }

    public void Prepend(Node? node)
    {
        if (node == null)
        {
            return;
        }

        if (head == null)
        {
            head = node;
            return;
        }

        node.SetNext(head);
        head = node;
    }

    public int Search(int value)
    {
        int pos = -1;
        Node? current = head;

        while (current != null)
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

    public bool Remove(int num)
    {
        if (head == null)
        {
            return false;
        }

        if (head.Value() == num)
        {
            head = head.Next();
            return true;
        }

        Node previous = head;
        Node? current = head.Next();

        while (current != null)
        {
            if (current.Value() == num)
            {
                previous.SetNext(current.Next());
                return true;
            }

            previous = current;
            current = current.Next();
        }

        return false;
    }

    public int Count()
    {
        int count = 0;
        Node? current = head;

        while (current != null)
        {
            ++count;
            current = current.Next();
        }

        return count;
    }

    public int? Min()
    {
        Node? current = head;

        if (current == null)
        {
            return null;
        }

        int minimum = current.Value();
        current = current.Next();

        while (current != null)
        {
            int value = current.Value();

            if (value < minimum)
            {
                minimum = value;
            }

            current = current.Next();
        }

        return minimum;
    }

    public int? Max()
    {
        Node? current = head;

        if (current == null)
        {
            return null;
        }

        int maximum = current.Value();
        current = current.Next();

        while (current != null)
        {
            int value = current.Value();

            if (value > maximum)
            {
                maximum = value;
            }

            current = current.Next();
        }

        return maximum;
    }
}

public class Exercicio6
{
    private static void Pause()
    {
        Console.Write("[Enter] Ok");
        Console.ReadLine();
    }

    public static void Clear()
    {
        Console.Clear();
    }

    private static int ReadInt(string message)
    {
        while (true)
        {
            try
            {
                Console.Write(message);
                return int.Parse(Console.ReadLine()!);
            }
            catch (FormatException)
            {
                Console.WriteLine("Digite um número válido.");
            }
        }
    }

    private static void FluxoInserir(LinkedList list, bool inserirInicio)
    {
        int qtde = ReadInt("Digite a quantidade de números a inserir: ");

        for (int i = 0; i < qtde; ++i)
        {
            Node n = new Node(
                ReadInt($"Digite o {i + 1}º número: ")
            );

            if (inserirInicio)
            {
                list.Prepend(n);
            }
            else
            {
                list.Append(n);
            }
        }

        Console.WriteLine("Registros inseridos com sucesso!");
        Pause();
    }

    private static void FluxoListar(LinkedList list)
    {
        if (list.IsEmpty())
        {
            Console.WriteLine("Nenhum registro inserido.");
            Pause();
            return;
        }

        Node? current = list.Head();

        while (current != null)
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

    private static void FluxoRemover(LinkedList list)
    {
        int num = ReadInt("Digite o número para remover: ");

        if (list.Remove(num))
        {
            Console.WriteLine("Número removido com sucesso!");
        }
        else
        {
            Console.WriteLine("Número não encontrado.");
        }

        Pause();
    }

    private static void FluxoContar(LinkedList list)
    {
        Console.WriteLine(
            "Quantidade de registros: " + list.Count()
        );

        Pause();
    }

    private static void FluxoExibirMaior(LinkedList list)
    {
        int? maximum = list.Max();

        if (maximum.HasValue)
        {
            Console.WriteLine("Maior número: " + maximum.Value);
        }
        else
        {
            Console.WriteLine(
                "A lista está vazia. Não há maior elemento."
            );
        }

        Pause();
    }

    private static void FluxoExibirMenor(LinkedList list)
    {
        int? minimum = list.Min();

        if (minimum.HasValue)
        {
            Console.WriteLine("Menor número: " + minimum.Value);
        }
        else
        {
            Console.WriteLine(
                "A lista está vazia. Não há menor elemento."
            );
        }

        Pause();
    }

    public static void Main()
    {
        LinkedList list = new LinkedList();
        int choice = -1;

        do
        {
            Clear();

            choice = ReadInt(
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
                Escolha:
                """
            );

            Clear();

            switch (choice)
            {
                case 1:
                    FluxoInserir(list, true);
                    break;

                case 2:
                    FluxoInserir(list, false);
                    break;

                case 3:
                    FluxoListar(list);
                    break;

                case 4:
                    FluxoPesquisa(list);
                    break;

                case 5:
                    FluxoRemover(list);
                    break;

                case 6:
                    FluxoContar(list);
                    break;

                case 7:
                    FluxoExibirMaior(list);
                    break;

                case 8:
                    FluxoExibirMenor(list);
                    break;

                case 0:
                    break;

                default:
                    Console.WriteLine("Posição inválida");
                    Pause();
                    break;
            }

        } while (choice != 0);
    }
}
