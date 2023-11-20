from modules.Node import Node

class Chat:
    def __init__(self, user1, user2):
        self.head = None
        self.tail = None
        self.size = 0
        self.user1 = user1
        self.user2 = user2
        self.indicators = [0, 0, 0, 0] # Love, hatred, work, school
        self.relationship = "Friends"
    
    def add_to_end(self, nodo):
        if self.head is None:
            self.head = self.tail = nodo
            self.size += 1
        else:
            self.tail.next = nodo
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.size += 1

    def remove_from_end(self):
        if self.head is None:
            print("Lista vacía")
        elif self.head.next is None:
            self.head = self.tail = None
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

    def analize_message(self, message):
        message = message.lower()
        if "love" in message or "kiss" in message or "hug" in message:
            self.indicators[0] += 1
        if "hate" in message or "kill" in message or "die" in message or "peace" in message:
            self.indicators[1] += 1
        if "work" in message or "job" in message or "money" in message or "salary" in message or "bussy" in message:
            self.indicators[2] += 1
        if "school" in message or "university" in message or "college" in message or "homework" in message or "study" in message:
            self.indicators[3] += 1

    def add_lines(self, archivo):
        with open(archivo, "r") as file:
            for line in file:
                new_message = Node(line.strip())
                self.analize_message(new_message.data)
                self.add_to_end(new_message)

        if (self.indicators[0] > 4 or self.indicators[1] > 4 or self.indicators[2] > 4 or self.indicators[3] > 4):
            if(self.indicators.index(max(self.indicators)) == 0):
                self.relationship = "Lovers"
            elif (self.indicators.index(max(self.indicators)) == 1):
                self.relationship = "Haters"
            elif (self.indicators.index(max(self.indicators)) == 2):
                self.relationship = "Coworkers"
            elif(self.indicators.index(max(self.indicators)) == 3):
                self.relationship = "Classmates"

    def print_list(self):
        if self.head is None:
            print("Lista vacía")
        else:
            aux = self.head
            while aux is not None:
                print(aux.data)
                aux = aux.next

    def __str__(self):
        return f"{self.user1} y {self.user2} se mandarón {self.size} mensajes"