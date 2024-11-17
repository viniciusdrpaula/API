from flask import Blueprint, request, jsonify, render_template
from models.atividade import (AtividadeNaoEncontrada, listar_atividades, atividade_por_id, 
                              adicionar_atividade, atualizar_atividade, excluir_atividade)

atividades_blueprint = Blueprint('atividades', __name__)

# ROTA PARA OBTER A LISTA DE ATIVIDADES
@atividades_blueprint.route('/atividades', methods=['GET'])
def obter_lista_atividades():
    try:
        atividades = listar_atividades()
        return render_template("atividades/atividades.html", atividades=atividades)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ROTA PARA CRIAR UMA NOVA ATIVIDADE (FORMULÁRIO)
@atividades_blueprint.route('/atividades/adicionar', methods=['GET'])
def formulario_nova_atividade():
    return render_template('atividades/criarAtividade.html')

# ROTA PARA CRIAR UMA NOVA ATIVIDADE (ENVIO DO FORMULÁRIO)
@atividades_blueprint.route('/atividades', methods=['POST'])
def criar_atividade():
    dados_atividade = request.get_json()
    adicionar_atividade(dados_atividade)
    return jsonify({'message': 'Atividade criada com sucesso!'}), 201

# ROTA PARA ATUALIZAR UMA ATIVIDADE EXISTENTE
@atividades_blueprint.route('/atividades/<int:id_atividade>', methods=['PUT'])
def atualizar_atividade_existente(id_atividade):
    dados_novos = request.get_json()
    try:
        atualizar_atividade(id_atividade, dados_novos)
        return jsonify({'message': 'Atividade atualizada com sucesso!'})
    except AtividadeNaoEncontrada:
        return jsonify({'error': 'Atividade não encontrada'}), 404

# ROTA PARA EXCLUIR UMA ATIVIDADE EXISTENTE
@atividades_blueprint.route('/atividades/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade):
    try:
        excluir_atividade(id_atividade)
        return jsonify({'message': 'Atividade excluída com sucesso!'})
    except AtividadeNaoEncontrada:
        return jsonify({'error': 'Atividade não encontrada'}), 404
