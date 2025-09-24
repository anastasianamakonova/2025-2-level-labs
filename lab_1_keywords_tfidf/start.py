"""
Frequency-driven keyword extraction starter
"""

# pylint:disable=too-many-locals, unused-argument, unused-variable, invalid-name, duplicate-code
from json import load
from main import (
    clean_and_tokenize,
    remove_stop_words,
    calculate_frequencies,
    calculate_tf,
    calculate_tfidf,
    get_top_n
)

def main() -> None:
    """
    Launches an implementation.
    """
    with open("assets/Дюймовочка.txt", "r", encoding="utf-8") as file:
        target_text = file.read()
        tokens = clean_and_tokenize(target_text)
    with open("assets/stop_words.txt", "r", encoding="utf-8") as file:
        stop_words = file.read().split("\n")
        cleaned_tokens = remove_stop_words(tokens, stop_words)
        freq_dict = calculate_frequencies(cleaned_tokens)
        get_top_words = get_top_n(freq_dict, 5)
    with open("assets/IDF.json", "r", encoding="utf-8") as file:
        idf = load(file)
        tf = calculate_tf(freq_dict)
        tfidf = calculate_tfidf(tf, idf)
        top_10_tfidf = get_top_n(tfidf, 10)
        print(top_10_tfidf)
    with open("assets/corpus_frequencies.json", "r", encoding="utf-8") as file:
        corpus_freqs = load(file)
    result = cleaned_tokens
    assert result, "Keywords are not extracted"


if __name__ == "__main__":
    main()