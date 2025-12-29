# CDD Python Adapter

> **Official Python adapter for the CDD (Cyberattack-Driven Development) framework.**
> Effortlessly audit your application's security posture using our high-performance native Rust core.

## Installation

You can now install the package directly from PyPI:

```bash
# Official release
pip install cdd-python

# Or for local development (editable mode)
pip install -e .
```

## Integration Guide (e.g., FastAPI)
Integrating CDD into your existing projects allows you to automate security feedback during the development phase.

1. Create an Audit Script
In your project root (alongside your main.py), create a file named security_audit.py:

```bash
from cdd_python.engine import CDDEngine

def run_security_check():
    # 1. Initialize the engine
    engine = CDDEngine()
    
    # 2. Launch the attack on your local server
    # Ensure your server (FastAPI, Flask, etc.) is currently running!
    target_url = "http://localhost:8000"
    
    print(f"🛡️ CDD: Starting automated audit on {target_url}...")
    engine.execute_audit(target_url)

if __name__ == "__main__":
    run_security_check()
```

2. Run the Audit
Start your application in one terminal, then execute the audit script in another:

```bash
python security_audit.py
```

## Under the Hood
Native Rust Core: The package bundles pre-compiled binaries for Windows, Linux, and macOS (alpha.2).

Security Checks: Detects missing headers (HSTS), information leaks (X-Powered-By), and permissive CORS policies.

Part of the CDD-Framework organization.