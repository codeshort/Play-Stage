#!/usr/bin/env python
# coding: utf-8

# In[2]:


from rdflib import URIRef ,BNode,Literal,Namespace
from rdflib.namespace import FOAF,DCTERMS,XSD,RDF,SDO


# In[4]:


mona_lisa = URIRef('http://www.wikidata.org/entity/Q12418')
davinci = URIRef('http://dbpedia.org/resource/Leonardo_Da_Vinci')
lajoconde= URIRef('http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619')


# In[20]:


EX = Namespace('http://example.org/')
bob = EX['Bob']
alice = EX['Alice']

birth_date = Literal("1990-07-04",datatype = XSD.date)
title = Literal('Mona Lisa', lang ="en")


# In[21]:


title.value


# In[22]:


from rdflib import Graph
g = Graph()


# In[23]:


g.add((bob, RDF.type,FOAF.Person))
g.add((bob, FOAF.knows, Alice))
g.add((bob, FOAF['topic_interest'],mona_lisa))
g.add((bob,SDO['birthDate'], birth_date))
g.add((mona_lisa,DCTERMS['creator'],davinci))
g.add((mona_lisa,DCTERMS['title'],title))
g.add((lajoconde,DCTERMS['subject'],mona_lisa))


# In[24]:


print(g.serialize(format = 'ttl').decode('u8'))


# In[25]:


for prefix,ns in g.namespaces():
    print(prefix, " ", ns)
    


# In[26]:


#Replcing literal values:
g.set((bob,SDO['birthdate'],Literal('1990-01-01',datatype = XSD.date)))
g.set((mona_lisa,DCTERMS['title'],Literal('La Joconde',lang ='fr')))


# In[27]:


print(g.serialize(format = 'ttl').decode('u8'))


# In[28]:


g.remove((lajoconde,None,None))


# In[29]:


print(g.serialize(format = 'ttl').decode('u8'))


# In[30]:


g.remove((mona_lisa,None,None))


# In[31]:


print(g.serialize(format = 'ttl').decode('u8'))


# In[ ]:




