from pathlib import Path

# Project root directory (one level above this file's folder).
root_path = Path(__file__).resolve().parents[2]

if __name__ == "__main__" : 
    print(root_path)