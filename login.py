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
    
def menu():
  texto = '0-Sair\n1-Login\n2-Logoff\n'
  usuario = None
  op = int(input(texto))
  while op != 0:
    if op == 1:
      login = input('Digite seu login')
      senha = input('Digite sua senha')
      usuario = Usuario(login, senha)
      print(
        "Usuário OK!" if existe(usuario) else "Usuário n OK"
      )
    elif op == 2:
      usuario = None
      print('Logoff feito com sucesso')
    op = int(input(texto))
  else:
    print('Até mais')

menu()