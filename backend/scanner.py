import os
import re
import json

# -----------------------------
# Secret detection rules
# -----------------------------
SECRET_PATTERNS = {
    "aws_access_key": r"AKIA[0-9A-Z]{16}",
    "aws_secret_key": r"(?i)aws(.{0,20})?['\"][0-9a-zA-Z/+]{40}['\"]",
    "github_token": r"ghp_[A-Za-z0-9]{36}",
    "openai_key": r"sk-[A-Za-z0-9]{20,}",
    "private_key": r"-----BEGIN PRIVATE KEY-----",
    "jwt": r"eyJ[A-Za-z0-9_-]+?\.[A-Za-z0-9_-]+?\.[A-Za-z0-9_-]+",
    "password_inline": r"password\s*=\s*['\"].+?['\"]"
}

# -----------------------------
# Files/folders to ignore
# -----------------------------
IGNORE_PATHS = [
    ".git",
    "node_modules",
    ".png",
    ".jpg",
    ".jpeg",
    ".exe",
    "scanner.py",   # IMPORTANT: prevent self-scanning
]

def is_ignored(file_path: str) -> bool:
    """Check if file should be ignored."""
    lower_path = file_path.lower()
    return any(ignore.lower() in lower_path for ignore in IGNORE_PATHS)


# -----------------------------
# Scan a single file
# -----------------------------
def scan_file(file_path):
    findings = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, start=1):
            for secret_type, pattern in SECRET_PATTERNS.items():
                if re.search(pattern, line):
                    findings.append({
                        "type": "secret",
                        "secret_type": secret_type,
                        "file": file_path,
                        "line": i,
                        "content": line.strip(),
                        "severity": "critical"
                    })

    except Exception as e:
        return [{
            "error": str(e),
            "file": file_path
        }]

    return findings


# -----------------------------
# Scan directory recursively
# -----------------------------
def scan_directory(path):
    all_findings = []

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip unwanted files
            if is_ignored(file_path):
                continue

            all_findings.extend(scan_file(file_path))

    return all_findings


# -----------------------------
# CLI entry point
# -----------------------------
if __name__ == "__main__":
    target = input("Enter directory to scan: ").strip()

    results = scan_directory(target)

    print("\n=== SENTINELIQ SCAN RESULTS ===\n")
    print(json.dumps(results, indent=2))