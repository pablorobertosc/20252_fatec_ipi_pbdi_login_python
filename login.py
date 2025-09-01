import psycopg
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    with psycopg.connect(
    host='localhost',
    port=5432,
    dbname='20252_fatec_ipi_pbdi_pablo_roberto',
    user='postgres',
    password='123456'
) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (f'{usuario.login}', f'{usuario.senha}')
            )
            result = cursor.fetchone()
            return result != None

def cadastrar(usuario):
    try:
        with psycopg.connect(
        host='localhost',
        port=5432,
        dbname='20252_fatec_ipi_pbdi_pablo_roberto',
        user='postgres',
        password='123456'
        ) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                'INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)',
                (usuario.login, usuario.senha)
                )
                conexao.commit() 
                print("Usuário cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar: {e}")

def menu():
    texto = '0-Sair\n1-Login\n2-Logoff\n3-Cadastrar novo usuário\n' 
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Digite seu login')
            senha = input('Digite sua senha')
            usuario = Usuario(login, senha)
            print("Usuário OK!" if existe(usuario) else "Usuário n OK")
        elif op == 2:
            usuario = None
            print('Logoff feito com sucesso')
        elif op == 3:
            print("--- Cadastro de Novo Usuário ---")
            login = input('Digite o login desejado: ')
            senha = input('Digite a senha desejada: ')
            novo_usuario = Usuario(login, senha)
            cadastrar(novo_usuario)
        else:
            print("Opção inválida. Tente novamente.")  
        op = int(input(texto))
    else:
        print('Até mais')

menu()