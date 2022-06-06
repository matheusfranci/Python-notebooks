#!/usr/bin/env python
# coding: utf-8

# In[1]:


valor = input("Digite um valor a classificar: ")


# In[2]:


type(valor)


# In[4]:


valor = int(valor)


# In[6]:


type(valor)


# In[7]:


resto = valor % 2
if resto == 0:
    print("O número é par")
else:
    print("O número é impar")


# In[10]:


print("Este é o valor digitado: {}".format(valor))


# In[11]:


print("Este é o valor digitado {}, e o resto da divisão é {}".format(valor,resto))


# In[13]:


print("Este é o valor digitado {v1}, e o resto da divisão de {v1} por 2 é igual a {v2}".format(v1=valor,v2=resto))


# In[18]:


print("Este é o valor da divisão de {} por 2 {:.3f}".format(valor, (valor/2)))


# In[ ]:




