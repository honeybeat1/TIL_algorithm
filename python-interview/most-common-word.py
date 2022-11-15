def mostCommonWord(para, ban):
    table = para.maketrans('', '', ',.')
    para = para.translate(table)
    word_list = list(para.lower().split(' '))
    word_list = [w for w in word_list if w not in ban]
    print(word_list)

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    mostCommonWord(paragraph, banned)
