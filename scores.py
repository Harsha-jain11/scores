
# Main branch: Sum and Average of scores
def main():
    scores = list(map(int, input("Enter scores separated by spaces: ").split()))

    total = sum(scores)
    avg = total / len(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average score:", round(avg, 2))
if __name__ == "__main__":
    main()
