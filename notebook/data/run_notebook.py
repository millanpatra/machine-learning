"""Run MODEL TRAINING.ipynb code cells in order."""
import json
import os
import sys

# Run from notebook directory so stud.csv is found
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("MODEL TRAINING.ipynb", encoding="utf-8") as f:
    nb = json.load(f)

# Use non-interactive backend for matplotlib
import matplotlib
matplotlib.use("Agg")

globs = {}
for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] != "code":
        continue
    src = "".join(cell.get("source", []))
    if not src.strip():
        continue
    print(f"Running cell {i+1}...")
    try:
        exec(compile(src, f"<cell {i}>", "exec"), globs)
    except Exception as e:
        print(f"Cell {i+1} failed: {e}")
        sys.exit(1)

print("\nNotebook finished successfully.")
