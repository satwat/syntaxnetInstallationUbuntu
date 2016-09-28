from __future__ import division
import os



SimPath =os.getcwd()+'/Stemmed/SimilaritytenResult.txt'

SPath =os.getcwd()+'/Stemmed/stemtenDep.txt'


def simDependency(s1,s2,path):
	fb = open(path, 'r')	
	for i, x in enumerate(fb):
		if i == s1:
			print("x "+x)	
	for j, y in enumerate(fb):
		if j == s2:
			print("y ")
		


def getS(s1,path):
	fb = open(path, 'r')	
	for i, x in enumerate(fb):
		if(s1== i):
			return x


fSim = open(SimPath, 'a+b')
#simDependency(SPath)

fb = open(SPath, 'r')

len = sum(1 for _ in fb)	
print(len)

def simChk(cc1,cc2,i,j):
	num1=i.split()[0]
	w1= i.split()[1]
	rel1=i.split()[2]
	dep1=i.split()[3]

	num2=j.split()[0]
	w2= j.split()[1]
	rel2=j.split()[2]
	dep2=j.split()[3]

	Simchk=0			
	score=0
	#print("nuu ",cc1,cc2)
	if(cc1==int(num1) and cc2== int(num2)):
		#print(cc1,cc2)
		if(w1==w2):
			Simchk=Simchk+1
			if(rel1==rel2):
				Simchk=Simchk+1
			if(dep1==dep2):
				Simchk=Simchk+1

			#print(cc1,cc2,w1,w2,Simchk)
			#fSim.write(str(cc1) + ' '+ str(cc2)+ ' '+ str(Simchk)+ '\n')
	
	return Simchk


c=50
c1=1

while(c1<=c):
	c2=1
	while(c2<=c):
		outer =0 
		SumC1=0
		while(outer<len):
			inner =0
			bb = getS(outer,SPath)	
			while(inner<len):
				#if(inner!=outer and c1!=c2):
				fSim = open(SimPath, 'a+b')
				aa= getS(inner,SPath)
				SC =simChk(c1,c2,bb,aa)
				SumC1=SumC1+SC
				inner=inner+1
			outer=outer+1
		#print(c1,c2,SumC1)
		fSim.write("Sentence "+ str(c1) + ' '+ "Sentence "+str(c2)+ ' = '+ str(SumC1)+ '\n')
		c2=c2+1
	c1=c1+1

#print(arr)

fSim.close()






