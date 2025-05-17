from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
#===================================================================
# SE CONSTRUYE TABLA
#===================================================================
@callback(
    Output('tabla_causas', 'children'),
    Input('dropdown_departamento', 'value')
)
def tabla_causas_principales(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    causas = df_filtrado.groupby(['COD_MUERTE', 'DESCRIPCION TRES CARACTERES']).size().reset_index(name='TOTAL')
    causas = causas.sort_values(by='TOTAL', ascending=False).head(10)
    return html.Table([
        html.Tr([html.Th(col) for col in causas.columns])
    ] + [
        html.Tr([html.Td(causas.iloc[i][col]) for col in causas.columns]) for i in range(len(causas))
    ])