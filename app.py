from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos

app = Flask(__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def pg_principal():

    musicas = recuperar_musicas()
    generos = recuperar_generos()



    return render_template("principal.html", musicas = musicas)


@app.route("/admin")
def pg_administracao():
    musicas = recuperar_musicas()
    generos = recuperar_generos()
    return render_template("administracao.html", musicas = musicas, generos = generos)


if __name__ == "__main__":
    app.run(debug=True)
