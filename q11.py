##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl2.tsv', sep = '\t',thousands = None, decimal = '.')
tbl2 = pd.DataFrame(x)

ordenados = tbl2.sort_values(by=['_c0','_c5a','_c5b'])
ordenados['union_c5a_c5b'] = ordenados['_c5a'] +':'+ ordenados['_c5b'].map(str)
dflista = ordenados[['_c0','union_c5a_c5b']]
grupo_dflista = dflista.groupby('_c0')['union_c5a_c5b'].apply(list)
merge_dflista = pd.merge(dflista[['_c0']],grupo_dflista,on='_c0')

def concatenar(list):
    result= ''
    for index, value in enumerate(list,1):
        if index < len(list):
            result += str(value)+','
        else:
            result += str(value)
    return result

merge_dflista['lista']= merge_dflista['union_c5a_c5b'].map(lambda x: concatenar(x))
filasunicas = merge_dflista[['_c0','lista']].drop_duplicates()
filasunicas = filasunicas.reset_index(drop=True)
print(filasunicas)
