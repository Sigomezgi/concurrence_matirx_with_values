import pandas as pd
import numpy as np

#The elements must be uniques
# Example like what is df.

####
# dict_clients = {}
# fechas= list (abogados["fecha"].unique())

# for i in fechas:
#     dict_clients[i] = list (abogados[abogados["fecha"]== i]["Nit"].unique())# IMPORTANTE TO UNIQUE

# df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in dict_clients.items()]))



df_corr = df.corr(method=lambda x, y: len (set(x).intersection(set(y)))/len(set(y)))
mask = np.tril(np.ones_like(df_corr, dtype=bool), k=-1)
df_corr= df_corr.mask(mask,0)
