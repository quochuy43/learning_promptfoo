import pandas as pd

df = pd.read_csv("results.csv")
# df.columns = ['input', 'gemini_1_5', 'gemini_2_0']
# print(df.columns)

import re

def parse_result(result):
    # find PASS/FAIL
    pass_fail_match = re.search(r'\[(PASS|FAIL)\]', result)
    score_match = re.search(r'\(([\d.]+)\)', result)
    reason_match = re.search(r'(Pass Reason|Fail Reason): (.*)', result)

    return {
        'status': pass_fail_match.group(1) if pass_fail_match else None,
        'score': float(score_match.group(1)) if score_match else None,
        'reason': reason_match.group(2).strip() if reason_match else None
    }
print(df.columns)


