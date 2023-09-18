def arrange_sentences(sentences: list) -> str:
    final_sentence = ""
    filtered_sentences = list(filter(lambda item: item != "", sentences))

    for i, sentence in enumerate(filtered_sentences):
        if i > 1:
            final_sentence += ","

        final_sentence += sentence

    return final_sentence
