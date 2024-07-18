from flask import Flask,jsonify,request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET']) # Ruta del metodo GET
def get_todos():
    todos_text = jsonify(todos)
    return todos_text

@app.route('/todos', methods=['POST']) # Ruta del metodo POST
def add_new_todo():
    request_body = request.get_json(force=True)  # Forzar la decodificación JSON
    print("Incoming request with the following body", request_body)
    
    # Agregar el nuevo todo a la lista global todos
    todos.append(request_body)
    
    # Devolver la lista actualizada de todos
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])  # Ruta del método DELETE
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        del todos[position] # Eliminar el todo en la posición especificada
        return jsonify(todos), 200  # Devolver la lista actualizada de todos con código de estado 200 (OK)
    else:
        return jsonify({"error": "Index fuera de rango"}), 404  # Devolver un error si el índice está fuera de rango


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)