from dash import Dash, html, dcc, callback, Output, Input 
import plotly.express as px
from main import df
from apply_filters.filter_departments import funcion_filtro
import json
from functools import lru_cache
#===================================================================
# SE CONSTRUYE GRAFICO DE MAPA 
#===================================================================
@lru_cache()
def cargar_geojson():
    with open("resources/departamento24.geojson", "r", encoding="utf-8") as f:
        return json.load(f)

@callback(
    Output('grafico_mapa', 'figure'),
    Input('dropdown_departamento', 'value')
)
def actualiza_mapa(departamento):
    df_filtrado = funcion_filtro(df, departamento)
    geojson_colombia = cargar_geojson()
    df_conteo= df_filtrado.groupby('DEPARTAMENTO').size().reset_index(name='MUERTES')
    fig = px.choropleth(
        df_conteo,
        geojson=geojson_colombia,
        locations='DEPARTAMENTO',
        featureidkey='properties.NOMBRE_DPT',  # Asegúrate de que este campo coincida con el del GeoJSON
        color='MUERTES',
        color_continuous_scale=["green", "yellow", "red"],
        title='Distribución de muertes por departamento - 2019'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig