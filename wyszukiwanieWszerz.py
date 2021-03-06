#from AlgorytmyGrafowe.implementacjaGrafu import implementacjaGrafu as implementacjaGrafu
from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' sprzedaje mango')
                return True
            else :
                search_queue += graph[person]
                searched.append(person)
    return None

graph = {}
graph["ty"] = ["alicja", "bartek", "cecylia"] 
graph["bartek"] = ["janusz", "patrycjam"] 
graph["alicja"] = ["patrycjam"] 
graph["cecylia"] = ["tamara", "jarek"] 
graph ["janusz"] = []
graph["patrycja"] = [] 
graph["tamara"] = [] 
graph["jarek"] = []

print(search('ty'))