from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE GRAFICO APILADAS 
#===================================================================
@callback(
    Output('grafico_apiladas', 'figure'),
    Input('dropdown_departamento', 'value')
)
def muertes_por_sexo_y_departamento(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    conteo = df_filtrado.groupby(['DEPARTAMENTO', 'SEXO']).size().reset_index(name='MUERTES')
    fig = px.bar(conteo, x='DEPARTAMENTO', y='MUERTES', color='SEXO',
                 title='Muertes por sexo y departamento', barmode='stack')
    return fig