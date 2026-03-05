from database.conexao import conectar
def inserir_usuario(nome: str, senha: str):
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO cadastro (nome, senha)
    VALUES(%s, %s)""", [nome, senha])
    conexao.commit()
    conexao.close()
    