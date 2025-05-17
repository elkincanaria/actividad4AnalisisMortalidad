from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
import pandas as pd
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE HISTOGRAMA
#===================================================================
@callback(
    Output('grafico_histograma', 'figure'),
    Input('dropdown_departamento', 'value')
)
def histograma_edades(departamento):
    bins = list(range(0, 90, 5)) + [120]
    labels = [f"{i}-{i+4}" for i in range(0, 85, 5)] + ['85+']
    df_filtrado = funcion_filtro(df, departamento)
    df_filtrado['GRUPO_EDAD1'] = pd.to_numeric(df_filtrado['GRUPO_EDAD1'], errors='coerce')
    df_filtrado['RANGO_EDAD'] = pd.cut(df_filtrado['GRUPO_EDAD1'], bins=bins, labels=labels, right=False)
    conteo = df_filtrado.groupby('RANGO_EDAD').size().reset_index(name='MUERTES')
    fig = px.bar(conteo, x='RANGO_EDAD', y='MUERTES', title='Distribución de muertes por rango de edad')
    return fig