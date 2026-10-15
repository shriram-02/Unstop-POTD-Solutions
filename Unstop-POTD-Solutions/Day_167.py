import sys
from bisect import bisect_left, insort

def main():
    input = sys.stdin.readline
    m = int(input())
    books = {}
    scores = []
    result = []

    for _ in range(m):
        query = list(map(int, input().split()))
        t = query[0]

        if t == 1:
            book_id, score = query[1], query[2]
            books[book_id] = score
            insort(scores, score)

        elif t == 2:
            book_id = query[1]
            score = books.pop(book_id)
            idx = bisect_left(scores, score)
            scores.pop(idx)

        else:
            threshold = query[1]
            result.append(str(bisect_left(scores, threshold)))

    print("\n".join(result))

if __name__ == "__main__":
    data = sys.stdin.read().split()
    if not data:
        sys.exit()

    it = iter(data)
    m = int(next(it))
    books = {}
    scores = []
    result = []

    for _ in range(m):
        t = int(next(it))

        if t == 1:
            book_id = int(next(it))
            score = int(next(it))
            books[book_id] = score
            insort(scores, score)

        elif t == 2:
            book_id = int(next(it))
            score = books.pop(book_id)
            idx = bisect_left(scores, score)
            scores.pop(idx)

        else:
            threshold = int(next(it))
            result.append(str(bisect_left(scores, threshold)))

    print("\n".join(result))