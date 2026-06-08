def calculate_discount(total_before, current_order):
    if total_before >= 50000000:
        return 0.1

    if total_before + current_order >= 50000000:
        return 0.1

    return 0