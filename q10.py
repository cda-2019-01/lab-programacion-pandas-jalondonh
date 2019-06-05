##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl1.tsv', sep = '\t',thousands = None, decimal = '.')
tbl1 = pd.DataFrame(x)
ordenados = tbl1.sort_values(by=['_c0','_c4'])
gruponumero = ordenados.groupby('_c0')['_c4'].apply(list)
mergegruponumero = pd.merge(ordenados[['_c0']],gruponumero,on='_c0')
def concatenar(list):
    result= ''
    for index, value in enumerate(list,1):
        if index < len(list):
            result += str(value)+','
        else:
            result += str(value)
    return result

mergegruponumero['lista']= mergegruponumero['_c4'].map(lambda x: concatenar(x))
filasunicas = mergegruponumero[['_c0','lista']].drop_duplicates()
filasunicas = filasunicas.reset_index(drop=True)
print(filasunicas)
