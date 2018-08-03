import pandas as pd
import numpy as np

date_index = pd.date_range('2018/08/01',periods=10,freq='10D')
print(date_index)
df_obj = pd.DataFrame(np.random.randn(10,2),index=date_index,columns=['A','B'])
print(df_obj)
print (df_obj.truncate(before='2018-09'))

print(df_obj.resample('M').sum())
print(df_obj.resample('M').mean())
print(df_obj.resample('D').asfreq())
df_obj['year'] = df_obj[:1]


df_obj['date']  = df_obj.index
df_obj['year'] = df_obj['date'].apply(lambda x: x.year)
df_obj['month'] = df_obj['date'].apply(lambda x: x.month)
df_obj['day'] = df_obj['date'].apply(lambda x: x.day)
print(df_obj)