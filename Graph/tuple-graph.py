from __future__ import division
import os
import re
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline

SPath =os.getcwd()+'/fifty/tenDep.txt'

G= nx.Graph()
H= nx.Graph()

def simDependency(s1, s2, path):
	fb = open(path, 'r')
	
	for a in fb.readlines():
		st= a.split()
		if str(s1) in st:					
			#print(s1, "...", s2, "...", a)
			#print isinstance(a, basestring)
			temp=nx.Graph()
			try:
				w1= a.split()[1]
			except IndexError:
				w1= a.split()[0]
			try:
				rel1=a.split()[2]
			except IndexError:
				rel1=''
			try:
				dep1=a.split()[3]
			except IndexError:
				dep1=''
			if(s1==2 and s2 ==1):
				G.add_nodes_from([w1],sent=1,pos=rel1, dep=dep1 )               
				print(s1, "...", s2, "...", a)                   
			#nx.draw(G, with_labels= True)
			if(s1==2 and s2 ==3):
				H.add_nodes_from([w1],sent=1,pos=rel1, dep=dep1 )                
				print(s1, "...", s2, "...", a)                   
			#nx.draw(G, with_labels= True)
            
            
            
            
outer=1
while(outer <10):
	inner =1
	while(inner<10):		
		if(inner!=outer):
			#fSim = open(SimPath, 'a+b')
			simDependency(inner, outer,SPath)
											
		inner= inner+1
	outer=outer+1

att = nx.get_node_attributes(G,'pos')


att

nx.draw(G, with_labels=True)

nx.is_isomorphic(G, H) 

att = nx.get_node_attributes(K,'Sim')

att
