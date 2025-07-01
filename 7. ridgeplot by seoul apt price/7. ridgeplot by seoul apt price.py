import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name
plt.rcParams['axes.unicode_minus'] = False

path = 'Z:/시각화/릿지라인차트 그리기/'
df = pd.read_csv(path + '서울시 부동산 실거래가 정보_아파트_2025.csv', encoding='euc-kr')

구_list = sorted(df['자치구명'].unique())
n = len(구_list)

x_min = df['물건금액(천만원)'].min()
x_max = df['물건금액(천만원)'].max()
tick_range = list(range(100, int(x_max)+100, 100))

fig, axes = plt.subplots(nrows=n, figsize=(13, 8), sharex=True)
fig.subplots_adjust(left=0.15, hspace=-0.2)
fig.set_alpha(0)

for i, (gu, ax) in enumerate(zip(구_list, axes)):
    data = df.loc[df['자치구명'] == gu, '물건금액(천만원)']
    sns.kdeplot(data, fill=True, color='#AEDFF7', alpha=0.75, ax=ax, ec='#76C7B7', lw=0.5, bw_adjust=1)

    mean_val = data.mean()
    ax.axvline(mean_val, color='gray', lw=0.5, ls='-', zorder=3)

    y_max = ax.get_ylim()[1]
    ax.text(mean_val, y_max * 0.95, f"{mean_val:,.0f}",
            color='gray', fontsize=6, fontweight='bold',
            ha='center', va='bottom', zorder=4)

    ax.set_ylabel("")
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_yticks([])

    ax.text(0, ax.get_ylim()[1] * 0.2, gu, fontdict={"fontsize":10, "weight":"bold"}, va="center", ha="right")
    if i == n-1:
        ax.set_xlabel("아파트 거래가 (천만원)", fontsize=12)
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

plt.savefig(path + '부동산 릿지차트.png', dpi=300)