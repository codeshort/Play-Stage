#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install rdflib')


# In[2]:


get_ipython().system('pip show rdflib ')


# In[6]:


#importing graph 
from rdflib import Graph 


# In[7]:


#initialize a graph 


# In[9]:


g = Graph()


# In[17]:


g.parse('http://dbpedia.org/resource/Michael_Jackson')


# In[21]:


for index, (sub,pred,obj) in enumerate(g):
    print(pred)
    if(index==10):
        break
    


# In[24]:


#print size of graph
print(f'graph has {len(g)} facts')


# In[25]:


print(g.serialize(format='ttl').decode('u8'))


# # Example - 2

# In[26]:


from rdflib import Graph,Literal,RDF,URIRef
from rdflib.namespace import FOAF,XSD


# In[27]:


g = Graph()


# In[28]:


#creating a URI node to be used for triples of multiple nodes
mason = URIRef("http://example.org/mason")


# In[53]:


#addiing triples
g.add((mason,RDF.type,FOAF.Person))
g.add((mason,FOAF.nick,Literal("mason", lang="en")))
g.add((mason,FOAF.name,Literal("Mason Carter")))
g.add((mason,FOAF.mbox,URIRef("mailto:mason@exampl.org")))


# In[54]:


#creating a URI node to be used for triples of multiple nodes
shyla = URIRef("http://example.org/shyla")


# In[55]:


#addiing triples
g.add((shyla,RDF.type,FOAF.Person))
g.add((shyla,FOAF.nick,Literal("shilli", datatype="XSD.string")))
g.add((shyla,FOAF.name,Literal("Shyla Bond")))
g.add((shyla,FOAF.mbox,URIRef("mailto:shyla@exampl.org")))


# In[56]:


for (s,p,o) in g:
    print(s,p,o)


# In[57]:


#accessing only nicknames out of all 
#for each foaf:person value , print out their nickname


# In[61]:


for person in g.subjects(RDF.type,FOAF.Person):
    print("person is ", person)
    for nick in g.objects(person, FOAF.nick):
        print(nick)


# In[62]:


g.bind("foaf",FOAF)


# In[63]:


#printing in n3 format
print(g.serialize(format='n3').decode("utf-8"))


# In[ ]:




