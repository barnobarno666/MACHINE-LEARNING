import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv('data.csv')
data=data.sort_values('price',ascending=False)
#datas=data.pivot_table(values='price',index='city',columns='bedrooms')

datas=data.groupby('city')['price'].mean()
#datas=datas.sort_index('price')
#datas=datas.iloc[0:10]
data.plot(kind='line',y='price',x='city',title='hello',rot=45)
plt.show()
#datas.to_csv('matplotlibhaj.csv')