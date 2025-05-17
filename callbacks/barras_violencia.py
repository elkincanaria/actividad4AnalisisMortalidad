from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE GRAFICO DE BARRAS
#===================================================================
@callback(
    Output('grafico_barras_violencia', 'figure'),
    Input('dropdown_departamento', 'value')
)
def ciudades_mas_violentas(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    homicidios = df_filtrado[df_filtrado['COD_MUERTE'].isin(['X95'])]
    top5 = homicidios.groupby('MUNICIPIO').size().reset_index(name='HOMICIDIOS')
    top5 = top5.sort_values(by='HOMICIDIOS', ascending=False).head(5)
    fig = px.bar(top5, x='MUNICIPIO', y='HOMICIDIOS', title='5 Ciudades más violentas (Homicidios)')
    return fig