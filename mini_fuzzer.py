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
    return crashes

if __name__ == "__main__":
    results = fuzz(1000)
    print(f"Ran 1000 iterations, found {len(results)} crashes\n")

    unique_errors = {}
    for test_input, error_type, error_msg in results:
        key = error_type
        if key not in unique_errors:
            unique_errors[key] = (test_input, error_msg)

    print(f"Unique crash types: {len(unique_errors)}\n")
    for error_type, (example_input, error_msg) in unique_errors.items():
        print(f"{error_type}")
        print(f"  Example input: {example_input!r}")
        print(f"  Example message: {error_msg}\n")