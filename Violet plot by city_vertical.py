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

data = pd.read_csv('Z:/바이올렛 차트 그리기/data/국토생활인프라_1km_euckr.csv', encoding='euc-kr')
data = data[['sido_nm','Me_CI']]
unique_sido_list = data['sido_nm'].drop_duplicates().tolist()

# 그래프 스타일 설정 # 세로 : figsize=(10, 24) # 가로 : figsize=(24, 10)
plt.figure(figsize=(10, 24))

# 배경 스타일 설정
plt.grid(axis='x', color='lightgray', linestyle='-', linewidth=0.5)
plt.grid(axis='y', visible=False)  # y축 그리드 제거

# 가로형 바이올린 플롯 생성
ax = sns.violinplot(
    x='Me_CI',
    y='sido_nm',
    data=data,
    orient='h',  # 방향 (v, h)
    color='lightgray',  # 모든 바이올린을 동일한 회색으로
    inner=None,
    linewidth=0.5,  # 테두리 선 두께
    width=1.65,  # 바이올린 너비
)

# 사분위수 정보 계산
quartiles = {}
for sido_nm in unique_sido_list:
    sido_data = data[data['sido_nm'] == sido_nm]['Me_CI']
    q1 = np.percentile(sido_data, 25)
    q2 = np.percentile(sido_data, 50)  # 중앙값
    q3 = np.percentile(sido_data, 75)
    quartiles[sido_nm] = (q1, q2, q3)

# 수동으로 중앙값과 사분위수 범위 추가
for i, sido_nm in enumerate(unique_sido_list):
    q1, median, q3 = quartiles[sido_nm]

    # 어두운 회색 사분위수 바 추가
    plt.hlines(i, q1, q3, color='#555555', linewidth=4, zorder=3)

    # 검은색 중앙값 점 추가
    plt.scatter(median, i, color='black', s=50, zorder=4)

plt.xlim(0, 20)

# 세로 격자선 설정 - 더 세부적이고 원본과 비슷하게
ax.xaxis.set_major_locator(MultipleLocator(1))  # 주 눈금 간격
plt.grid(axis='x', which='minor', color='lightgray', linestyle='-', linewidth=0.5)

# 축과 테두리 설정
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 축 레이블 설정
plt.xlabel('')
plt.ylabel('')

plt.subplots_adjust(left=0.25)

plt.title('시도별 생활인프라 충족도 분포 (1km)', fontsize=16, fontweight='bold', pad=20)

# 그래프 여백 조정
plt.tight_layout()

# 그래프 저장 및 표시
plt.savefig('Z:/바이올렛 차트 그리기/data/시도별 바이올렛 차트_세로.png', dpi=300, bbox_inches='tight')
plt.close()