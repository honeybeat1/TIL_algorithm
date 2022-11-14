# 투포인터
def reverseString(s):
    left, right = 0, len(s)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    stringList = ['h','e','l','l','o']
    reverseString(stringList)
    print(stringList)
