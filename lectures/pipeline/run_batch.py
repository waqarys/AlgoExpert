#!/usr/bin/env python3
"""Build many specs in parallel, skipping finished lectures. Usage: run_batch.py [-j 4] SPEC..."""
import subprocess, sys
from concurrent.futures import ThreadPoolExecutor
args = sys.argv[1:]; j = 4
if args[:1] == ["-j"]: j, args = int(args[1]), args[2:]
def one(f): subprocess.run([sys.executable, "make_lecture.py", "--skip-existing", f])
with ThreadPoolExecutor(j) as ex: list(ex.map(one, args))
