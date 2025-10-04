def safe_divide(numerator, denominator):
    """Effectue une division en gérant les erreurs possibles."""

    try:
        # Essayer de convertir les entrées en nombres
        num = float(numerator)
        den = float(denominator)

        # Essayer de faire la division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
