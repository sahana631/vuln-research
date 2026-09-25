# Vuln Research

A set of hands-on projects exploring vulnerability discovery and exploitation, built to understand the mechanics behind automated security tools (fuzzers, exploit validators) by building small, deliberately vulnerable code and breaking it myself.

## Project 1: Fuzzing (`vuln_target.py`, `mini_fuzzer.py`)

A small function that parses a comma-separated string (`name,age,email`) into a dict, originally written with no input validation. Paired with a custom-built fuzzer (Google's Atheris failed to build on macOS due to missing libFuzzer support in Apple Clang, so this implements the same discover-crash loop from scratch).

**What it found:** 1000 random inputs → 1000 crashes. Initial crash triage grouped by full error message, which misleadingly showed "90 unique crash types" — actually the same bug with different values embedded in the message. Fixing the triage to group by error type revealed the real picture: 2 distinct root causes (`IndexError` for malformed input, `ValueError` for non-numeric age field).

**The fix:** added explicit validation so both failure modes now raise one clean, intentional error instead of an unhandled exception.

Run it:
python mini_fuzzer.py


## Project 2: Command Injection (`vuln-ping.py`)

A small CLI tool that pings a hostname, built with a classic command injection flaw: it uses `shell=True` and inserts user input directly into a command string.

**The exploit:** entering `google.com; whoami` as the "hostname" ran an entirely separate command (`whoami`), leaking the local username. Real-world equivalent could run arbitrary destructive commands.

**The fix:** removed `shell=True` and passed the command as a list of arguments (`["ping", "-c", "1", hostname]`) instead of a string. The same injection input is now treated as one literal (invalid) hostname and fails safely, with no code execution.

Run it:
python vuln-ping.py


## Why this matters

Both projects follow the same loop: build something with a real, common vulnerability class, prove it's exploitable, fix it properly, then reverify the fix actually closes the gap. This mirrors (at a much smaller scale) the discover → validate → protect pipeline used by automated vulnerability research tools.

## Setup
python3 -m venv venv
source venv/bin/activate

No external dependencies — both projects use only the Python standard library.
