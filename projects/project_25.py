def parse_csv(path: str):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.strip().split(',')

def calculate_sums(path: str) -> None:
    with open('result.csv', 'w') as f:
        for row in parse_csv(path):
            adad = sum(map(int ,row))
            row.append(str(adad))
            csv_file = ', '.join(row)
            f.write(csv_file + '\n')
