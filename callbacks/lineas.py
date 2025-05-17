from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE GRAFICO DE LINEAS
#===================================================================
@callback(
    Output('grafico_lineas', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualiza_lineas(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    df_conteo = df_filtrado.groupby('MES').size().reset_index(name='CANTIDAD_MUERTES')
    fig = px.line(df_conteo, x='MES', y='CANTIDAD_MUERTES',
                  title='Cantidad de muertes por mes en Colombia',
                  labels={'MES': 'Mes', 'CANTIDAD_MUERTES': 'Cantidad de muertes'})
    return fig