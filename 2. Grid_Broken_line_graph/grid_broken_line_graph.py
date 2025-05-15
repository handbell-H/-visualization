import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import platform
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('확인 필요')

plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv('Z:/격자 차트그리기 재도전/시군구별_연도별_인구_0024.CSV', encoding='cp949')

# 연도 컬럼만 추출
year_columns = [col for col in df.columns if col.isdigit()]

# 데이터 전처리
for col in year_columns:
    df[col] = df[col].replace("-", np.nan)
    df[col] = df[col].str.replace(",", "").astype(float)

# 시도 라인
BORDER_LINES = [
        [(3, 1),(3, 2), (5, 2), (5, 3), (9, 3), (9, 0)],  # 인천
        [(1, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
        [(1, 5), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3),(5, 3),(5, 2),(3, 2),(3, 3),(2, 3),(2, 5)],  # 경기도
        [(9, 13), (9, 10), (3, 10), (3, 9), (1, 9), (1, 6), (0, 6) ],  # 강원도
        [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
         (13, 4), (14, 4), (14, 2)],  # 충청남도
        [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
         (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)],  # 충청북도
        [(14, 4), (15, 4), (15, 6)],  # 대전시
        [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)],  # 경상북도
        [(14, 8), (16, 8), (16, 10), (15, 10),
         (15, 11), (14, 11), (14, 12), (13, 12)],  # 대구시
        [(15, 11), (16, 11), (16, 13)],  # 울산시
        [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)],  # 전라북도
        [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)],  # 광주시
        [(18, 5), (20, 5), (20, 6),(21, 6)],  # 전라남도
        [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9),(20, 10),(20, 12)], # 부산시
        [(20, 10),(21, 10)],
        [(24, 4), (24, 5),(26, 5),(26, 4),(24, 4)]#경상남도
    ]

# 시군구별 꺾은선 그래프 지도 함수
def drawKoreaWithLinePlots(pop_data, year_columns, x_col='x', y_col='y', label_col='행정구역'):
    fig, ax = plt.subplots(figsize=(10, 15))
    ax.set_xlim(0, pop_data[x_col].max() + 1)
    ax.set_ylim(0, pop_data[y_col].max() + 1)
    ax.set_aspect('equal')  # 💡 정사각형 유지
    ax.invert_yaxis()
    ax.axis('off')

    plt.text(-0.05, 0.99, f"시군구별 총 인구수 변화\n2000년 ~ 2024년", transform=plt.gca().transAxes,
             fontsize=17.5, verticalalignment='top', horizontalalignment='left',weight = 'bold')

    for _, row in pop_data.iterrows():
        if row['행정구역'] != '범례':
            x, y = row[x_col], row[y_col]
            values = row[year_columns].values.astype(float)

            # 크기를 줄이고 위치 살짝 조정
            inset_size = 0.5  # 💡 정사각형 크기
            inset_ax = inset_axes(ax,
                                  width=inset_size, height=inset_size,
                                  loc='center',
                                  bbox_to_anchor=(x, y, 1, 1),
                                  bbox_transform=ax.transData,
                                  borderpad=0)

            inset_ax.plot(year_columns, values, color='black', linewidth=1)
            inset_ax.fill_between(year_columns, values, color='red', alpha=0.1)
            inset_ax.set_xticks([])
            inset_ax.set_yticks([])
            inset_ax.set_facecolor('white')

            max_idx = np.nanargmax(values)
            max_year = year_columns[max_idx]
            max_value = values[max_idx]

            inset_ax.scatter(year_columns[max_idx], values[max_idx], color='red', s=4, zorder=5)

            formatted_value = format(int(max_value), ',')
            inset_ax.text(0.5, 0.5, f"{max_year}년\n{formatted_value}명",
                          fontsize=3, ha='center', va='center', color='black',
                          transform=inset_ax.transAxes)

            inset_ax.set_frame_on(False)
            '''

            for spine in inset_ax.spines.values():
                spine.set_visible(False)
                spine.set_color('black')
                spine.set_linewidth(0.05)
            '''

            inset_ax.text(0.5, 0.1, row['행정구역'], fontsize=5, ha='center', va='bottom', color='black', weight='bold',
                          transform=inset_ax.transAxes)

        else:
            x, y = row[x_col], row[y_col]
            values = row[year_columns].values.astype(float)

            # 크기를 줄이고 위치 살짝 조정
            inset_size = 0.5  # 💡 정사각형 크기
            inset_ax = inset_axes(ax,
                                  width=inset_size, height=inset_size,
                                  loc='center',
                                  bbox_to_anchor=(x, y, 1, 1),
                                  bbox_transform=ax.transData,
                                  borderpad=0)

            inset_ax.plot(year_columns, values, color='black', linewidth=0)
            inset_ax.fill_between(year_columns, values, color='red', alpha=0.1)
            inset_ax.set_xticks([])
            inset_ax.set_yticks([])
            inset_ax.set_facecolor('white')

            inset_ax.text(0.5, 0.8, f"인구수 꺾은선",
                          fontsize=4, ha='center', va='center', color='black', weight='bold',
                          transform=inset_ax.transAxes)

            inset_ax.text(0.5, 0.5, f"인구 최고연도\n최고 인구 수",
                          fontsize=3, ha='center', va='center', color='black',
                          transform=inset_ax.transAxes)

            inset_ax.set_frame_on(True)

            inset_ax.text(0.5, 0.1, row['행정구역'], fontsize=5, ha='center', va='bottom', color='black', weight='bold',
                          transform=inset_ax.transAxes)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        ax.plot(xs, ys, c='gray', lw=2)


    plt.tight_layout()
    plt.show()
    plt.savefig('Z:/격자 차트그리기 재도전/결과.png', dpi=300)
    plt.close()
# 실행

drawKoreaWithLinePlots(df, year_columns)
