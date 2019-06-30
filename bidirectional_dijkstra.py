# Сам алгоритм Дейктсры
from heapq import heapify,heappop,heappush

class priority_queue():
    def __init__(self):
        self.queue = list() # Создаем список 
        heapify(self.queue) # Двоичная куча
        self.index = dict() # Создаем словарь с приоритетами
    def push(self,priority,label):
        if label in self.index:
            self.queue = [(w,l) for w,l in self.queue if l!= label] 
            heapify(self.queue)
        heappush(self.queue,(priority,label))
        self.index[label] = priority
    def pop(self):
        if self.queue:
            return heappop(self.queue)
    def __contains__(self, label):
        return label in self.index
    def __len__(self):
        return len(self.queue)


def dijkstra(graph,start,end):
    inf = float('inf')
    known = set() # Множество для сохранения путей которые мы просматривали
    priority = priority_queue()
    path = {start: start}
    for vertex in graph: # Проходимся по алгоритму
        if vertex == start:
            priority.push(0,vertex)
        else:
            priority.push(inf, vertex)
    last = start
    while last != end: # Первое не ровняется последнему 
        (weight, actual_node) = priority.pop() # Удаляем путь с которым мы работали и который в приоритете
        if actual_node not in known: # Пока путь с которым мы работаем не входит в мно-во лушчего пути
            for next_node in graph[actual_node]: # Прозодимся по след его путям
                upto_actual = priority.index[actual_node] # Мы ставим вначале приоритет на 1 путь
                upto_next = priority.index[next_node] # И берем значения следуйщих путей
                to_next = upto_actual +  graph[actual_node][next_node]# Получаем значения будушего пути
                if to_next < upto_next: # Сравниваем с другим будущим аутем
                    priority.push(to_next,next_node) # Если возможный приоритетные путь лучше то добавляем го
                    path[next_node] = actual_node # Добавляем его в переменную лучшего пути
            last = actual_node # Актуальная вершина становится точкой старта последуйщих обоходов
            known.add(actual_node) # Добавляем в наше множество путей которые мы просматривали
    return priority.index, path 