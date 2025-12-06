def count_words(text):
    words = text.split()
    num_of_words = len(words)
    return num_of_words

def num_of_characters(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_dictionary(char_counts):
    results =[]
    for ch, count in char_counts.items():
        if not ch.isalpha():
            continue
        item = {"char": ch, "num": count}
        results.append(item)

    def sort_on(item):
        return item["num"]
    
    results.sort(reverse=True, key=sort_on)

    return results
