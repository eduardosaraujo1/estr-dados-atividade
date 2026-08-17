# Desenvolva um pequeno sistema para controlar produtos de uma loja.
# Crie: ArrayList<String> produtos
# Menu:
# ===== MENU =====
# 1 - Adicionar produto
# 2 - Listar produtos
# 3 - Pesquisar produto
# 4 - Remover produto
# 5 - Sair
#
# Requisitos:
# Opção 1: Adicionar um produto.
# Opção 2: Mostrar todos os produtos.
# Opção 3: Pesquisar um produto pelo nome.
# Opção 4: Remover um produto.
# Opção 5: Encerrar o programa.
# Desafio: Utilize um while para manter o menu funcionando até o usuário escolher Sair.
import sys

def readInt():
    return int(input())

def readFloat():
    return float(input())

def clear():
    # os.system("clear")
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def pause(msg="Pressione qualquer tecla para continuar."):
    print(msg,end="")
    # Windows implementation
    if sys.platform == "win32":
        import msvcrt
        # getwch handles unicode characters and returns a string
        return msvcrt.getwch()
        
    # Linux and macOS implementation
    else:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Switch the terminal out of 'line-buffered' mode
            tty.setcbreak(fd)
            return sys.stdin.read(1)
        finally:
            # Always restore the original terminal settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def addProduct(products: list(str)):
    products.append(input("Digite o nome do produto a adicionar: "))
    pause()

def removeProduct(products: list(str)):
    products.remove(input("Digite o nome do produto a remover: "))
    pause()

def showProducts(products: list(str)):
    print('\n'.join(products))
    pause()

def searchProduct(products: list(str)):
    key = input("Digite o nome do produto: ")
    print("Posição: ", products.index(key))
    pass

def showUI() -> int:
    MAX_NUM = 5;

    clear()
    print("""# ===== MENU =====
    1 - Adicionar produto
    2 - Listar produtos
    3 - Pesquisar produto
    4 - Remover produto
    5 - Sair""")

    return min(MAX_NUM,max(1,readInt()))

def main():
    products: list(str) = []

    while True:
        opt = showUI()
        match(opt):
            case 1:
                addProduct(products)
                break
            case 2:
                showProducts(products)
                break
            case 3:
                searchProduct(products)
                break
            case 4:
                removeProduct(products)
                break
            case 5:
                exit()
                break

if __name__ == '__main__':
    main()
