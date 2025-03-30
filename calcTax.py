from typing import List, Optional


def calculate_tax(levels: List[List[Optional[float]]], salary: float) -> float:
    # T: O(n log n), S: O(1)
    # Sort levels based on income limit (handling None separately)
    levels.sort(key=lambda x: float("inf") if x[0] is None else x[0])

    tax = 0.0
    prev_limit = 0  # Tracks the lower bound of the tax bracket

    for limit, rate in levels:
        if limit is None or salary < limit:
            tax += (salary - prev_limit) * rate
            break
        else:
            tax += (limit - prev_limit) * rate
            prev_limit = limit  # Move to the next bracket

    return tax


# Example usage
levels = [[10000, 0.3], [20000, 0.2], [30000, 0.1], [None, 0.1]]

salary = 45000
tax = calculate_tax(levels, salary)
print(tax)  # Expected output: 10000*0.3 + 10000*0.2 + 10000*0.1 + 15000*0.1 = 8000
