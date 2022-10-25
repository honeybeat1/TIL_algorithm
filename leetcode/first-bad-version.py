def firstBadVersion(self, n: int) -> int:
    start = 1
    end = n
    while start < end :
        mid = (start + end) // 2
        if isBadversion(mid) == True:
            mid = end
        else:
            start = mid + 1
    return start
