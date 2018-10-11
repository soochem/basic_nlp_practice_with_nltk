# Inflearn pandas L1

import pandas as pd

data_frame = pd.read_csv('data/friend_list.csv')
print(data_frame)
print(data_frame.head(2)) #2개만 보겠다
data_frame.tail(2) #2개만 보겠다
print(type(data_frame.name)) #type이 series -> column, df는 series의 집합체

list_temp = [1,2,3]
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series(['one', 'two', 'three'])
df = pd.DataFrame(data=dict(num=s1, word=s2))
print(df)
