import re

def camelCase(s: str) -> str:
    return re.sub(r'(.*?)_([a-z])', lambda m: m.group(1) + m.group(2).upper(), str)