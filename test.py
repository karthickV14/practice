def demo(lst):
    result = []
    for element in lst:
        if isinstance(element, str) and any(char.isdigit() for char in element):
            result.append(element)
    print(result)

lst = ["apple", 123, "banana", "cherry2", "3grape"]
demo(lst)