def solution(box):
  total = box[0]
  result = [box[0]]
  for i in range(1, len(box)):
    total += box[i]
    tmp = total // (i + 1) + (1 if total % (i + 1) != 0 else 0)
    result.append(max(result[-1], tmp))
  return result[-1]
