import pandas as pd
import numpy as np
datas=pd.read_csv('data.csv')
data=datas.pivot_table(values='price',index='city',columns='bedrooms',fill_value=0,aggfunc=np.mean,margins=min,sort=True)
#data=data[]
data.to_csv('pivot_test.csv',index=True)