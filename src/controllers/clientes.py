from flask import make_response, jsonify, request

from src.server.instance import server

app, db = server.app, server.db


class Clientes():

	@app.route('/clientes', methods=['POST'])
	def create_cliente():
		cliente = request.json
		cursor = db.cursor()
		cursor.execute("INSERT INTO clientes (nome, sobrenome, telefone, cpf) "
		+ "VALUES (%s, %s, %s, %s)", (cliente['nome'], cliente['sobrenome'], cliente['telefone'], cliente['cpf']))
		id = cursor.lastrowid
		db.commit()
  
		return make_response(
			jsonify(
				{'id': id, **cliente}
			)
		)

	@app.route('/clientes', methods=['GET'])
	def get_clientes():

		cursor = db.cursor()
		cursor.execute('SELECT * FROM clientes;')
		cliente_tuple = cursor.fetchall()

		clientes = list()
		for cliente in cliente_tuple:
			clientes.append(
				{
					'id': cliente[0],
					'nome': cliente[1],
					'sobrenome': cliente[2],
					'telefone': cliente[3],
					'cpf': cliente[4]

				}
			)

		return make_response(
			jsonify(clientes)
		)

	@app.route('/clientes/<cliente_id>', methods=['DELETE'])
	def delete_cliente(cliente_id):
		sql = 'DELETE FROM clientes WHERE id = %s'
		cursor = db.cursor()
		cursor.execute(sql, (cliente_id,))

		db.commit

		response = make_response("")
		response.status_code = 200
		response.headers = {
			"Content-Type": "application/json",
			'Access-Control-Allow-Origin': '*',
		}
		return response
