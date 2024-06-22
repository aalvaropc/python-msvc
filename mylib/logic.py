import wikipedia


def wiki(name="Java (programming language)", length=1):
    """Retrieves a summary of a Wikipedia article.

    Args:
        name (str, optional): The name of the Wikipedia article. Default is "Python (programming language)".
        length (int, optional): The number of sentences in the summary. Default is 1.

    Returns:
        str: Summary of the specified Wikipedia article with the given length.
    """

    return wikipedia.summary(name, length)
