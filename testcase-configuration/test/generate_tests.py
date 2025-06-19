def load_test_data():
    return [
        {"input": "Hello world", "context": "", "expected": "Hello"},
        {"input": "Calculate 5 * 6", "context": "", "expected": "30"},
    ]

def create_tests():
    test_cases = []

    test_data = load_test_data()

    for item in test_data:
        test_cases.append({
            "vars": {
                "input": item["input"],
                "context": item["context"]
            },
            "assert": [{
                "type": "contains",
                "value": item["expected"]
            }]
        })

    return test_cases
