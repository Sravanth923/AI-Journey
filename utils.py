def clean_text(text: str) -> str:
    """
    Cleans input text by stripping whitespace and converting to lowercase.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    return text.strip().lower()
