def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            return ["all"]
        else:
            return [-c / b]
    else:
        d = b**2 - 4 * a * c
        if d < 0:
            return []
        else:
            x1 = (-b + (d**0.5)) / (2 * a)
            x2 = (-b - (d**0.5)) / (2 * a)
            if abs(x1 - x2) < 1e-9:
                return [x1]
            else:
                result = sorted([x1, x2])  # Assign result here
                try:
                    return [int(x) for x in result]
                except (ValueError, TypeError):
                    return result  # Return original list if int conversion fails
