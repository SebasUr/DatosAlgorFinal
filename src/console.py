from modules.Graph import Graph
from modules.Node import Node
from modules.Chat import Chat
import random, os

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


    # Se agregan las relaciones entre los usuarios existentes en el grafo
    visited_edges_set = set()
    nodes_list = list(graph_users.nodes.keys())
    num_nodes = len(nodes_list)
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
        new_chat = Chat(node_a, node_b)
        new_chat.add_lines(f"src\chats\chat{i}.txt")

        # Hacer que la arista que conecta a los dos usuarios/nodos sea el chat
        graph_users.add_edge(node_a, node_b, new_chat)

        # Agregar la relación a la lista de relaciones ya existentes
        visited_edges_set.add(frozenset([node_a, node_b]))

    graph_users.print_graph()

    # print("\n", "-"*50)
    # # Imprimir los usuarios/nodos con más amigos (Nodos con mayor grado)
    # print("Usuario(s) con más amigos:")
    # popular_users, top_3_users = graph_users.get_nodes_with_most_edges()
    # for user in popular_users:
    #     print(f"   - {user}")
    
    # # Imprimir el top 3 de usuarios/nodos con más amigos
    # print("\n", "-"*50)
    # print("Top 3 de usuarios con más amigos:")
    # for i in range(len(top_3_users)):
    #     print(f"   {i+1}. {top_3_users[i]}")

    # # Imprimir la relación más fuerte entre dos usuarios/nodos
    # print("\n", "-"*50)
    # print("Relación más fuerte entre dos usuarios:")
    # stronger_relationships = graph_users.get_strongest_edge()
    # for relationship in stronger_relationships:
    #     print(f"   - {relationship.weight}")
    
    # Imprimir los usuarios/nodos con 0 amigos (Nodos con grado 0)
    # print("\n", "-"*50)
    # print("Usuarios con 0 amigos:")
    # nodes_with_0_edges = graph_users.get_nodes_with_0_edges()
    # for node in nodes_with_0_edges:
    #     print(f"   - {node}")

    graph_users.print_graph()
    filepath = os.path.join("src", "static")

    graph_users.save_graph(filepath)