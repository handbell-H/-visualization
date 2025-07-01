import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name
plt.rcParams['axes.unicode_minus'] = False

path = 'Z:/시각화/릿지라인차트 그리기/'
df = pd.read_csv(path + '서울시 부동산 실거래가 정보_아파트_합본_50억 이상 아파트 제외.csv', encoding='euc-kr')

접수연도_list = sorted(df['접수연도'].unique())
palette = ['#AEDFF7', '#FFD6A5']  # 연도별 색상 (원하는대로 추가)
edge_palette = ['#76C7B7', '#F6AE99']

x_min = df['물건금액(천만원)'].min()
x_max = df['물건금액(천만원)'].max()
tick_range = list(range(100, int(x_max)+100, 100))

# (1) 기준연도별 평균으로 구 정렬
기준연도 = 접수연도_list[-1]  # 가장 최근 연도
구별_평균 = (
    df[df['접수연도'] == 기준연도]
    .groupby('자치구명')['물건금액(천만원)'].mean()
    .sort_values()
)
구_list = 구별_평균.index.tolist()
n = len(구_list)

fig, axes = plt.subplots(nrows=n, figsize=(13, 8), sharex=True)
fig.subplots_adjust(left=0.15, hspace=-0.2)
fig.set_alpha(0)

for i, (gu, ax) in enumerate(zip(구_list, axes)):
    mean_list = []
    for yidx, 접수연도 in enumerate(접수연도_list):
        data = df.loc[(df['자치구명'] == gu) & (df['접수연도'] == 접수연도), '물건금액(천만원)']
        if len(data) == 0:
            mean_list.append(None)
            continue
        sns.kdeplot(data, fill=True, color=palette[yidx], alpha=0.75,
                    ax=ax, ec=edge_palette[yidx], lw=1.0, bw_adjust=1,
                    label=f"{접수연도}" if i == 0 else None)
        mean_val = data.mean()
        mean_list.append(mean_val)
        ax.axvline(mean_val, color=edge_palette[yidx], lw=1, ls='--', zorder=3)

    if len(mean_list) == 2 and None not in mean_list:
        diff = mean_list[1] - mean_list[0]
        mid_val = (mean_list[0] + mean_list[1]) / 2
        y_max = ax.get_ylim()[1]
        sign = "+" if diff >= 0 else ""
        ax.text(mid_val, y_max * 0.35, f"{sign}{diff:,.0f}",
                color="black", fontsize=6,
                ha='center', va='bottom', zorder=5)

    ax.set_ylabel("")
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_yticks([])
    ax.text(0, ax.get_ylim()[1] * 0.2, gu,
            fontdict={"fontsize":10, "weight":"bold"}, va="center", ha="right")
    if i == n-1:
        ax.set_xlabel("아파트 거래가(천만원) [50억 이상 아파트 제외]", fontsize=12)
        ax.tick_params(axis="x", direction="inout", color="lightgray", length=5, width=1.5, labelsize=10)
    else:
        ax.tick_params(axis="x", length=0, labelbottom=False)
    ax.set_xlim(x_min, x_max)
    ax.set_xticks(tick_range)

    xticks = ax.get_xticks()
    for xtick in xticks:
        ax.axvline(xtick, color='lightgray', lw=0.5, zorder=0)
    ax.axhline(0, color="lightgray", lw=0.5)
    ax.patch.set_alpha(0)

if n > 0:
    axes[0].legend(title='접수연도', loc='upper right', fontsize=9, title_fontsize=10)

plt.tight_layout()
plt.savefig(path + '부동산 릿지차트_비교_증감폭_정렬.png', dpi=300)
plt.close()
