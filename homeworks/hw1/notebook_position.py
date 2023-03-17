def notebook_pos(a1, b1, a2, b2):
    sides = []

    if a1 >= a2:
        if b1 >= b2:
            sides.append([a1 + a2, b1])
            sides.append([b1 + b2, a1])
            sides.append([a1 + b2, b1])
            sides.append([b1 + a2, a1])
        else:
            sides.append([a2 + a1, b2])
            sides.append([a2 + b1, b2])
            sides.append([b2 + b1, a1])
            if a2 >= b1:
                sides.append([b2 + a1, a2])
            else:
                sides.append([b2 + a1, b1])
    else:
        return notebook_pos(a2, b2, a1, b1)
    squares = [item[0] * item[1] for item in sides if item[0] * item[1] >= (a1 * b1 + a2 * b2)]
    for item in sides:
        if min(squares) == item[0] * item[1]:
            return ' '.join(map(str, item))


# a1, b1, a2, b2 = map(int, input().split())
# print(notebook_pos(a1, b1, a2, b2))
# print(notebook_pos(10, 2, 2, 10))
# print(notebook_pos(5, 7, 3, 2))
# print(notebook_pos(1, 1, 1, 2))
# print(notebook_pos(1, 2, 1, 2))
# print(notebook_pos(1, 2, 3, 4))
# print(notebook_pos(25, 13, 111, 12))
