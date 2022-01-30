def calculate_discount(amount: int, member: bool) -> float:
    if not isinstance(amount, int):
        raise ValueError("amount must be an int")
    if amount < 1 or amount > 10:
        raise ValueError("amount has to be greater than 0 and less or equal to 10")
    percentages = {(1, 2): 1.0, (3, 3): 3/4, (4, 5): 2/3, (6, 10): 1/2}
    for interval, percentage in percentages.items():
        if interval[0] <= amount <= interval[1]:
            if member:
                percentage *= 4 / 5
            return 1 - percentage
    raise RuntimeError("Logical error. Check implementation.")
