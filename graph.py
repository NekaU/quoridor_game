from field import field_preparation, fill_the_field, get_connected_points, found_players, backwards_calculating_point, \
    calculate_point


class Node:

    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        # установка матрица смежности
        self.adj_mat = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    # Связывает node1 с node2
    # Обратите внимание, что ряд - источник, а столбец - назначение
    # Обновлен для поддержки взвешенных ребер (поддержка алгоритма Дейкстры)
    def connect_dir(self, node1, node2, weight=1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight

    # Опциональный весовой аргумент для поддержки алгоритма Дейкстры
    def connect(self, node1, node2, weight=1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    # Получает ряд узла, отметить ненулевые объекты с их узлами в массиве self.nodes
    # Выбирает любые ненулевые элементы, оставляя массив узлов
    # которые являются connections_to (для ориентированного графа)
    # Возвращает значение: массив кортежей (узел, вес)
    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if
                self.adj_mat[node][col_num] != 0]

    # Проводит матрицу к столбцу узлов
    # Проводит любые ненулевые элементы узлу данного индекса ряда
    # Выбирает только ненулевые элементы
    # Обратите внимание, что для неориентированного графа
    # используется connections_to ИЛИ connections_from
    # Возвращает значение: массив кортежей (узел, вес)
    def connections_to(self, node):
        node = self.get_index_from_node(node)
        column = [row[node] for row in self.adj_mat]
        return [(self.nodes[row_num], column[row_num]) for row_num in range(len(column)) if column[row_num] != 0]

    def print_adj_mat(self):
        for row in self.adj_mat:
            print(row)

    def node(self, index):
        return self.nodes[index]

    def remove_conn(self, node1, node2):
        self.remove_conn_dir(node1, node2)
        self.remove_conn_dir(node2, node1)

    # Убирает связь в направленной манере (nod1 к node2)
    # Может принять номер индекса ИЛИ объект узла
    def remove_conn_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = 0

        # Может пройти от node1 к node2

    def can_traverse_dir(self, node1, node2):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        return self.adj_mat[node1][node2] != 0

    def has_conn(self, node1, node2):
        return self.can_traverse_dir(node1, node2) or self.can_traverse_dir(node2, node1)

    def add_node(self, node):
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adj_mat:
            row.append(0)
        self.adj_mat.append([0] * (len(self.adj_mat) + 1))

    # Получает вес, представленный перемещением от n1
    # к n2. Принимает номера индексов ИЛИ объекты узлов
    def get_weight(self, n1, n2):
        node1, node2 = self.get_index_from_node(n1), self.get_index_from_node(n2)
        return self.adj_mat[node1][node2]

    # Разрешает проводить узлы ИЛИ индексы узлов
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(self, node):
        # Получает индекс узла (или поддерживает передачу int)
        node_num = self.get_index_from_node(node)
        # Заставляет массив отслеживать расстояние от одного до любого узла
        # в self.nodes. Инициализирует до бесконечности для всех узлов, кроме
        # начального узла, сохраняет "путь", связанный с расстоянием.
        # Индекс 0 = расстояние, индекс 1 = перескоки узла
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([self.nodes[node_num]])

        dist[node_num][0] = 0
        # Добавляет в очередь все узлы графа
        # Отмечает целые числа в очереди, соответствующие индексам узла
        # локаций в массиве self.nodes
        queue = [i for i in range(len(self.nodes))]
        # Набор увиденных на данный момент номеров
        seen = set()
        while len(queue) > 0:
            # Получает узел в очереди, который еще не был рассмотрен
            # и который находится на кратчайшем расстоянии от источника
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n

            # Добавляет мин. расстояние узла до увиденного, убирает очередь
            # print(queue)
            # print(min_node)
            queue.remove(min_node)
            seen.add(min_node)
            # Получает все следующие перескоки
            connections = self.connections_from(min_node)
            # Для каждой связи обновляет путь и полное расстояние от
            # исходного узла, если полное расстояние меньше
            # чем текущее расстояние в массиве dist
            for (node, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.index][0]:
                    dist[node.index][0] = tot_dist
                    dist[node.index][1] = list(dist[min_node][1])
                    dist[node.index][1].append(node)
        return dist


def create_graph(nodes):
    list_of_nodes = []
    for row in nodes:
        for node in row:
            list_of_nodes.append(node)
    graph = Graph.create_from_nodes(list_of_nodes)
    return graph


def create_nodes_from_field(field):
    nodes = []
    i = 0

    counter = 0
    for row in field:
        row_items = []
        j = 0
        for row_item in row:
            if row_item == 0 or row_item == 1 or row_item == 2:
                row_items.append(Node(f"{counter}"))
                j += 1
                counter += 1
        if row[:-1] == row[1:]:
            i += 1

        nodes.append(row_items)
    return [x for x in nodes if x != []]




def print_nodes(nodes):
    for row in nodes:
        print([node.data for node in row])


def create_connections(graph, nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != len(nodes) - 1 and j != len(nodes) - 1:
                graph.connect(nodes[i][j], nodes[i + 1][j])
                graph.connect(nodes[i][j], nodes[i][j + 1])
            else:
                if i == len(nodes) - 1 and j != len(nodes) - 1:
                    graph.connect(nodes[i][j], nodes[i][j + 1])
                if j == len(nodes) - 1 and i != len(nodes) - 1:
                    graph.connect(nodes[i][j], nodes[i + 1][j])

    return graph


def update_connections_from_field(connected_points, graph, nodes):
    for point in connected_points:
        graph.connect(nodes[point[0][0]][point[0][1]], nodes[point[1][0]][point[1][1]])
    return graph


def if_there_path_to_win(data):
    players = found_players(data['field'])
    first = [calculate_point(players['first'][0]), calculate_point(players['first'][1])]
    second = [calculate_point(players['second'][0]), calculate_point(players['second'][1])]
    win_for_first = [node.data for node in data['nodes'][0]]
    win_for_second = [node.data for node in data['nodes'][-1]]
    endpoints_for_first = get_all_endpoint(data['graph'], data['nodes'][first[0]][first[1]])
    endpoints_for_second = get_all_endpoint(data['graph'], data['nodes'][second[0]][second[1]])
    first_win_result = [i for i in endpoints_for_first if i in win_for_first]
    second_win_result = [i for i in endpoints_for_second if i in win_for_second]
    print(f"\n 111111111111 {first_win_result} 111111111 \n")
    print(f"\n 222222222222 {second_win_result} 2222222222 \n")
    if len(first_win_result) != 0 and len(second_win_result) != 0:
        return True
    else:
        return False


def get_all_roads(graph, start_node):
    roads = []
    for conn in [(weight, [n.data for n in node]) for (weight, node) in graph.dijkstra(start_node)]:
        roads.append(conn)
    return roads


def get_all_endpoint(graph, node):
    endpoints = []
    for road in get_all_roads(graph, node):
        endpoints.append(road[1][-1])
    return endpoints


# final_field = field_preparation(fill_the_field())
# nodes_final = create_nodes_from_field(final_field)
# graph_final = update_connections_from_field(get_connected_points(final_field), create_graph(nodes_final), nodes_final)
# print_nodes(nodes)
# graph.print_adj_mat()

# print(if_there_path_to_win(final_field, graph_final, nodes_final))

# print(graph.get_weight(nodes[0][4], nodes[8][4]))






