# 两组数据绘制散点图 分别拟合 添加 Slope为两条拟合线差值的 0截距线
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

import pandas as pd

# 字体
mat.rcParams['font.sans-serif']=['Arial']
mat.rcParams['axes.unicode_minus'] = False

# 读取文件
data1 = pd.read_csv(r"D:\ActiveStudy\ClimateAsymmetry\Fig\Three_Area_Asymmetry_Fig\Bor_LSTdailymean_gain.csv")
data2 = pd.read_csv(r"D:\ActiveStudy\ClimateAsymmetry\Fig\Three_Area_Asymmetry_Fig\Bor_LSTdailymean_loss.csv")

# 清理数据，删除 NaN 值，确保数据为浮点数
data1 = data1.dropna(subset=['ratio_range', 'new_variable'])
data2 = data2.dropna(subset=['ratio_range', 'new_variable'])

data1['ratio_range'] = data1['ratio_range'].astype(float)
data1['new_variable'] = data1['new_variable'].astype(float)
data2['ratio_range'] = data2['ratio_range'].astype(float)
data2['new_variable'] = data2['new_variable'].astype(float)

# 创建散点图
plt.figure(figsize=(8,6))
scatter1=plt.scatter(data1['ratio_range'],data1['new_variable'],color = 'red', alpha = 0.5,s=100,label='Gain')
scatter2=plt.scatter(data2['ratio_range'],data2['new_variable'],color = 'blue',alpha = 0.5,s=100,label='Loss')

# 添加拟合线（截距为0）
fit1 = np.polyfit(data1['ratio_range'], data1['new_variable'], 1)
slope1 = fit1[0]
x_vals = np.linspace(0, 0.55, 100) # 修改
fit_line1 = slope1 * x_vals
plt.plot(x_vals, fit_line1, color='red', linewidth=4)

fit2 = np.polyfit(data2['ratio_range'], data2['new_variable'], 1)
slope2 = fit2[0]
fit_line2 = slope2 * x_vals
plt.plot(x_vals, fit_line2, color='blue', linewidth=4)

# 计算两条拟合线的斜率和，并绘制一条截距为0的直线
slope_diff = fit1[0] + fit2[0]
x_vals = np.linspace(0, 0.55, 100) # 修改
y_vals = slope_diff * x_vals
plt.plot(x_vals, y_vals, color='green', linewidth=4)


# 添加标题、标签等
'''
plt.title('Scatter Plot of Two Datasets')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
'''

# 增加轴线粗细
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 设置坐标范围
plt.xlim(0, 0.55) # 修改
plt.ylim(-0.4, 0.4) # 修改

# 设置坐标刻度
plt.xticks(np.arange(0, 0.55, 0.1), fontsize=22,fontweight='bold') # 修改
plt.yticks(np.arange(-0.4, 0.6, 0.2), fontsize=22, fontweight='bold') # 修改

# 添加图例
plt.legend(handles=[scatter1, scatter2], prop={'size': 20, 'weight': 'bold'}, loc='upper left')

# 展示并导出矢量图形
#plt.grid()
#plt.tight_layout()
# plt.savefig(r"D:\ActiveStudy\ClimateAsymmetry\Fig\Three_Area_Asymmetry_Slope_Fig\Separate_Slope_originalpoint_python\Tro_day.svg", format='svg', bbox_inches='tight')
#plt.show()

print(f"Slope of Data Set 1: {slope1}")
print(f"Slope of Data Set 2: {slope2}")