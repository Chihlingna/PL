import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei')

data = {
    "新北市": {
        "男生": 1965445,
        "女生": 2075675
    },
    "台北市": {
        "男生": 1187064,
        "女生": 1324822
    },
    "桃園市": {
        "男生": 1142786,
        "女生": 1174659
    },
    "台中市": {
        "男生": 1391681,
        "女生": 1454228
    },
    "台南市": {
        "男生": 923152,
        "女生": 936794
    },
    "高雄市": {
        "男生": 1343106,
        "女生": 1394835
    },
    "宜蘭縣": {
        "男生": 225873,
        "女生": 224017
    },
    "新竹縣": {
        "男生": 299933,
        "女生": 289356
    },
    "苗栗縣": {
        "男生": 274920,
        "女生": 259655
    },
    "彰化縣": {
        "男生": 628065,
        "女生": 610983
    },
    "南投縣": {
        "男生": 242993,
        "女生": 234101
    },
    "雲林縣": {
        "男生": 340082,
        "女生": 319386
    },
    "嘉義縣": {
        "男生": 250858,
        "女生": 233702
    },
    "屏東縣": {
        "男生": 402917,
        "女生": 392080
    },
    "台東縣": {
        "男生": 107954,
        "女生": 103590
    },
    "花蓮縣": {
        "男生": 159649,
        "女生": 157840
    },
    "澎湖縣": {
        "男生": 55208,
        "女生": 52531
    },
    "基隆市": {
        "男生": 180125,
        "女生": 182130
    },
    "新竹市": {
        "男生": 225225,
        "女生": 231250
    },
    "嘉義市": {
        "男生": 126610,
        "女生": 136974
    },
    "金門縣": {
        "男生": 71542,
        "女生": 72607
    },
    "連江縣": {
        "男生": 8079,
        "女生": 5960
    }
}

# 將資料轉換為JSON格式並寫入檔案
with open('population_data.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
import json

# 讀取JSON檔案
with open('population_data.json', 'r') as json_file:
    data = json.load(json_file)
# 提取各縣市男生總人口和女生總人口
counties = list(data.keys())
male_population = [data[county]['男生'] for county in counties]
female_population = [data[county]['女生'] for county in counties]

# 繪製長條圖
plt.figure(figsize=(15, 8))
bar_width = 0.35
index = range(len(counties))

plt.bar(index, male_population, bar_width, label='男生總人口')
plt.bar([i + bar_width for i in index], female_population, bar_width, label='女生總人口')

plt.xlabel('縣市')
plt.ylabel('人口數量')
plt.title('各縣市男生與女生總人口')
plt.xticks([i + bar_width / 2 for i in index], counties, rotation=45)
plt.legend()

# 在右側留出空白區域
plt.xlim([-0.5, len(counties) - 0.5])

# 添加自己的想法，將 y 參數調整為向上移動
plt.text(len(counties) + 5, max(max(male_population), max(female_population)) / 2, '從這張圖表可以發現前幾名最多人口的\n縣市都是女生人口數量多於男生人口數\n量，而後面人口數量較少的縣市卻是男\n生多於女生。', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()


# 計算各縣市男生及女生加總人口
male_population = {}
female_population = {}

for city, population in data.items():
    male_population[city] = population['男生']
    female_population[city] = population['女生']

# 繪製長條圖
plt.figure(figsize=(12, 6))
plt.bar(male_population.keys(), male_population.values(), color='blue', label='男生總人口')
plt.bar(female_population.keys(), female_population.values(), color='pink', label='女生總人口', bottom=list(male_population.values()))
plt.xlabel('縣市')
plt.ylabel('人數')
plt.title('各縣市男女生總人口')
plt.xticks(rotation=45, ha='right')
plt.legend()

# 在右側留出空白區域
plt.xlim([-0.5, len(male_population.keys()) - 0.5])

# 添加自己的想法，將 y 參數調整為向上移動
plt.text( 0.5, sum(male_population.values()) / 2, '由這張圖表可以發現各縣市的男女比幾乎都是接近1:1', fontsize=12, ha='left', va='center')

plt.tight_layout()
plt.show()


# 找出最多男生的前三名縣市
sorted_male_population = sorted(data.items(), key=lambda x: x[1]['男生'], reverse=True)[:3]
top_male_cities = [city for city, _ in sorted_male_population]
male_population = [data[city]['男生'] for city in top_male_cities]

# 找出最多女生的前三名縣市
sorted_female_population = sorted(data.items(), key=lambda x: x[1]['女生'], reverse=True)[:3]
top_female_cities = [city for city, _ in sorted_female_population]
female_population = [data[city]['女生'] for city in top_female_cities]

# 繪製長條圖
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(top_male_cities, male_population, color='blue')
plt.title('男生總人口最多的前三名')
plt.xlabel('縣市')
plt.ylabel('男生總人口')

plt.subplot(1, 2, 2)
plt.bar(top_female_cities, female_population, color='pink')
plt.title('女生總人口最多的前三名')
plt.xlabel('縣市')
plt.ylabel('女生總人口')

# 調整子圖間的間距
plt.subplots_adjust(wspace=0.5)

# 添加自己的想法
plt.text(4, 0.5, '由這張圖表可以發現不論男生或\n女生，總人口最多的是新北市，\n其次是台中市和高雄市，而且新\n北市遠遠超過其他兩個縣市。', fontsize=12, ha='center')


plt.tight_layout()
plt.show()