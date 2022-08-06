import sys

def spelling_test(s, l):


def spelling_test_helper(s, l):



def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()
