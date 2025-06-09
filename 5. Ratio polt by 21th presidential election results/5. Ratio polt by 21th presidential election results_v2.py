import pandas as pd
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

df = pd.read_csv('Z:/격자 차트그리기 재도전/시군구별_득표율.CSV', encoding='cp949')

ratio_columns = ['1번','2번','그외']

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

def make_dispname(row):
    if row['광역시도'].endswith('시') and not row['행정구역'].startswith('세종'):
        dispname = '{} {}'.format(row['광역시도2'][:2], row['행정구역'])
    else:
        dispname = '{}'.format(row['행정구역'])
    return dispname

# 시군구별 비율 플롯 함수
def drawKoreaWithRatioPlots(election_data, ratio_columns, x_col='x', y_col='y', label_col='행정구역'):
    COLORS = ['#4F9DD9', '#FF6F61', '#FFD600']

    fig, ax = plt.subplots(figsize=(10, 15))
    ax.set_xlim(0, election_data[x_col].max() + 1)
    ax.set_ylim(0, election_data[y_col].max() + 1)
    ax.set_aspect('equal')  # 💡 정사각형 유지
    ax.invert_yaxis()
    ax.axis('off')

    plt.text(-0.05, 0.99, f"21대 대선 지역별\n개표 결과", transform=plt.gca().transAxes,
             fontsize=17.5, verticalalignment='top', horizontalalignment='left',weight = 'bold')

    for _, row in election_data.iterrows():
        if row['시군구명'] != '범례':
            x, y = row[x_col], row[y_col]
            ratios = row[ratio_columns].astype(float)
            ratios = ratios / ratios.sum()  # 총합이 1이 되도록 정규화

            inset_size = 0.5
            inset_ax = inset_axes(ax,
                                  width=inset_size, height=inset_size,
                                  loc='center',
                                  bbox_to_anchor=(x, y, 1, 1),
                                  bbox_transform=ax.transData,
                                  borderpad=0)

            # 스택형 가로 바(비율 그래프) 그리기
            inset_ax.set_aspect('equal')

            left = 0
            for idx, (ratio, color) in enumerate(zip(ratios, COLORS)):
                inset_ax.barh(0.5, ratio, left=left, height=1, color=color)
                # 비율값(%) 표기
                if ratio > 0.2:  # 너무 작으면 표시 안함
                    inset_ax.text(left + ratio / 2, 0.5, f"{int(ratio * 100)}%", ha='center', va='center', fontsize=5,
                                  color='white')
                left += ratio

            # 구역명

            dispname = make_dispname(row)
            last_line = dispname.splitlines()[-1]
            if len(last_line) >= 3:
                fontsize, linespacing = 5, 1.3
            else:
                fontsize, linespacing = 5, 1.2

            inset_ax.text(0.5, 0.75, dispname, fontsize=fontsize, ha='center', va='bottom', color='white', weight='bold',linespacing=linespacing,
                          transform=inset_ax.transAxes)

            # 바 외 기타 설정
            inset_ax.set_xlim(0, 1)
            inset_ax.set_ylim(0, 1)
            inset_ax.set_xticks([])
            inset_ax.set_yticks([])
            inset_ax.set_frame_on(False)
            inset_ax.axis('off')

        else:
            x, y = row[x_col], row[y_col]
            ratios = row[ratio_columns].astype(float)
            ratios = ratios / ratios.sum()  # 총합이 1이 되도록 정규화

            inset_size = 0.5
            inset_ax = inset_axes(ax,
                                  width=inset_size, height=inset_size,
                                  loc='center',
                                  bbox_to_anchor=(x, y, 1, 1),
                                  bbox_transform=ax.transData,
                                  borderpad=0)

            # 스택형 가로 바(비율 그래프) 그리기
            inset_ax.set_aspect('equal')

            left = 0
            for idx, (ratio, color) in enumerate(zip(ratios, COLORS)):
                inset_ax.barh(0.5, ratio, left=left, height=1, color=color)
                left += ratio

            # 구역명

            inset_ax.text(0.5, 1.2, f"범례",
                          fontsize=7, ha='center', va='center', color='black', weight='bold',
                          transform=inset_ax.transAxes)

            inset_ax.text(0.5, 0.4, row[label_col], fontsize=5, ha='center', va='bottom', color='black',
                          transform=inset_ax.transAxes)

            # 바 외 기타 설정
            inset_ax.set_xlim(0, 1)
            inset_ax.set_ylim(0, 1)
            inset_ax.set_xticks([])
            inset_ax.set_yticks([])
            inset_ax.set_frame_on(False)
            inset_ax.axis('off')

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        ax.plot(xs, ys, c='gray', lw=2)

    plt.tight_layout()
    plt.show()
    plt.savefig('Z:/격자 차트그리기 재도전/21대 대선 지역별 개표 결과_v1.png', dpi=300)
    plt.close()

drawKoreaWithRatioPlots(df, ratio_columns)
