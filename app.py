# from flask import Flask, jsonify,request  # Depois de instalado importar o Flask e o jsonify
# import json

# app = Flask(__name__)

# desenvolvedores = [
#
#     {'nome':'Rafael',
#      'habilidades':['Python','Flask']
#      },
#     {'nome': 'Adilson',
#      'habilidades':['PHP','Symfony']
#      }
# ]
#
# @app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE']) # Adicionando a rota atravez do decorador
# def desenvolvedor(id):
#     if request.method == 'GET':
#         try:
#             response = desenvolvedores[id]
#         except IndexError:
#             mensagem = 'Desenvolvedor de Id {} não existe' .format(id)
#             response = {'status':'erro', 'mensagem':mensagem}
#         except Exception:
#             mensagem = 'Erro desconhecido. Procure o desenvolvedor da API'
#             response = {'status': 'erro', 'mensagem': mensagem}
#         return jsonify(response)
#     elif request.method == 'PUT':
#         dados = json.loads(request.data)
#         desenvolvedores[id] = dados
#         return jsonify(dados)
#     elif request.method == 'DELETE':
#         desenvolvedores.pop(id)
#         return jsonify({'status':'sucesso', 'mensagem':'Registro excluído com sucesso!'})
#
# @app.route('/dev/', methods=['POST', 'GET'])
# def lista_desenvolvedores():
#     if request.method == 'POST':
#         dados = json.loads(request.data)
#         desenvolvedores.append(dados)
#         return jsonify({'status':'sucesso', 'mensagem':'Registro inserido com sucesso!'})
#     elif request.method == 'GET':
#         return jsonify(desenvolvedores)


# if __name__ == '__main__':
#    app.run()

