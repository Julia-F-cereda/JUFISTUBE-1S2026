from database.conexao import conectar
def recuperar_generos():
    conexao, cursor = conectar()

    #executado consulta genero
    cursor.execute("SELECT nome_genero, icone, cor FROM genero;")

    #recuperando os dados do genero
    generos = cursor.fetchall()

    #Fechando
    conexao.close()

    return generos