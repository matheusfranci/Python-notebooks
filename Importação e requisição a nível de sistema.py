#!/usr/bin/env python
# coding: utf-8

# In[8]:


import subprocess as sp


# In[9]:


retorno = sp.Popen("ipconfig",stdout=sp.PIPE).communicate()[0]


# In[10]:


type(retorno)


# In[11]:


retorno = retorno.decode("cp850")


# In[12]:


type(retorno)


# In[13]:


print(retorno)


# In[14]:


print("Escolha pelo número do comando desejado")
print("1 - IPCONFIG")
print("2 - PING")
escolha = int(input())


# In[15]:


if escolha == 1:
    retorno = sp.Popen("ipconfig",stdout=sp.PIPE).communicate()[0]
elif escolha ==2:
    local = input("Informe o site ou ip em que deseja realizar o ping: ")
    retorno = sp.Popen(["ping",local], stdout=sp.PIPE).communicate()[0]
else:
    print("Esta opção não existe")


# In[17]:


print(retorno.decode("cp850"))


# In[ ]:





# In[ ]:




