def get_value(color):
    if color == "black":
        return 0
    elif color == "brown":
        return 1
    elif color == "red":
        return 2
    elif color == "orange":
        return 3
    elif color == "yellow":
        return 4
    elif color == "green":
        return 5
    elif color == "blue":
        return 6
    elif color == "violet":
        return 7
    elif color == "grey":
        return 8
    elif color == "white":
        return 9


first = input()
second = input()
third = input()

print(int(str(get_value(first)) + str(get_value(second)))
      * (10 ** get_value(third)))
