from __future__ import division
import os
import re
import editdistance 

count = 1

pathr =os.getcwd()+'/crowd_out.txt'    
pathw =os.getcwd()+'/num.txt'
pathpos =os.getcwd()+'/pos.txt'

patharr=os.getcwd()+'/arr.txt'

pathed=os.getcwd()+'/ed.txt'

pathSim =os.getcwd()+'/sim.txt'


parr=[]

pathRoot=os.getcwd()+'/root.txt'
parr.append(pathRoot)

pathDep=os.getcwd()+'/dep.txt'
parr.append(pathDep)


pathnSubj=os.getcwd()+'/nsubj.txt'
parr.append(pathnSubj)


pathnSubjpass=os.getcwd()+'/nsubjpass.txt'
parr.append(pathnSubjpass)


pathdObj=os.getcwd()+'/dobj.txt'
parr.append(pathdObj)

pathiObj=os.getcwd()+'/iobj.txt'
parr.append(pathiObj)


pathcSubj=os.getcwd()+'/csubj.txt'
parr.append(pathcSubj)


pathcsSubjpass=os.getcwd()+'/cssubjpass.txt'
parr.append(pathcsSubjpass)


pathcComp=os.getcwd()+'/ccomp.txt'
parr.append(pathcComp)


pathxComp=os.getcwd()+'/xcomp.txt'
parr.append(pathxComp)


pathnmod=os.getcwd()+'/nmod.txt'
parr.append(pathnmod)


pathadvcl=os.getcwd()+'/advcl.txt'
parr.append(pathadvcl)


pathadvmod=os.getcwd()+'/advmod.txt'
parr.append(pathadvmod)

pathneg=os.getcwd()+'/neg.txt'
parr.append(pathneg)


pathscore=os.getcwd()+'/score.txt'



f= open(pathr,'r')
fw= open(pathw, 'w')
fpos = open(pathpos, 'w')

for x in f:
	if "Input" in x:
		linenum = fw.write(str(count)+'\t'+x+'\n')
		count = count+1 

	#elif "Parse" in x:
			
	else:
		lineblank=fw.write(x)
		count = count

f= open(pathr,'r')
k=0

for x in f:
	if re.search('ROOT',x):
		k=k+1
		word=fpos.write('\n'+str(k)+' '+x)

	elif re.search(r'\b' + "dep" + r'\b', x):	#	elif re.match('advcl',x):
		deps = x.strip().lstrip("| +--")
		dep =fpos.write(str(k)+' '+deps+'\n')

	elif re.search(r'\b' + "advcl" + r'\b', x):	#	elif re.match('advcl',x):
		advs = x.strip().lstrip("| +--")
		adv =fpos.write(str(k)+' '+advs+'\n')

	elif re.search(r'\b' + "nsubj" + r'\b', x):
		subjs = x.strip().lstrip("| +--")
		subj =fpos.write(str(k)+' '+subjs+'\n')

	elif re.search(r'\b' + "nsubjpass" + r'\b', x):
		subjs = x.strip().lstrip("| +--")
		subj =fpos.write(str(k)+' '+subjs+'\n')

	elif re.search(r'\b' + "dobj" + r'\b', x):
		dobjs = x.strip().lstrip("| +--")
		dobj =fpos.write(str(k)+' '+dobjs+'\n')


	elif re.search(r'\b' + "iobj" + r'\b', x):	
		objs = x.strip().lstrip("| +--")
		obj =fpos.write(str(k)+' '+objs+'\n')
	
	elif re.search(r'\b' + "csubj" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')
	
	elif re.search(r'\b' + "csubjpass" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "ccomp" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')
	
	elif re.search(r'\b' + "xcomp" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "nmod" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')

	elif re.search(r'\b' + "advmod" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')
	elif re.search(r'\b' + "neg" + r'\b', x):
		mods = x.strip().lstrip("| +--")
		mod =fpos.write(str(k)+' '+mods+'\n')


fw.close()
fpos.close()


fpos = open(pathpos, 'r')

arrDep=[]
arrIobj=[]
arrDobj=[]

arrNsubjpass=[]
arrNsubj=[]
arrAdvcl=[]

arrCsubj=[]
arrCsubjpass=[]
arrCComp=[]

arrXcomp=[]
arrNmod=[]
arrAdvmod=[]

arrNeg=[] #
arrRoot=[] #


for l in fpos.readlines():
	s=l.split()
	if "ROOT" in s:
		arrRoot.append(l)

	elif "dep" in s:
		arrDep.append(l)
	
	elif "nsubj" in s:
		arrNsubj.append(l)

	elif "nsubjpass" in s:
		arrNsubjpass.append(l)

	elif  "dobj" in s:
		arrDobj.append(l)

	elif "iobj" in s:	
		arrIobj.append(l)
	
	elif "csubj" in s:
		arrCsubj.append(l)
	
	elif "csubjpass" in s:
		arrCsubjpass.append(l)

	elif "ccomp" in s:
		arrCComp.append(l)
	
	elif "xcomp" in s:
		arrXcomp.append(l)

	elif "nmod" in s:
		arrNmod.append(l)

	elif "advcl" in s:
		arrAdvcl.append(l)		

	elif "advmod" in s:
		arrAdvmod.append(l)

	elif "neg" in s:
		arrNeg.append(l)



def relation(idx,pos,array, fw):
	var=''
	for a in array:
		if pos in a:
			if idx== int(a.split()[0]):
				var=a
				fw.write("%s" % a)
				fw.write("\n")
	#jarr=[]
	#oper=[]
	if var == '':
		#jarr.append(str(idx))
		#jarr.append(" ")
		#oper.append(jarr)
	#	for j in jarr:
		fw.write("%s" % idx)
		fw.write("\n\n")



 # 1. Root
#pathRoot=os.getcwd()+'/root.txt'

fblockRoot = open(pathRoot, 'w')

r=1
while(r <count):
	relation(r,"ROOT",arrRoot,fblockRoot)
	r=r+1



# 2. dep
#pathDep=os.getcwd()+'/dep.txt'

fblockDep = open(pathDep, 'w')

b=1
while(b <count):
	relation(b,"dep",arrDep,fblockDep)
	b=b+1


# 3. nsubj
#pathDep=os.getcwd()+'/dep.txt'

fblockNsubj = open(pathnSubj, 'w')
c=1
while(c <count):
	relation(c,"nsubj",arrNsubj,fblockNsubj)
	c=c+1


#4. nsubjpass
# pathnSubjpass=os.getcwd()+'/nsubjpass.txt'

fblockNsubjpass = open(pathnSubjpass, 'w')
d=1
while(d <count):
	relation(d,"nsubjpass",arrNsubjpass,fblockNsubjpass)
	d=d+1



#5. dobj
# pathdObj=os.getcwd()+'/dobj.txt'

fblockdobj = open(pathdObj, 'w')
e=1
while(e <count):
	relation(e,"dobj",arrDobj,fblockdobj)
	e=e+1



#6. iobj
# pathiObj=os.getcwd()+'/iobj.txt'

fblockiobj = open(pathiObj, 'w')
f=1
while(f <count):
	relation(f,"iobj",arrIobj,fblockiobj)
	f=f+1

fblockiobj.close()

#7. csubj
# pathcSubj=os.getcwd()+'/csubj.txt'

fblockcSubj = open(pathcSubj, 'w')
r=1
while(r <count):
	relation(r,"csubj",arrCsubj,fblockcSubj)
	r=r+1

fblockcSubj.close()

#8. csubjpass
# pathcsSubjpass=os.getcwd()+'/cssubjpass.txt'

fblockcSubjpass = open(pathcsSubjpass, 'w')
r=1
while(r <count):
	relation(r,"csubjpass",arrCsubjpass,fblockcSubjpass)
	r=r+1

fblockcSubjpass.close()

#9. ccomp
# pathcComp=os.getcwd()+'/ccomp.txt'

fblockcComp = open(pathcComp, 'w')
r=1
while(r <count):
	relation(r,"ccomp",arrCComp,fblockcComp)
	r=r+1

fblockcComp.close()

#10. xcomp
#pathxComp=os.getcwd()+'/xcomp.txt'

fblockxComp = open(pathxComp, 'w')
r=1
while(r <count):
	relation(r,"xcomp",arrXcomp,fblockxComp)
	r=r+1


fblockxComp.close()

#11. nmod
#pathnmod=os.getcwd()+'/nmod.txt'

fblocknMod = open(pathnmod, 'w')
r=1
while(r <count):
	relation(r,"nmod",arrNmod,fblocknMod)
	r=r+1


fblocknMod.close()

#12. advcl
#pathadvcl=os.getcwd()+'/advcl.txt'

fblockAdvcl = open(pathadvcl, 'w')
r=1
while(r <count):
	relation(r,"advcl",arrAdvcl,fblockAdvcl)
	r=r+1

fblockAdvcl.close()

#13. advmod
#pathadvmod=os.getcwd()+'/advmod.txt'

fblockAdvmod = open(pathadvmod, 'w')
r=1
while(r <count):
	relation(r,"advmod",arrAdvmod,fblockAdvmod)
	r=r+1


fblockAdvmod.close()

#14. neg
#pathneg=os.getcwd()+'/neg.txt'

fblockneg = open(pathneg, 'w')
r=1
while(r <count):
	relation(r,"neg",arrNeg,fblockneg)
	r=r+1


fblockneg.close()


fblockRoot.close()
fblockDep.close()
fblockNsubj.close()
fblockNsubjpass.close()
fblockdobj.close()



fScore = open(pathscore, 'w')


def score(s1,s2,path):
	fb = open(path, 'r')
	w1=''
	w2=''
	rel1=''
	rel2=''
	ele1=[]
	ele2=[]
	relArr1=[]
	relArr2=[]
	
	name= os.path.basename(path.split('.')[0])

#	for a in array:
	#	if pos in a:
		#	if idx== int(a.split()[0]):


	for a in fb.readlines():
		st= a.split()
		if str(s1) in st:
			#if s1 == a.split()[1]:
				#print("SSS")
			
			#if(s1 == a.split()[0]):
					
					try:
						w1= a.split()[1]
					except IndexError:
						w1= a.split()[0]
					try:
						rel1=a.split()[2]
					except IndexError:
						rel1=''

					ele1.append(w1)	
					relArr1.append(rel1)
			#except IndexError:
			#	print("errror")
			
			#for b in fb.readlines():
			#else:
				#	ele1.append(w1)	
				#	relArr1.append(rel1)	
					print(s1,w1)

		if str(s2) in st:
		#	if s2 == a.split()[0]:
				#if(s2 == a.split()[0]):

				#if len(a)>2:
					try:
						w2= a.split()[1]
					except IndexError:
						w2= a.split()[0]
					try:
						rel2=a.split()[2]
					except IndexError:
						rel2=''
	
					ele2.append(w2)
					relArr2.append(rel2)
				#else:
					#ele2.append(w2)	
				#	relArr2.append(rel2)

				#print(s2,w2)
	#	print(s1,s2,w1,w2,rel1,rel2)
	
	l1=0
	while(l1<len(ele1)):
		l2=0
		while(l2<len(ele2)):
			w1= ele1[l1]
			w2=ele2[l2]
			rel1=relArr1[l1]
			rel2=relArr2[l2]

			score=0
			if (w1!='' and w2!='' and w1==w2):
				if(rel1!='' and rel2!='' and rel1==rel2):
					score=2
					#print("Input "+ str(s1)+ ', ' + str(s2)+'\n')
					#print(w1 + ' ' +w2 + ' '+str(score)+'\n')
					#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+ name+'  \n')
					fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				else:
					score=1
					#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
					#print(w1 + ' ' +w2 + ' '+str(score)+'\n')
					fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')

			elif (rel1!='' and rel2!='' and rel1==rel2):
				score=1
				#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
				fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				#print(w1 + ' ' +w2 + ' '+str(score)+'\n')

			else:
				score=0
				#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
				fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				#print(w1 + ' ' +w2 + ' '+str(score)+'\n')

			l2=l2+1
		l1=l1+1
		#fb.close()

#outer=1
#while(outer <count):
#	inner =1
#	while(inner<count):
#		if (inner !=outer):
#			i=0
#			while(i<14):
#				name= os.path.basename(parr[i]).split('.')[0]
#				#fScore.write("\nInput "+str(inner)+' ' + "Input "+str(outer)+' ' + name+'\n\n')
				#score(inner,outer,parr[i])
#				print(name, str(i), str(inner), str(outer))
#				i=i+1
			
#		inner= inner+1
#	outer=outer+1




Simarr=[]

pathRoot=os.getcwd()+'/Simroot.txt'
Simarr.append(pathRoot)

pathDep=os.getcwd()+'/Simdep.txt'
Simarr.append(pathDep)


pathnSubj=os.getcwd()+'/Simnsubj.txt'
Simarr.append(pathnSubj)


pathnSubjpass=os.getcwd()+'/Simnsubjpass.txt'
Simarr.append(pathnSubjpass)


pathdObj=os.getcwd()+'/Simdobj.txt'
Simarr.append(pathdObj)

pathiObj=os.getcwd()+'/Simiobj.txt'
Simarr.append(pathiObj)


pathcSubj=os.getcwd()+'/Simcsubj.txt'
Simarr.append(pathcSubj)


pathcsSubjpass=os.getcwd()+'/Simcssubjpass.txt'
Simarr.append(pathcsSubjpass)


pathcComp=os.getcwd()+'/Simccomp.txt'
Simarr.append(pathcComp)


pathxComp=os.getcwd()+'/Simxcomp.txt'
Simarr.append(pathxComp)


pathnmod=os.getcwd()+'/Simnmod.txt'
Simarr.append(pathnmod)


pathadvcl=os.getcwd()+'/Simadvcl.txt'
Simarr.append(pathadvcl)


pathadvmod=os.getcwd()+'/Simadvmod.txt'
Simarr.append(pathadvmod)

pathneg=os.getcwd()+'/Simneg.txt'
Simarr.append(pathneg)





Sim =[]
#fSim= open(pathSim,'w')
#fScore = open(pathscore, 'w')

def simDependency(s1, s2, path, SimPath):
	fb = open(path, 'r')
	#SimPath= Simarr[depIdx]
	#fSim = open(SimPath, 'w')
	w1=''
	w2=''
	rel1=''
	rel2=''
	ele1=[]
	ele2=[]
	relArr1=[]
	relArr2=[]
	
	name= os.path.basename(path.split('.')[0])

	for a in fb.readlines():
		st= a.split()
		if str(s1) in st:					
				try:
					w1= a.split()[1]
				except IndexError:
					w1= a.split()[0]
				try:
					rel1=a.split()[2]
				except IndexError:
					rel1=''

				ele1.append(w1)	
				relArr1.append(rel1)
		
				print(s1,w1)
		if str(s2) in st:
				try:
					w2= a.split()[1]
				except IndexError:
					w2= a.split()[0]
				try:
					rel2=a.split()[2]
				except IndexError:
					rel2=''
	
				ele2.append(w2)
				relArr2.append(rel2)
	Simchk=0
	l1=0
	while(l1<len(ele1)):
		l2=0
		while(l2<len(ele2)):
			w1= ele1[l1]
			w2=ele2[l2]
			rel1=relArr1[l1]
			rel2=relArr2[l2]

			score=0
			if (w1!='' and w2!='' and w1==w2):
				if(rel1!='' and rel2!='' and rel1==rel2):
					score=2
					Simchk=Simchk+2
					#print("Input "+ str(s1)+ ', ' + str(s2)+'\n')
					print(w1 + ' ' +w2 + ' '+str(score)+'\n')
					#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+ name+'  \n')
					#fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				else:
					score=1
					#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
					print(w1 + ' ' +w2 + ' '+str(score)+'\n')
					#fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')

			elif (rel1!='' and rel2!='' and rel1==rel2):
				score=1
				Simchk=Simchk+1
				#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
				#fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				print(w1 + ' ' +w2 + ' '+str(score)+'\n')

			else:
				score=0
				#fScore.write("Input "+ str(s1)+ ', ' + str(s2)+' '+name+'  \n')
				#fScore.write(w1 + ' ' +w2 + ' '+str(score)+'\n')
				print(w1 +' '+w2 + ' '+str(score)+'\n')

			l2=l2+1
		l1=l1+1
	#print("Sim " + str(s1) +' '+str(s2)+' = '+ str(Simchk))
	SimVal= Simchk/(l2+l1)	
	#print(str(s1) +', '+str(s2)+' = '+ str(SimVal))
	fSim.write(str(s1) +', '+str(s2)+' = '+ str(SimVal)+'\n')

	#print('\n\n')
	#fSim.write("Sim " + str(s1) +' '+str(s2)+' = '+ str(Simchk)+'\n'+str(l1)+' '+str(l2)+'\n')
	#fSim.write("Option 1 Score: " + str(SimVal)+' \n')
	
	
i=0
while(i<14):

	outer=1
	while(outer <count):
		inner =1
		while(inner<count):
			if (inner !=outer):
				name= os.path.basename(parr[i]).split('.')[0]
				#fScore.write("\nInput "+str(inner)+' ' + "Input "+str(outer)+' ' + name+'\n\n')
				#score(inner,outer,parr[i])
				SimPath= Simarr[i]
				fSim = open(SimPath, 'a+b')

				print(name, str(i), str(inner), str(outer))
				simDependency(inner, outer, parr[i],Simarr[i])
											
			inner= inner+1
		outer=outer+1
	i=i+1





fScore.close()
fSim.close()
