# Vuln Research — Custom Fuzzer
A small hands-on project exploring fuzzing and vulnerability discovery, built after Google's Atheris fuzzer failed to build on macOS (missing libFuzzer support in Apple Clang). Rather than spend hours building LLVM from source, this project implements a simple fuzzer from scratch to explore the same core concepts.

## What's here
**`vuln_target.py`**
A small function that parses a comma-separated string (`name,age,email`) into a dict. Originally written with no input validation, so it would crash on almost any malformed input.

**`mini_fuzzer.py`**
A basic random-input fuzzer:
- Generates random printable strings of varying length
- Feeds each one to `parse_user_record()`
- Catches and logs any exceptions raised
- Groups crashes to identify distinct root causes, not just raw crash count

## What it found
First run: 1000 random inputs → 1000 crashes.

Initial triage grouped crashes by full error message, which produced a misleading "90 unique crash types" — actually just the same bug (`int()` failing on non-numeric input) with a different value embedded in each message. Fixing the triage logic to group by error type alone revealed the real picture: only **2 distinct root causes**:

- `IndexError` — input didn't have exactly 3 comma-separated fields
- `ValueError` — the second field wasn't a valid integer

## The fix
Added explicit validation to `parse_user_record()`:
- Checks for exactly 3 fields before unpacking
- Validates the age field is numeric before converting

Result: all 1000 fuzzed inputs now raise a single, intentional, controlled `ValueError` instead of an unhandled internal exception. The function still rejects bad input — it just does so predictably instead of crashing.

## Why this matters
Unhandled exceptions from unvalidated input are a real vulnerability class — they can cause denial-of-service, leak internal implementation details via stack traces, or serve as a stepping stone to more serious bugs depending on what the crashing code actually does. This project is a minimal, from-scratch illustration of the discover → triage → fix → reverify loop that real vulnerability research tools (like fuzzers used in automated security scanning) apply at much larger scale.

## Setup
python3 -m venv venv
source venv/bin/activate
python mini_fuzzer.py

## Notes
- Atheris (Google's coverage-guided Python fuzzer) was the original plan, but failed to build on macOS due to missing libFuzzer support in Apple's bundled Clang. This custom fuzzer implements the same discover-crash-triage loop without that dependency.
