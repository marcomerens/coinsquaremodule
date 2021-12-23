#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
import time
import json


# In[19]:


now=round(time.time()*1000)


# In[20]:


r=requests.get("https://api.coinsquare.com/winterfell/v1/data/quotes?cacheBuster="+str(now))


# In[21]:


quotes=json.loads(r.text)


# In[22]:


currencies=["BTC"]
bases=["BTC"]
for i in quotes["quotes"]:
    if i["base"]=="BTC":
        currencies.append(i["ticker"])
    else:
        bases.append(i["base"])
        


# In[23]:


q=[]
for curr in currencies:
    for base in bases:
        if base!=curr:
            if base=="BTC":
                i = [x for x in quotes["quotes"] if x["ticker"] == curr and x["base"]=="BTC"][0]
                el={"currency":curr,"base":"BTC","ret_24h_pc":round(100*float(i["ret24"]),2),"value":round(float(i["last"])/100000000,2),"tstamp":now}
            elif curr== "BTC":
                b=[x for x in quotes["quotes"] if x["ticker"] == "BTC" and x["base"]==base][0]
                el={"currency":curr,"base":base,
                    "ret_24h_pc":round(100*float(b["ret24"]),2),
                    "value":round(float(b["last"])/100,2),
                   "tstamp":now}
            
            else:
                c = [x for x in quotes["quotes"] if x["ticker"] == curr and x["base"]=="BTC"][0]
                b=[x for x in quotes["quotes"] if x["ticker"] == "BTC" and x["base"]==base][0]
                el={"currency":curr,"base":base,
                    "ret_24h_pc":round(100*((float(c["ret24"])+1)*(float(b["ret24"])+1)-1),2),
                    "value":round(float(c["last"])*float(b["last"])/100000000/100,2),"tstamp":now}
            q.append(el)


# In[24]:


print(json.dumps(q))


# In[ ]:




