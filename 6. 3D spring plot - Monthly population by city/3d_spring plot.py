import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv('Z:/시각화/3D 스프링차트 그리기/충주시 인구.csv', encoding='cp949')
df = df.dropna(subset=['연월', 'pop_충주']).copy()

dates = df['연월'].astype(str)
pops = df['pop_충주'].astype(float).values
n = len(df)

month_list, year_list = [], []
for d in dates:
    y, m = d.split('년 ')
    year_list.append(int(y.strip()))
    month_list.append(int(m.replace('월','').strip()))
months = np.array(month_list)
years = np.array(year_list)

month_idx = months - 1
theta = month_idx / 12 * 2 * np.pi
z = np.arange(n) * 0.2  # z축 빽빽하게 (0.2~0.08 등으로 조절 가능)
pops_norm = (pops - pops.min()) / (pops.max() - pops.min())
radius = 1.0 + pops_norm * 0.6
x = np.cos(theta) * radius
y = np.sin(theta) * radius
labels = [f"{d}<br>{int(p):,}명" for d, p in zip(dates, pops)]

# 2011년 기준으로 2d 십이각형
idx_2011 = np.where(years == 2011)[0][:12]
theta_2011 = theta[idx_2011]
radius_2011 = radius[idx_2011]
x_2011 = np.cos(theta_2011) * radius_2011
y_2011 = np.sin(theta_2011) * radius_2011
z_2011 = np.zeros_like(x_2011)
x_2011 = np.append(x_2011, x_2011[0])
y_2011 = np.append(y_2011, y_2011[0])
z_2011 = np.append(z_2011, 0)

month_angles = np.arange(12) / 12 * 2 * np.pi
label_r = np.mean(radius_2011) * 1.08
x_label = np.cos(month_angles) * label_r
y_label = np.sin(month_angles) * label_r
z_label = np.zeros_like(x_label)
month_names = [f"{i+1}월" for i in range(12)]

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(color=pops, colorscale='Bluered', width=35),
    text=labels,
    hoverinfo='text',
    name="시계열"
))

fig.add_trace(go.Scatter3d(
    x=x_2011, y=y_2011, z=z_2011,
    mode='lines',
    line=dict(color='black', width=8, dash='dot'),
    showlegend=False
))

fig.add_trace(go.Scatter3d(
    x=x_label, y=y_label, z=z_label,
    mode='text',
    text=month_names,
    textfont=dict(size=22, color='gray'),
    showlegend=False
))

fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False, showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(visible=False, showticklabels=False, showgrid=False, zeroline=False),
        zaxis=dict(visible=False, showticklabels=False, showgrid=False, zeroline=False),
        bgcolor='white'
    ),
    margin=dict(l=0, r=0, t=40, b=0),
    title="충주시 월별 인구 - 3D 스프링 시계열",
    paper_bgcolor='white',
    plot_bgcolor='white'
)

fig.write_html('Z:/시각화/3D 스프링차트 그리기/충주시_스프링_인구시계열.html')
