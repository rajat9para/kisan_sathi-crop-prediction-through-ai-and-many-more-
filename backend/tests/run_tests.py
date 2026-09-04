import sys
import os
import inspect
import time

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import test_services
import test_edge_services

def run_suite(module, name):
    print(f"\n==========================================")
    print(f"RUNNING SUITE: {name}")
    print(f"==========================================")
    funcs = [getattr(module, attr) for attr in dir(module) if attr.startswith("test_") and callable(getattr(module, attr))]
    passed = 0
    failed = 0
    start = time.time()
    for f in funcs:
        fn_name = f.__name__
        try:
            f()
            print(f"  [PASS] {fn_name}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {fn_name}: {e}")
            failed += 1
    duration = time.time() - start
    print(f"Suite {name}: {passed} passed, {failed} failed in {duration:.2f}s")
    return passed, failed

if __name__ == "__main__":
    p1, f1 = run_suite(test_services, "Backend Core Services & APIs")
    p2, f2 = run_suite(test_edge_services, "Edge Node Hardware & IoT Services")
    total_passed = p1 + p2
    total_failed = f1 + f2
    print(f"\nTOTAL: {total_passed} passed, {total_failed} failed")
    if total_failed > 0:
        sys.exit(1)
    sys.exit(0)
