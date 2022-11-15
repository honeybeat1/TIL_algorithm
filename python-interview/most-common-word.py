from collections import Counter

def mostCommonWord(para, ban):
    table = para.maketrans('', '', ',.')
    para = para.translate(table)
    word_list = [w for w in list(para.lower().split(' ')) if w not in ban]
    most_common_word = Counter(word_list).most_common(1)[0][0]
    return most_common_word

if __name__ == '__main__':
    PARA = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    print(mostCommonWord(PARA, banned))
