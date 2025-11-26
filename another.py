import sys
# Read scores from command line arguments
scores = list(map(int, sys.argv[1:]))
if not scores:
    print("No scores provided!")
    sys.exit(1)
print("Scores:", scores)
print("Maximum Score:", max(scores))
print("Minimum Score:", min(scores))
