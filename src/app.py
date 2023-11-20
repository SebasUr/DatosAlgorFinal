from modules.Graph import Graph
from modules.Node import Node
from modules.Chat import Chat
import random, os
from flask import Flask, redirect
from flask import render_template
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/leaderboard")

@app.route("/leaderboard")
def main_app():
    filepath = os.path.join("src", "static", "graph.png")
    if os.path.exists(filepath):
        os.remove(filepath)

    graph_users = Graph()
    num_users = random.randint(5, 15) # Número random de usuarios entre 5 y 15
    # num_users = 30 # Número random de usuarios entre 5 y 15
    names = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofía", "Miguel", "Isabel", "Diego", "Elena", "Javier", "Carmen", "Francisco", "Luis", "Patricia", "Antonio", "Rosa", "José", "Lucía", "Raúl", "Silvia", "Manuel", "Victoria", "Fernando", "Eva", "Alberto", "Natalia", "Roberto", "Marta"]
    used_names = []
    # Se ingresan la cantidad de usuarios randoms al grafo
    for _ in range(num_users):
        name = random.choice(names)

        while name in used_names:
            name = random.choice(names)
        
        graph_users.add_node(Node(name))
        used_names.append(name)


    # Se agregan las relaciones entre los usuarios existentes en el grafo
    visited_edges_set = set()
    nodes_list = list(graph_users.nodes.keys())
    for i in range(1, 25):
        # Intentamos seleccionar nodos diferentes al menos 5 veces
        for _ in range(5):
            node_a = random.choice(nodes_list)
            node_b = random.choice(nodes_list)

            # Verificamos que los nodos no sean iguales y que la relación no exista
            if node_a != node_b and frozenset([node_a, node_b]) not in visited_edges_set:
                break
        else:
            # Si el bucle for no se rompe (no encontramos nodos válidos), continuamos con la siguiente iteración
            continue

        # Crear el chat entre los dos usuarios
        filename = f"chat{i}.txt"
        filepath = os.path.join("src", "chats", filename)

        new_chat = Chat(node_a, node_b)
        new_chat.add_lines(filepath)

        # Hacer que la arista que conecta a los dos usuarios/nodos sea el chat
        graph_users.add_edge(node_a, node_b, new_chat)

        # Agregar la relación a la lista de relaciones ya existentes
        visited_edges_set.add(frozenset([node_a, node_b]))

    users_result = graph_users.get_nodes_with_most_edges()
    users_with_0_edges = graph_users.get_nodes_with_0_edges()

    filepath = os.path.join("src", "static")
    graph_users.save_graph(filepath)

    edges = graph_users.get_edges()
    result = {
        'popular_users': [users_result[0], users_result[2]],
        'top_3_users': enumerate(users_result[1]),
        'number_edges_top_3': users_result[3],
        'stronger_relationships': [relationship.weight for relationship in graph_users.get_strongest_edge()],
        'users_with_0_edges': users_with_0_edges,
        'edges': edges
    }

    return render_template("index.html", result=result)
    # return render_template("index.html")

    

if(__name__=="__main__"): 
    app.run(debug=True) 