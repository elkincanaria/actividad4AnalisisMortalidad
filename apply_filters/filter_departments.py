#===================================================================
# SE DEFINE FUNCION DE FILTRO POR DEPARTAMENTOS
#===================================================================
def funcion_filtro(df, departamento):
    if departamento == 'TODOS':
        df_filtrado = df
    else:
        df_filtrado = df[df['DEPARTAMENTO'] == departamento]
    return df_filtrado