# scripts/generate_chart.py
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. 读取数据
with open('data/stats.json', 'r') as f:
    data = json.load(f)

# 2. 转换数据为Pandas DataFrame
df = pd.DataFrame(data['weightLog'])
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# 3. 生成图表
plt.style.use('seaborn-v0_8-darkgrid') # 使用一个好看的样式
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df['date'], df['weight_kg'], marker='o', linestyle='-', color='b')
ax.set_title('Weight Trend Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Weight (kg)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout() # 调整布局，防止标签重叠

# 4. 保存图表
# 确保charts目录存在
if not os.path.exists('charts'):
    os.makedirs('charts')

plt.savefig('charts/weight_trend.png')

print("Chart generated successfully!")