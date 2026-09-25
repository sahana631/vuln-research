import random
import string
from vuln_target import parse_user_record

def random_input():
    length = random.randint(0, 20)
    charset = string.printable
    return "".join(random.choice(charset) for _ in range(length))

def fuzz(iterations=1000):
    crashes = []
    for i in range(iterations):
        test_input = random_input()
        try:
            parse_user_record(test_input)
        except Exception as e:
            crashes.append((test_input, type(e).__name__, str(e)))

if __name__ == "__main__":
    results = fuzz(1000)
    print(f"Run 1000 iterations, found {len(results)} crashes\n")
    for test_input, error_type, error_msg in results[:5]:
        print(f"Input: {test_input!r}")
        print(f"Error: {error_type}: {error_msg}\n")