from flask import make_response, jsonify, request

from src.server.instance import server

app, db = server.app, server.db


class Livros():

    @app.route('/livros', methods=['GET'])
    def get_livros():
        cursor = db.cursor()
        cursor.execute("SELECT l.id, l.titulo, l.editora, l.autor, l.ano, CONCAT(c.nome, ' ', c.sobrenome) as locador, l.locado_em FROM livros as l"
        + " left JOIN clientes as c"
        + " ON l.locado_por = c.id;")
        livros_tuple = cursor.fetchall()

        livros = list()
        for livro in livros_tuple:
            if livro[6] is None:
                locado_em = None
            else:
                locado_em = livro[6].strftime('%d/%m/%Y')

            livros.append(
                {
                    'id': livro[0],
                    'título': livro[1],
                    'editora': livro[2],
                    'autor': livro[3],
                    'ano': livro[4],
                    'locador': livro[5],
                    'locado_em': locado_em
                }
            )

        return make_response(
         jsonify(livros)
        )

    @app.route('/livros', methods=['POST'])
    def create_livro():
        livro = request.json
        cursor = db.cursor()
        cursor.execute("INSERT INTO livros (titulo, editora, autor, ano) "
        + "VALUES (%s, %s, %s, %s)", (livro['titulo'], livro['editora'], livro['autor'], livro['ano']))
        id = cursor.lastrowid
        db.commit()

        return make_response(
            jsonify(
                {
                  'id': id,
                  **livro
                }
            )
        )

    @app.route('/livros/<livro_id>', methods=['DELETE'])
    def delete_livro(livro_id):
        sql = 'DELETE FROM livros WHERE id = %s'
        cursor = db.cursor()
        cursor.execute(sql, (livro_id,))

        db.commit

        response = make_response("")
        response.status_code = 200
        response.headers = {
            "Content-Type": "application/json",
            'Access-Control-Allow-Origin': '*',
        }
        return response

