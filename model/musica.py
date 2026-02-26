from database.conexao import conectar

def recuperar_musicas():
    #passo 1 e 2 fitos
    conexao, cursor = conectar()
     
     #executando a consulta       
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica") 

    #recuperando os dados
    musicas = cursor.fetchall()

    #fechando
    conexao.close()      

    return musicas         

def salvar_musica( cantor: str, duracao: str, nome: str,  imagem: str, genero: str,) -> bool:
    """ Esa função serve para salvar as musicas dentro da função, e o bool vai mostrar se deu ou nao certo"""
    try:
        conexao, cursor = conectar()

        cursor.execute("""INSERT INTO musica (cantor, duracao, nome, url_imagem, nome_genero) 
                    VALUES (%s, %s, %s, %s, %s)""", [cantor, duracao, nome, imagem, genero])

        conexao.commit()

      
        conexao.close()

        return True
    except Exception as erro:
        print(erro)
        return False
    
def excluir_musica(codigo):
    """essa função precisa apagar dados"""
    try:
        conexao, cursor = conectar()

        cursor.execute("DELETE FROM musica where codigo= %s",[codigo,])

        conexao.commit()

        
        conexao.close()
        return True
    except Exception as erro:
        print(erro)
        return False
    
def ativar_musica(codigo,ativo, ):
    """essa função vai ativar a musica que estiver desativada"""
    try:
        conexao, cursor = conectar()

        cursor.execute("UPDATE musica SET ativo= %s WHERE codigo= %s",[codigo,ativo,])

        conexao.commit()

        
        conexao.close()
        return True
    except Exception as erro:
        print(erro)
        return False



