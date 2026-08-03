def count_executable_lines(path: str) -> int:
    code_lines = 0
    with open(path, 'r') as f:
        for line in f:
            line_check = line.strip()
            if line_check.startswith('#'):
                continue
            elif not line_check:
                continue
            else:
                code_lines += 1
    return code_lines