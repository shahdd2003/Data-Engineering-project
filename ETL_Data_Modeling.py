import pandas as pd

dfeg=pd.read_csv("abfss://##@#######.dfs.core.windows.net/PData.csv")


dfsa=pd.read_csv("abfss://##@#######.dfs.core.windows.net/PData_SA.csv")
dfnl=pd.read_csv("abfss://##@#######.dfs.core.windows.net/PData_NL.csv")


dfeg['Region']='Egypt'
dfsa['Region']='Saudi Arabia'
dfnl['Region']="Netherlands"
dfsa.drop(columns=['refresh rate'], inplace=True)
dfeg.drop(columns=['refresh rate'], inplace=True)
dfnl.drop(columns=['refresh rate'], inplace=True)

df=pd.concat([dfnl,dfsa,dfeg],ignore_index=True)
df
b={}
db=df['brand']
db=db.unique()
db

for i in range(len(db)):
    b[db[i]]=i

s={}
sb=df['storage']
sb=sb.unique()
sb

for i in range(len(sb)):
    s[sb[i]]=i


c={}
cb=df['color']
cb=cb.unique()
cb

for i in range(len(cb)):
    c[cb[i]]=i

m={}
mb=df['model']
mb=mb.unique()
mb

for i in range(len(mb)):
    m[mb[i]]=i

o={}
ob=df['os']
ob=ob.unique()
ob

p={}
pb=df['cpu']
pb=pb.unique()
pb

for i in range(len(pb)):
    p[pb[i]]=i
   

for i in range(len(ob)):
    
    o[ob[i]]=i


w={}
wb=df['website']
wb=wb.unique()
wb

for i in range(len(wb)):
    
    w[wb[i]]=i


#screansize and resltion and concat to reslution id 

scr={}
scb=df['screen size']
scb=scb.unique()
scb

for i in range(len(scb)):
    
    scr[scb[i]]=i

for i in range(len(res)):
    
    rs[res[i]]=i

#wire provie and wire tech and cellular
wpt={}
wptb=df['wireless provider']
wptb=wptb.unique()
wptb

for i in range(len(wptb)):
    
    wpt[wptb[i]]=i

wtt={}
wttb=df['wireless technology']
wttb=wttb.unique()
wttb

for i in range(len(wttb)):
    
    wtt[wttb[i]]=i


ctt={}
cttb=df['cellular technology']
cttb=cttb.unique()
cttb

for i in range(len(cttb)):
    
    ctt[cttb[i]]=i

import copy

df_cpy=copy.deepcopy(df)

df_cpy['Brand'] = df_cpy['brand'].map(b)
df_cpy['OS'] = df_cpy['os'].map(o)
df_cpy['Model'] = df_cpy['model'].map(m)
df_cpy['Cpu'] = df_cpy['cpu'].map(p)
df_cpy['Color'] = df_cpy['color'].map(c)
df_cpy['Storage'] = df_cpy['storage'].map(s)
df_cpy['Website'] = df_cpy['website'].map(w)

df_cpy['Screen Size'] = df_cpy['screen size'].map(scr)
df_cpy['Wireless Provider'] = df_cpy['wireless provider'].map(wpt)
df_cpy['Wireless Technology'] = df_cpy['wireless technology'].map(wtt)
df_cpy['Cellular Technology'] = df_cpy['cellular technology'].map(ctt)
df_cpy


df_cpy['product_id'] = df_cpy[['OS', 'Model', 'Cpu','Brand','Storage','Color']].astype(str).agg('-'.join, axis=1)
df_cpy
df_cpy['resolution_id'] = df_cpy[['Screen Size']].astype(str).agg('-'.join, axis=1)


df_cpy['tech_spec_id'] = df_cpy[['Wireless Provider', 'Wireless Technology','Cellular Technology']].astype(str).agg('-'.join, axis=1)


df['product_id']=df_cpy['product_id']
df['resolution_id']=df_cpy['resolution_id']
df['tech_spec_id']=df_cpy['tech_spec_id']
df['website_id']=df_cpy['Website']
df
df_cpy['website_id']=df_cpy['Website']

new_column_names = {
    'Region': 'region',
    'Brand': 'brand_id',
    'OS': 'os_id',
    'Model': 'model_id',
    'Cpu': 'cpu_id',
    'Color': 'color_id',
    'Storage': 'storage_id',
    'Website': 'website_id',
    'Screen Size': 'screen size_id',
    'Wireless Provider': 'wireless provider_id',
    'Wireless Technology': 'wireless technology_id',
    'Cellular Technology': 'cellular technology_id'
    
}

df_cpy.rename(columns=new_column_names, inplace=True)
df_cpy.columns
#df_cpy.drop(columns=['ProductID'], inplace=True)

#df_cpy.drop(columns=['ProductID'], inplace=True)
df_cpy.rename(columns={'Resolution ID':'resolution_id2f'}, inplace=True)

df_cpy.columns
df_cpy.rename(columns={'Resolution ID':'resolution_id2f'}, inplace=True)
df_cpy
df_cpy.columns

df_cpy.drop(columns=['website_id'], inplace=True)

df_cpy['website_id'] = df_cpy['website'].map(w)

df=df_cpy
df['product_id'] = df['product_id'].astype(str)
df['resolution_id'] = df['resolution_id'].astype(str)
df['tech_spec_id'] = df['tech_spec_id'].astype(str)
df['website_id'] = df['website_id'].astype(str)

df.columns
fact=df[['product_id','resolution_id','tech_spec_id','website_id','cellular technology_id','wireless technology_id','wireless provider_id','brand_id', 'os_id', 'model_id', 'cpu_id', 'color_id',
       'storage_id', 'screen size_id', 'resolution_id2f','price', 'price before promotion', 'rate']]
product=df[['title', 'brand', 'os', 'ram', 'cpu', 'storage', 'model', 'color','camera', 'img','product_id']]
reso=df[[ 'width resolution', 'height resolution','screen size','resolution_id']]
webs=df[[ 'url', 'reviews','region','website','currancy','website_id' ]]
tecsp=df[['wireless technology','wireless provider',
       'cellular technology', 'sim count','tech_spec_id']]

       
webs
fact.to_parquet('abfss://######@######.dfs.core.windows.net/Fact_Table.parquet', index=False)
product.to_parquet('abfss://######@######.dfs.core.windows.net/Product_Dimsion.parquet', index=False)
reso.to_parquet('abfss://######@######.dfs.core.windows.net/Resolution_Dimsion.parquet', index=False)
webs.to_parquet('abfss://######@######.dfs.core.windows.net/Website_Dimsion.parquet', index=False)
tecsp.to_parquet('abfss://######@######.dfs.core.windows.net/Tech_special_Dimion.parquet', index=False)
