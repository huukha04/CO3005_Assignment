import os
import json

def load_json_tests(filename="test_lexer.json"):
    # Lấy thư mục hiện tại của file helper.py (chính là tests/)
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, filename)

    tests = []
    with open(path, encoding="utf-8") as f:
        data = json.load(f) 
        for item in data:
            tests.append((
                # item["id"],
                item["source"], 
                item["expected"]
            ))
    return tests
