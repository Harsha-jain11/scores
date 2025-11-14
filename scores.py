import sys
def main():
    # Option 1: scores provided as command-line arguments
    if len(sys.argv) > 1:
        try:
            scores = list(map(int, sys.argv[1:]))
        except ValueError:
            print("Error: All values must be integers.")
            return
    else:
        # Option 2: local testing (interactive input)
        user_input = input("Enter scores separated by spaces: ").strip()
        if not user_input:
            print("Error: No scores entered.")
            return
        try:
            scores = list(map(int, user_input.split()))
        except ValueError:
            print("Error: All values must be integers.")
            return
    if len(scores) == 0:
        print("Error: No scores provided.")
        return
    total = sum(scores)
    average = total / len(scores)
    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
if __name__ == "__main__":
    main()
