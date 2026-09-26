import subprocess

def ping_host(hostname: str) -> str:
    """Pings a hostname and returns the output."""
    result = subprocess.run(
        ["ping", "-c", "1", hostname],
        capture_output=True,
        text=True
    )
    print(f"Return code: {result.returncode}")
    print(f"Stdout: {result.stdout!r}")
    print(f"Stderr: {result.stderr!r}")
    return result.stdout

if __name__ == "__main__":
    host = input("Enter a hostname to ping: ")
    output = ping_host(host)