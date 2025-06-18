from typing import Dict

def get_var(var_name: str, prompt: str, other_vars: Dict[str, str]) -> Dict[str, str]:
    if var_name == 'context':
        return {
            'output': f"Some background knowledge for input '{other_vars['input']}'"
        }
    return {'output': 'default context'}
