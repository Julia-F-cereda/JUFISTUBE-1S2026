from database.conexao import conectar
def inserir_usuario(nome: str, senha: str):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO cadastro (nome, senha)
    VALUES(%s, %s)""", [nome, senha])
    conexao.commit()
    conexao.close()

def conferir_usuario(nome:str, senha:str) ->list:
    """Essa função verifica se o usuario esta cadastrado, se estiver ela vai retornar os dados dele."""
    try:
        conexao, cursor = conectar()
        cursor.execute(""" SELECT NOME, SENHA FROM CADASTRO WHERE NOME=%s AND SENHA=%s""", [nome, senha])
        usuario = cursor.fetchone()
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
    return False
        