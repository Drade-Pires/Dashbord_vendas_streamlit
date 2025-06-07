import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores, df_total_vendas, df_vendas_por_vendedor

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    color='Preço',  # <- Isso ativa a escala de cores
    color_continuous_scale='Plasma',  # <- Paleta de cores (opcional)
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)

grafico_map_estado.update_geos(
    fitbounds="locations",
    visible=True      
)
grafico_map_estado.update_layout(
    height=450,
    width=800,
    margin=dict(l=0, r=0, t=40, b=0)
)
grafico_map_estado.update_coloraxes(colorbar_title='Receita (R$)')

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers = True,
    range_y = (0, df_rec_mensal.max()),
    color = 'Ano',
    line_dash = 'Ano',
    title = 'Receita Mensal'

)

grafico_rec_mensal.update_layout(xaxis_title =None, yaxis_title =None )

grafico_rec_estado = px.bar(
    df_rec_estado.head(7),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top Receita por Estados',
)

grafico_rec_estado.update_layout(xaxis_title =None, yaxis_title =None )

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto = True,
    title = 'Top 7 Categorias com Maior Receita',
)

grafico_rec_categoria.update_layout(xaxis_title =None, yaxis_title =None, showlegend=False)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto = True,
    title = 'Top 7 Vendedores por Receita'
)

grafico_rec_vendedores.update_layout(xaxis_title =None, yaxis_title =None )

grafico_vendas_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto = True,
    title = 'Top 7 Vendedores por Venda'
)

grafico_vendas_vendedores.update_layout(xaxis_title =None, yaxis_title =None)

# Porcentagem de cada vendedor
vendas_pct = (df_vendas_por_vendedor / df_total_vendas) * 100