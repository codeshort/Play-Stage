#!/usr/bin/env python
# coding: utf-8

# # Navigating rdf graphs.
# 

# In[1]:


get_ipython().system('pip install rdflib')


# In[2]:


import rdflib


# In[3]:


g =rdflib.Graph()


# In[4]:


g.parse('http://dbpedia.org/resource/Berlin')


# In[6]:


for s,p,o in g:
    print("subject" , s)
    print("predicate ", p)
    print("object ", o)
    break


# In[7]:


print(len(g))


# In[8]:


#checking if the triple exists


# In[9]:


from rdflib import URIRef


# In[15]:


if(URIRef('http://dbpedia.org/resource/Berlin'),None,None) in g:
    print('Triple exists!!')
else:
    print('Triple does not exists!')


# In[16]:


#get list of properties


# In[17]:


from rdflib.namespace import RDF, OWL, RDFS, FOAF

properties = set()


# In[21]:


for s,p,o in g:
    properties.add(p)

from pprint import pprint
pprint(properties)


# In[24]:


len(properties)


# In[25]:


#Iterating over labels


# In[30]:


for s,o in g.subject_objects(RDFS.label):
    print(o.value, o.language ,o.datatype)


# In[31]:


for s,o in g.subject_objects(OWL.sameAs):
    print(o)


# In[36]:



population = URIRef('http://dbpedia.org/ontology/populationTotal')


# In[37]:


for o in g.objects(None, RDFS.label):
    print(o)


# In[38]:


for o in g.objects(None, population):
    print(o)


# In[39]:


from rdflib import Namespace


# In[40]:


DBO = Namespace('http://dbpedia.org/ontology/')
DBR = Namespace('http://dbpedia.org/resource/')


# In[43]:


print(g.value(DBR['Berlin'], DBO['populationMetro'],None))


# In[46]:


print(g.value(DBR['Berlin'], RDFS.label ,None))


# In[47]:


print(g.value(DBR['Berlin'], RDFS.label ,None).language)


# In[ ]:




