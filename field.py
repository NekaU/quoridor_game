def fill_the_field():
    field = []

    for row_index in range(9):
        if row_index != 8:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
            field.append([3 for i in range(17)])
        else:
            row_items = []
            for row_item_index in range(9):
                if row_item_index != 8:
                    row_items.append(0)
                    row_items.append(3)
                else:
                    row_items.append(0)
            field.append(row_items)
    return field


def print_field(field):
    num_horizontal = "     "
    counter = 0
    for item in field[0]:
        if counter < 10:
            num_horizontal += f"{counter}  "
            counter += 1
        else:
            num_horizontal += f"{counter} "
            counter += 1
    print(num_horizontal)

    num_horizontal = "     "
    counter = 0
    for item in field[0]:
        if item == 0 or item == 1 or item == 2:
            num_horizontal += f"{counter}"
            counter += 1
        else:
            num_horizontal += "     "
    print(num_horizontal)

    counter_1 = 0
    counter_2 = 0
    for row in field:
        if row[0] == 0 or row[0] == 1 or row[0] == 2:
            if counter_2 < 10:
                print(f"{counter_2}  {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1
            else:
                print(f"{counter_2} {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1

        else:
            if counter_2 < 10:
                print(f"{counter_2}   {row}")
                counter_2 += 1
            else:
                print(f"{counter_2}  {row}")
                counter_2 += 1


def field_preparation(field):
    center_real = backwards_calculating_point(5)
    field[0][center_real] = 2
    field[-1][center_real] = 1
    return field


def found_players(field):
    answer = {"first": [],
              "second": []}
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                answer['first'] = [i, j]
            if field[i][j] == 2:
                answer['second'] = [i, j]
    return answer


def get_connected_points(field):
    connected_points = []
    for i in range(0, len(field), 2):
        for j in range(0, len(field[i]), 2):
            if i != len(field) - 1 and j != len(field) - 1:
                if field[i][j + 1] == 3:
                    connected_points.append(
                        ((calculate_point(i), calculate_point(j)), (calculate_point(i), calculate_point(j + 2))))
                if field[i+1][j] == 3:
                    connected_points.append(
                        ((calculate_point(i), calculate_point(j)), (calculate_point(i + 2), calculate_point(j))))
            else:
                if i == len(field) - 1 and j != len(field) - 1:
                    if field[i][j + 1] == 3:
                        connected_points.append(
                            ((calculate_point(i), calculate_point(j)), (calculate_point(i), calculate_point(j + 2))))
                if j == len(field) - 1 and i != len(field) - 1:
                    if field[i + 1][j] == 3:
                        connected_points.append(
                            ((calculate_point(i), calculate_point(j)), (calculate_point(i + 2), calculate_point(j))))
    #print(connected_points)
    return connected_points


def calculate_point(point):
    return int(point/2)


def backwards_calculating_point(point):
    return point + (point - 2)


# final_field = field_preparation(fill_the_field())
# print_field(final_field)
# players = found_players(final_field)

# print(players)
