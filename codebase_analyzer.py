import os

def analyze_codebase(directory):
    summary = {"total_files": 0, "total_lines": 0, "python_files": 0, "duplicate_count": 0}
    seen_lines = set()

    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith(".py"):
                summary["python_files"] += 1
                summary["total_files"] += 1
                with open(os.path.join(root, f), 'r', encoding="utf-8", errors="ignore") as file:
                    lines = file.readlines()
                    summary["total_lines"] += len(lines)
                    for line in lines:
                        if line.strip() in seen_lines:
                            summary["duplicate_count"] += 1
                        else:
                            seen_lines.add(line.strip())
    return summary
