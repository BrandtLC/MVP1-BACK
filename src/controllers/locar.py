from flask import make_response
from datetime import date

from src.server.instance import server

app, db = server.app, server.db


class Locar():

    @app.route('/locar/<livro_id>/<cliente_id>', methods=['PATCH'])
    def locar(livro_id, cliente_id):
        cursor = db.cursor()
        cursor.execute("UPDATE livros SET locado_por = %s, locado_em = %s WHERE id = %s",
                       (cliente_id, date.today(), livro_id))
        db.commit()

        response = make_response("")
        response.status_code = 200
        response.headers = {
            "Content-Type": "application/json",
            'Access-Control-Allow-Origin': '*',
        }
        return response

    @app.route('/retornar/<livro_id>', methods=['PATCH'])
    def retornar(livro_id):
        cursor = db.cursor()
        cursor.execute("UPDATE livros SET locado_por = %s, locado_em = %s WHERE id = %s",
                       (None, None, livro_id))
        db.commit()

        response = make_response("")
        response.status_code = 200
        response.headers = {
            "Content-Type": "application/json",
            'Access-Control-Allow-Origin': '*',
        }
        return response
