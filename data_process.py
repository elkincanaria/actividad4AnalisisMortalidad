import pandas as pd
from functools import lru_cache
@lru_cache()
def consolidacion_mortalidad():
    df_mortalidad = pd.read_excel("resources/Anexo1.NoFetal2019_CE_15-03-23.xlsx")
    dim_causa= pd.read_excel("resources/Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx", skiprows=8)
    dim_divipola = pd.read_excel("resources/Anexo3.Divipola_CE_15-03-23.xlsx")
    dim_causa=dim_causa.rename(columns={"Capítulo":"CAPITULO",
                                        "Nombre capítulo":"NOMBRE CAPITULO",
                                        "Código de la CIE-10 tres caracteres": "COD_MUERTE",
                                        "Descripción  de códigos mortalidad a tres caracteres": "DESCRIPCION TRES CARACTERES",
                                        "Código de la CIE-10 cuatro caracteres": "CIE CUATRO CARACTERES",
                                        "Descripcion  de códigos mortalidad a cuatro caracteres": "DESCRIPCION CUATRO CARACTERES"})
    dim_causa=dim_causa.drop_duplicates(subset="COD_MUERTE")[["CAPITULO", "NOMBRE CAPITULO", "COD_MUERTE", "DESCRIPCION TRES CARACTERES"]]
    df_mortalidad["COD_MUERTE"]=df_mortalidad["COD_MUERTE"].str[0:3]
    mergeaux = pd.merge(right=df_mortalidad,
                    left=dim_divipola,
                    on=["COD_DANE", "COD_DEPARTAMENTO", "COD_MUNICIPIO"],
                    how="inner")
    data_consolidada = pd.merge(right=mergeaux,
                    left=dim_causa,
                    on="COD_MUERTE",
                    how="inner")
    return data_consolidada

