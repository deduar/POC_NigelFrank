# Helper (Jupyter-exported): performance baseline for clients.
import time
from src.pipeline.runner import run

for n in [1000, 100000]:
    # uses sample; scale via gen_data for large
    t0 = time.perf_counter()
    r = run()
    print(n, round(time.perf_counter() - t0, 3), "s", r["loaded"])