import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
import numpy as np

# 한글 폰트 설정
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('확인 필요')

file_path = 'W:/2025년/05_분석/생활인프라/시각화 자료 모음/dumbbel plot/dumbbel_plot 용 데이터2.csv'

# 데이터 불러오기
df = pd.read_csv(file_path, encoding='euc-kr')

# 1. 특광역시 제외 및 총 인구_비율 0 아닌 행 필터링
df_filtered = df[(df['유형'] != '특광역시') & (df['총 인구_비율'] != 0)].copy()

# 2. 유형 순서 사전 정의
order_dict = {
    '5만 미만': 0,
    '5만 이상 10만 미만': 1,
    '10만 이상 30만 미만': 2,
    '30만 이상 50만 미만': 3,
    '50만 이상 100만 미만': 4,
    '100만 이상': 5
}

df_filtered['구간순서'] = df_filtered['유형'].map(order_dict)

df_filtered.sort_values(['구간순서', '시군구명'], inplace=True)
df_filtered.reset_index(drop=True, inplace=True)

y_labels = df_filtered['시군구명'].values
y_pos = np.arange(len(y_labels))

x1 = df_filtered['65세 이상 인구_비율']
x2 = df_filtered['총 인구_비율']

fig, ax = plt.subplots(figsize=(10, len(y_labels)*0.3))
ax.hlines(y=y_pos, xmin=x1, xmax=x2, color='gray', alpha=0.7, linewidth=2)
ax.scatter(x2, y_pos, color='black', label='총 인구 비율 (○)', s=50, marker='o', zorder=3)
ax.scatter(x1, y_pos, color='gray', label='65세 이상 인구 비율 (△)', s=50, marker='^', zorder=3)

ax.set_yticks(y_pos)
ax.set_yticklabels(y_labels)

ax.set_xlim(0, 100)
ax.set_xlabel('비율 (%)')
ax.margins(y=0.01)

for 구간명, 순서 in order_dict.items():
    subset = df_filtered[df_filtered['구간순서'] == 순서]
    if subset.empty:
        continue
    min_y = subset.index.min()
    max_y = subset.index.max()

    ax.hlines(y=max_y + 0.5, xmin=0, xmax=100, colors='black', linestyles='dashed', linewidth=0.7, alpha=0.5)

    center_y = (min_y + max_y) / 2
    ax.text(102, center_y, 구간명, va='center', ha='left', fontsize=9, color='gray')

ax.legend()
fig.subplots_adjust(left=0.25, right=0.85, top=0.95, bottom=0.05)
plt.tight_layout()

ax.invert_yaxis()

plt.show()
plt.savefig('W:/2025년/05_분석/생활인프라/시각화 자료 모음/dumbbel plot/dumbbel_plot_with_lines_and_labels2.png', dpi=300)
plt.close()
