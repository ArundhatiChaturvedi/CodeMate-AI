def review_code_as_senior(code,context=None):
    suggestions = []

    if "try:" in code and "except:" in code and "Exception" not in code:
        suggestions.append("Consider catching specific exceptions for clarity.")

    if "global" in code:
        suggestions.append("Avoid using global variables if possible.")

    if len(code.split('\n')) > 50:
        suggestions.append("Code too long — consider modularizing it.")

    if context:
        suggestions.append(f"Contextual tip: For {context}, optimize your data structures.")

    return suggestions if suggestions else ["Looks good! Consider peer review for minor improvements."]
