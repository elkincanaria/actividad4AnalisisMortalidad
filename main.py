from dash import Dash
from layout import create_layout
import data_process

app = Dash(__name__)
df = data_process.consolidacion_mortalidad()
app.layout = create_layout(df)

# Importa todos los callbacks
import callbacks.lineas 
import callbacks.mapa
import callbacks.barras_violencia
import callbacks.circular
import callbacks.tabla
import callbacks.histograma
import callbacks.apiladas

if __name__ == '__main__':
    app.run(debug=True)