from datetime import datetime

now = datetime.now()

#date format
now.strftime('%Y/%m/%d')

dt_obj = datetime(2018,8,1)
print (dt_obj)
print (str(dt_obj))
dt_str = '2018/7/31'
dt_obj2 = datetime.strptime(dt_str,'%Y/%m/%d')
print (dt_obj2)
print (now)

import pandas as pd
s_obj = pd.Series(['2017/02/18', '2017/02/19', '2017-02-25', '2017-02-26'], name='course_time')
pd.to_datetime(s_obj)

