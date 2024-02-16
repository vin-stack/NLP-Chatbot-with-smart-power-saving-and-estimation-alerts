import pandas as pd
import numpy as np
dataimport=pd.read_csv(r"E:\Downloads\WIFI - Sheet1.csv")
dataimport['value'] = dataimport['value'].replace(np.nan, 1)
Type_new = pd.Series([])
k=10001
r=10001
rk=10004
for i in range(len(dataimport)):
    if dataimport["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport.insert(4, "info_id", Type_new) 
df=dataimport
df.created_at=df.created_at.astype(str)
df['created_at'] = pd.to_datetime(df.created_at.str.split(',\s*').str[0])
v=set(df['created_at'].dt.tz_localize(tz = None))
df["created_at"].replace=v
from sklearn.preprocessing import OrdinalEncoder
ord1 = OrdinalEncoder()
# fitting encoder
ord1.fit([df['info_id']])
# tranforming the column after fitting
df["info_id"]= ord1.fit_transform(df[["info_id"]])
df["info_id X"] = df["info_id"].shift()
df["info_id"] != df["info_id X"]
df["cumsum"] = (df["info_id"] != df["info_id X"]).cumsum()
dg=df.groupby((df["info_id"] != df["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg.columns=['a','b']
difference=dg['b']-dg['a']
dg["days"]=difference
import numpy as np
td=dg["days"].sum()
dg["hours"]=dg["days"]/np.timedelta64(1,'h')
dg["units"]=dg["hours"]*0.018
total_units = dg["units"].sum()
dg["price"]=dg["units"]*5.25
total_price=dg["price"].sum()
print("your wifi power consumption is:",total_price)

