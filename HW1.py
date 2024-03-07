import pandas as pd

# 從 CSV 檔案中讀取資料
df = pd.read_csv('C:/Users/USER/Desktop/HW1/badminton.csv')

# 將DataFrame轉換成Set資料型態
badminton1_set = set(zip(df['2022']))
badminton2_set = set(zip(df['2023']))
# 聯集分析
union = badminton1_set.union(badminton2_set)
print("聯集結果：", union)

# 交集分析
intersection = badminton1_set.intersection(badminton2_set)
print("交集結果：", intersection)

# 差集分析 (以原先的學生資料為基準)
difference = badminton1_set.difference(badminton2_set)
print("差集結果：", difference)