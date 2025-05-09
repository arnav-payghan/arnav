def count_words(text):
    word_list = text.strip("\"").split()
    return f"Word count: {len(word_list)}"
