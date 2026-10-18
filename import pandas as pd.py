import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: 生成数据
np.random.seed(42)
dates = pd.date_range('2020-01-01', '2023-12-31', freq='D')
value = 100 + 50*np.sin(np.arange(len(dates)) * 2 * np.pi / 365) + np.random.normal(0, 10, len(dates))
df = pd.DataFrame({'date': dates, 'value': value})
df.to_csv('data.csv', index=False)

# Step 2: 画时间序列图
plt.figure(figsize=(12, 4))
plt.plot(df['date'], df['value'], linewidth=0.8)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series — Synthetic Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('timeseries.png', dpi=150)
print('saved timeseries.png')
plt.show()
# Step 3: 散点图
plt.figure(figsize=(6, 6))
plt.scatter(df['date'], df['value'], alpha=0.3, s=8)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Scatter — Daily Observations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('scatter.png', dpi=150)
print('saved scatter.png')
plt.show()
# Step 4: 均值和月度聚合
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
print('Overall mean:', df['value'].mean())

df_monthly = df.groupby(df.index.to_period('M')).mean()
print('\nMonthly averages (first 12 months):')
print(df_monthly.head(12))

# 月度均值折线图
plt.figure(figsize=(12, 4))
plt.plot(df_monthly.index.astype(str), df_monthly['value'], marker='o', markersize=4, linewidth=1.5)
plt.xlabel('Month')
plt.ylabel('Monthly Mean Value')
plt.title('Monthly Averaged Time Series')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_avg.png', dpi=150)
print('\nsaved monthly_avg.png')
plt.show()