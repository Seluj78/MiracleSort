def miraclesort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    while not lst[0] <= min(lst[1:]):
        pass
    return [lst[0]] + miraclesort(lst[1:])
