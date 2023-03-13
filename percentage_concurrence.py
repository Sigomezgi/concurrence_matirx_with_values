df.corr(method=lambda x, y: len (set(x).intersection(set(y)))/len(set(x)))
