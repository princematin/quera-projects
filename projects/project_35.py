def check_words(text: str) -> dict[str, int]:
    ready_str = text.split()
    good_words = dict()
    for item in ready_str:
        clean_word = ''
        count = 0
        for j in item:
            if 'a' <= j <= 'z' or 'A' <= j <= 'Z':
                count += 1
                clean_word += j
        bad_word = len(item) - count
        if bad_word * 2 >= len(item):
            continue
        clean_word = clean_word.title()
        if clean_word not in good_words:
            good_words[clean_word] = 0
        good_words[clean_word] +=1 
    good_words = dict(sorted(good_words.items()))
    return good_words

print(check_words("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))