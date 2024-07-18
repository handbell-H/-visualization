import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 시스템에 따라 한글 폰트 설정
def set_korean_font():
    if platform.system() == 'Darwin':
        rc('font', family='AppleGothic')
    elif platform.system() == 'Windows':
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:
        print('Unknown system... sorry~~~~')
    plt.rcParams['axes.unicode_minus'] = False

set_korean_font()

# 데이터 불러오기
#data_path = '//nas1.krihs.re.kr/profile/20230003/Desktop/손종혁 국토연구원/지도그리기 연습/보고서표지.csv'
my_data_path = '//nas1.krihs.re.kr/profile/20230003/Desktop/손종혁 국토연구원/지도그리기 연습/보고서표지.csv'

data_grid_sgg = pd.read_csv(my_data_path, index_col=0, encoding='euc-kr')

def grid_sgg(target_data, blocked_map, region_col, subregion_col, cmap_name, save_path, white_label_min=50, gamma=0.75):
    BORDER_LINES = [
        [(3, 1),(3, 2), (5, 2), (5, 3), (9, 3), (9, 0)],  # 인천
        [(1, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
        [(1, 5), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
         (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3),(5, 3),(5, 2),(3, 2),(3, 3),(2, 3),(2, 5)],  # 경기도
        [(9, 13), (9, 10), (3, 10), (3, 9), (1, 9), (1, 6), (0, 6)],  # 강원도
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
        [(24, 4), (24, 5),(26, 5),(26, 4),(24, 4)]  # 경상남도
    ]

    map_data = blocked_map.pivot(index='y', columns='x', values=target_data)
    masked_map_data = np.ma.masked_where(np.isnan(map_data), map_data)

    plt.figure(figsize=(8, 13))
    plt.pcolor(masked_map_data, vmin=0, vmax=100, cmap=cmap_name, edgecolor='#808080', linewidth=0.5)

    for idx, row in blocked_map.iterrows():
        annocolor = 'white' if row[target_data] > white_label_min else 'black'

        if row[region_col].endswith('시') and not row[region_col].startswith('세종'):
            dispname = f"{row[region_col][:2]}\n{row[subregion_col]}\n({row[target_data]})"
        else:
            dispname = f"{row[subregion_col]}\n({row[target_data]})"

        fontsize, linespacing = (7, 1.3) if len(dispname.splitlines()[-1]) >= 3 else (8, 1.2)

        plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='Green', lw=3)

    plt.gca().invert_yaxis()
    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label('비율')

    plt.tight_layout()
    plt.savefig(save_path, dpi=1000)

save_path = '//nas1.krihs.re.kr/profile/20230003/Desktop/보고서표지5.png'

grid_sgg('보고서이미지용', data_grid_sgg, '광역시도', '행정구역', 'Greens', save_path)
