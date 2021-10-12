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


class Node:

    def __init__(self, data, indexloc=None):
        self.data = data
        self.index = indexloc


