from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE GRAFICO CIRCULAR
#===================================================================
@callback(
    Output('grafico_circular', 'figure'),
    Input('dropdown_departamento', 'value')
)
def ciudades_menor_mortalidad(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    mortalidad = df_filtrado.groupby('MUNICIPIO').size().reset_index(name='MENOR_MORTALIDAD')
    bottom10 = mortalidad.sort_values(by='MENOR_MORTALIDAD').head(10)
    fig = px.pie(bottom10, names='MUNICIPIO', values='MENOR_MORTALIDAD', title='10 Ciudades con menor índice de mortalidad')
    return fig