import pandas as pd
import numpy as np
dataimport1=pd.read_csv(r"E:\Downloads\WIFI_MLP.csv")
dataimport2=pd.read_csv(r"E:\Downloads\TV_MLP.csv")
dataimport3=pd.read_csv(r"E:\Downloads\Refrigerator_MLP.csv")
dataimport4=pd.read_csv(r"E:\Downloads\LAPTOP_SYSTEM_MLP.csv")
dataimport5=pd.read_csv(r"E:\Downloads\inverter_MLP.csv")
dataimport6=pd.read_csv(r"E:\Downloads\E-VEHICLE_MLP.csv")
dataimport7=pd.read_csv(r"E:\Downloads\ac_MLP.csv")
dataimport1['value'] = dataimport1['value'].replace(np.nan, 1)
dataimport2['value'] = dataimport2['value'].replace(np.nan, 1)
dataimport3['value'] = dataimport3['value'].replace(np.nan, 1)
dataimport4['value'] = dataimport4['value'].replace(np.nan, 1)
dataimport5['value'] = dataimport5['value'].replace(np.nan, 1)
dataimport6['value'] = dataimport6['value'].replace(np.nan, 1)
dataimport7['value'] = dataimport7['value'].replace(np.nan, 1)
Type_new = pd.Series([])
k=10001
r=10001
rk=10004
for i in range(len(dataimport1)):
    if dataimport1["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport1["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport1.insert(4, "info_id", Type_new) 
for i in range(len(dataimport2)):
    if dataimport2["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport2["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport2.insert(4, "info_id", Type_new) 
for i in range(len(dataimport3)):
    if dataimport3["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport3["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport3.insert(4, "info_id", Type_new) 
for i in range(len(dataimport4)):
    if dataimport4["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport4["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport4.insert(4, "info_id", Type_new) 
for i in range(len(dataimport5)):
    if dataimport5["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport5["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport5.insert(4, "info_id", Type_new) 
for i in range(len(dataimport6)):
    if dataimport6["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport6["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport6.insert(4, "info_id", Type_new) 
for i in range(len(dataimport7)):
    if dataimport7["value"][i] == 1:
        k
        Type_new[i]=str(k)
        k+=1
    elif dataimport7["value"][i] == 0:
        r
        Type_new[i]=str(r)
        r+=1
dataimport7.insert(4, "info_id", Type_new)
df1=dataimport1
df1.created_at=df1.created_at.astype(str)
df1['created_at'] = pd.to_datetime(df1.created_at.str.split(',\s*').str[0])
v=set(df1['created_at'].dt.tz_localize(tz = None))
df1["created_at"].replace=v
print(df1)
df2=dataimport2
df2.created_at=df2.created_at.astype(str)
df2['created_at'] = pd.to_datetime(df2.created_at.str.split(',\s*').str[0])
v=set(df2['created_at'].dt.tz_localize(tz = None))
df2["created_at"].replace=v
print(df2)
df3=dataimport3
df3.created_at=df3.created_at.astype(str)
df3['created_at'] = pd.to_datetime(df3.created_at.str.split(',\s*').str[0])
v=set(df3['created_at'].dt.tz_localize(tz = None))
df3["created_at"].replace=v
print(df3)
df4=dataimport4
df4.created_at=df4.created_at.astype(str)
df4['created_at'] = pd.to_datetime(df4.created_at.str.split(',\s*').str[0])
v=set(df4['created_at'].dt.tz_localize(tz = None))
df4["created_at"].replace=v
print(df4)
df5=dataimport5
df5.created_at=df5.created_at.astype(str)
df5['created_at'] = pd.to_datetime(df5.created_at.str.split(',\s*').str[0])
v=set(df5['created_at'].dt.tz_localize(tz = None))
df5["created_at"].replace=v
print(df5)
df6=dataimport6
df6.created_at=df6.created_at.astype(str)
df6['created_at'] = pd.to_datetime(df6.created_at.str.split(',\s*').str[0])
v=set(df6['created_at'].dt.tz_localize(tz = None))
df6["created_at"].replace=v
print(df6)
df7=dataimport7
df7.created_at=df7.created_at.astype(str)
df7['created_at'] = pd.to_datetime(df7.created_at.str.split(',\s*').str[0])
v=set(df7['created_at'].dt.tz_localize(tz = None))
df7["created_at"].replace=v
print(df7)


from sklearn.preprocessing import OrdinalEncoder
ord1 = OrdinalEncoder()
# fitting encoder
ord1.fit([df1['info_id']])
# tranforming the column after fitting
df1["info_id"]= ord1.fit_transform(df1[["info_id"]])

ord2 = OrdinalEncoder()
# fitting encoder
ord2.fit([df2['info_id']])
# tranforming the column after fitting
df2["info_id"]= ord2.fit_transform(df2[["info_id"]])

ord3 = OrdinalEncoder()
# fitting encoder
ord3.fit([df3['info_id']])
# tranforming the column after fitting
df3["info_id"]= ord3.fit_transform(df3[["info_id"]])

ord4 = OrdinalEncoder()
# fitting encoder
ord4.fit([df4['info_id']])
# tranforming the column after fitting
df4["info_id"]= ord4.fit_transform(df4[["info_id"]])

ord5 = OrdinalEncoder()
# fitting encoder
ord5.fit([df5['info_id']])
# tranforming the column after fitting
df5["info_id"]= ord5.fit_transform(df5[["info_id"]])

ord6 = OrdinalEncoder()
# fitting encoder
ord6.fit([df6['info_id']])
# tranforming the column after fitting
df6["info_id"]= ord6.fit_transform(df6[["info_id"]])

ord7 = OrdinalEncoder()
# fitting encoder
ord7.fit([df7['info_id']])
# tranforming the column after fitting
df7["info_id"]= ord7.fit_transform(df7[["info_id"]])

df1["info_id X"] = df1["info_id"].shift()
df2["info_id X"] = df2["info_id"].shift()
df3["info_id X"] = df3["info_id"].shift()
df4["info_id X"] = df4["info_id"].shift()
df5["info_id X"] = df5["info_id"].shift()
df6["info_id X"] = df6["info_id"].shift()
df7["info_id X"] = df7["info_id"].shift()

df1["cumsum"] = (df1["info_id"] != df1["info_id X"]).cumsum()
df2["cumsum"] = (df2["info_id"] != df2["info_id X"]).cumsum()
df3["cumsum"] = (df3["info_id"] != df3["info_id X"]).cumsum()
df4["cumsum"] = (df4["info_id"] != df4["info_id X"]).cumsum()
df5["cumsum"] = (df5["info_id"] != df5["info_id X"]).cumsum()
df6["cumsum"] = (df6["info_id"] != df6["info_id X"]).cumsum()
df7["cumsum"] = (df7["info_id"] != df7["info_id X"]).cumsum()

dg1=df1.groupby((df1["info_id"] != df1["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg2=df2.groupby((df2["info_id"] != df2["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg3=df3.groupby((df3["info_id"] != df3["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg4=df4.groupby((df4["info_id"] != df4["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg5=df5.groupby((df5["info_id"] != df5["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg6=df6.groupby((df6["info_id"] != df6["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})
dg7=df7.groupby((df7["info_id"] != df7["info_id"].shift()).cumsum()).agg({"created_at" : ["min", "max"]})

dg1.columns=['a','b']
dg2.columns=['a','b']
dg3.columns=['a','b']
dg4.columns=['a','b']
dg5.columns=['a','b']
dg6.columns=['a','b']
dg7.columns=['a','b']
print(dg1)
print(dg2)
print(dg3)
print(dg4)
print(dg5)
print(dg6)
print(dg7)

