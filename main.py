import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry = "That spot was not dust, it was a tiny rug crime scene, and I refuse to vacuum up evidence."
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
