from dash import html, dcc
import numpy as np

def create_layout(df):
    return html.Div([
        html.H1("Dashboard Análisis de Mortalidad en Colombia", style={'text-align': 'center'}),
        dcc.Dropdown(
            np.append('TODOS', df.DEPARTAMENTO.sort_values().unique()),
            'TODOS',
            id='dropdown_departamento'
        ),
        dcc.Tabs([
            dcc.Tab(label='Líneas - Muertes por Mes', children=[dcc.Graph(id='grafico_lineas')]),
            dcc.Tab(label='Mapa - Muertes por Departamento', children=[dcc.Graph(id='grafico_mapa')]),
            dcc.Tab(label='Barras - 5 Ciudades Más Violentas', children=[dcc.Graph(id='grafico_barras_violencia')]),
            dcc.Tab(label='Circular - 10 Ciudades con Menor Mortalidad', children=[dcc.Graph(id='grafico_circular')]),
            dcc.Tab(label='Tabla - Principales Causas de Muerte', children=[html.Div(id='tabla_causas')]),
            dcc.Tab(label='Histograma - Rango de Edad', children=[dcc.Graph(id='grafico_histograma')]),
            dcc.Tab(label='Barras Apiladas - Sexo por Departamento', children=[dcc.Graph(id='grafico_apiladas')]),
        ])
    ])