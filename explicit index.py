import pandas as pd
datas=pd.read_csv('data.csv')
data=datas.set_index(['city','bedrooms'])
#data.reset_index(drop=True)

y=data.loc[[('Snoqualmie',5),('Seattle',4)]]

#y=data.loc[[5,6]]
y.sort_index(leve)
y.reset_index()
y.sort_index()
y.to_csv('index.csv')
