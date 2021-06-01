def first_and_last(message):
    if not message:
        return False
    a = (message[0])
    b = (message[-1])
    return a == b


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
print(first_and_last("enrique"))