import sys
from cdd_python.engine import CDDEngine


def run_dynamic_test():
    port = sys.argv[1] if len(sys.argv) > 1 else "8080"
    target = f"http://localhost:{port}"

    engine = CDDEngine()

    print(f"🚀 Testing Python Wrapper dynamically against {target}...")

    engine.execute_audit(target)


if __name__ == "__main__":
    run_dynamic_test()
