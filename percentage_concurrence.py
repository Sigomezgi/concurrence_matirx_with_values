#The elements must be uniques
# Example like what is df.

####
# dict_clients = {}
# fechas= list (abogados["fecha"].unique())

# for i in fechas:
#     dict_clients[i] = list (abogados[abogados["fecha"]== i]["Nit"].unique())# IMPORTANTE TO UNIQUE

# df = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in dict_clients.items()]))



df.corr(method=lambda x, y: len (set(x).intersection(set(y)))/len(set(y)))
