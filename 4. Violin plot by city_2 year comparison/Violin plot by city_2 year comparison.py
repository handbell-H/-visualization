import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.ticker import MultipleLocator
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

df = pd.read_csv('Z:/0_국토모니터링/생활인프라 비교 분석 해보기/생활인프라_합본_melt_특광역시제외.csv', encoding='euc-kr')
df['year'] = df['year'].astype(str)
df['grade'].unique()

sorted_grade = ['~5만',  '5만~10만', '10만~30만', '30만~50만', '50만~100만', '100만 이상']

# 바이올린 플롯 그리기 figsize=(10, 24)
plt.figure(figsize=(8, 12))

ax = sns.violinplot(
    data=df,
    x='grade',
    y='CI',
    hue='year',
    split=True,
    orient='v',
    palette={'19': '#5dade2', '23': '#f1948a'},
    inner='quart',
    linewidth = 0.5,
    width=1, # 바이올린 너비
    cut = 0,
    order = sorted_grade,
    density_norm='count')

ax.set_axisbelow(True)

# 격자 설정 (Y축이 값 축이므로 Y축에 minor 지정)
plt.grid(True, which='major', axis='both', color='lightgray', linestyle='-', linewidth=0.5)
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(1))

# 축 스타일 등
for spine in ['right', 'top', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

# 제목과 축 레이블 위치 바꾸기
plt.title('시도별 생활인프라 충족도 분포 (2019 vs 2023)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('시군별 인구 규모')
plt.ylabel('생활인프라 충족도(평균)')
ax.legend(title='연도', loc='upper right')

plt.ylim(0, 10)
plt.yticks(np.arange(0, 11, 1))

medians = df.groupby(['grade', 'year'])['CI'].median().unstack()

# 꺾은선용
median_19_line = []
median_23_line = []

# 중위값 차이 선 연결 및 텍스트 표시
for i, grade in enumerate(sorted_grade):
    median_19 = medians.loc[grade, '19']
    median_23 = medians.loc[grade, '23']

    median_19_line.append((i, median_19))
    median_23_line.append((i, median_23))

    ax.scatter(i, median_19, color='gray', s=10, zorder=5)
    ax.scatter(i, median_23, color='black', s=10, zorder=5)

    ax.plot([i, i], [median_19, median_23], color='gray', linewidth=1, linestyle='--')

    diff = median_23 - median_19
    ax.text(i + 0.05 , (median_19 + median_23) / 2 - 0.04 , f'+{diff:.2f}', color='black', fontsize=8.5)

# 꺾은선 플롯
x19, y19 = zip(*median_19_line)
ax.plot(x19, y19, color='#5dade2', linestyle='--', linewidth = 1, marker='o', label='2019년 생활인프라 충족도 중앙값 추세')

x23, y23 = zip(*median_23_line)
ax.plot(x23, y23, color='#f1948a', linestyle='--', linewidth= 1, marker='o', label='2023년 생활인프라 충족도 중앙값 추세')

ax.legend(title='연도', loc='upper right')

plt.tight_layout()
plt.savefig('Z:/0_국토모니터링/생활인프라 비교 분석 해보기/인구규모 별 충족도_세로_특광역시 제외.png', dpi=300, bbox_inches='tight')
plt.close()

