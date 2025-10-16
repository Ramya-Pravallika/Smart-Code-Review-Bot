import subprocess

def analyze_python_code(code):
    # Write code to temp file, run pylint, capture output
    with open('temp.py', 'w') as f:
        f.write(code)
    result = subprocess.run(['pylint', 'temp.py'], capture_output=True, text=True)
    return result.stdout.splitlines()