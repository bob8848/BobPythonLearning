import csv

def average_column(file_path, column_index):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        values = [float(row[column_index]) for row in reader]
    return sum(values) / len(values) if values else 0

# 示例调用
print(average_column("data.csv", 2))
