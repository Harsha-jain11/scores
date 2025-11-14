import sys

scores = list(map(int, sys.argv[1:]))

if not scores:
    print("No scores provided")
    exit(1)

print(scores)
print(sum(scores))
print(sum(scores) / len(scores))
