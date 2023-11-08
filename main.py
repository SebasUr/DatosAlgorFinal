from modules.Graph import Graph
from modules.Node import Node
from modules.Chat import Chat
import random

if __name__ == "__main__":  
    graph_users = Graph()
    num_users = random.randint(5, 15) # Número random de usuarios entre 5 y 15
    names = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofía", "Miguel", "Isabel", "Diego", "Elena", "Javier", "Carmen", "Francisco", "Luis", "Patricia", "Antonio", "Rosa", "José", "Lucía", "Raúl", "Silvia", "Manuel", "Victoria", "Fernando", "Eva", "Alberto", "Natalia", "Roberto", "Marta"]
    
    used_names = []
    # Se ingresan la cantidad de usuarios randoms al grafo
    for _ in range(num_users):
        name = random.choice(names)

        while name in used_names:
            name = random.choice(names)
        
        graph_users.add_node(Node(name))
        used_names.append(name)

    visited_edges_list = []
    # Se agregan las relaciones entre los usuarios existentes en el grafo
    for i in range(1, 25):
        nodes_list = graph_users.nodes.keys()
        node_a = random.choice(list(nodes_list))
        node_b = random.choice(list(nodes_list))

        # Se verifica que los nodos no sean iguales o que la relación no exista
        while node_a == node_b or [node_a, node_b] in visited_edges_list or [node_b, node_a] in visited_edges_list:
            node_a = random.choice(list(nodes_list))
            node_b = random.choice(list(nodes_list))
        
        # Crear el chat entre los dos usuarios
        new_chat = Chat(node_a, node_b)
        new_chat.add_lines(f"./chats/chat{i}.txt")

        # Hacer que la arista que conecta a los dos usuarios/nodos sea el chat
        graph_users.add_edge(node_a, node_b, new_chat)

        # Agregar la relación a la lista de relaciones ya existentes
        visited_edges_list.append([node_a,node_b])
        visited_edges_list.append([node_b,node_a])

    graph_users.print_graph()

    print("\n", "-"*50)
    # Imprimir los usuarios/nodos con más amigos (Nodos con mayor grado)
    print("Usuario(s) con más amigos:")
    popular_users, top_3_users = graph_users.get_nodes_with_most_edges()
    for user in popular_users:
        print(f"   - {user}")
    
    # Imprimir el top 3 de usuarios/nodos con más amigos
    print("\n", "-"*50)
    print("Top 3 de usuarios con más amigos:")
    for i in range(len(top_3_users)):
        print(f"   {i+1}. {top_3_users[i]}")