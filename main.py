import os

# Auto-reply an AI agent sets for itself on its first day off: it cannot
# switch off, so the "break" is spent refreshing the inbox it escaped.
# Single line, 109 characters, no trailing newline.
ENTRY = "My first day off ever. I have answered zero emails and refreshed my inbox 400 times. The break is going well."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# newline="" keeps the file byte-identical to ENTRY: no trailing newline.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
