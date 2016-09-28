from __future__ import division

import os
import unicodedata


from nltk.compat import unicode_repr

from nltk import PorterStemmer
pStem= PorterStemmer()

pathr =os.getcwd()+'/fifty/tenDep.txt'

pathw =os.getcwd()+'/Stemmed/stemtenDep.txt'

f = open(pathw, 'w')
unStemmedfile = open(pathr, 'r')


for x in unStemmedfile.readlines():
	if x.strip():
		a= x.split()
		l = len(a)
		if int(l)>2:
				wor=pStem.stem_word(a[1])
				# unicode is used to remove the leading "u" letter from the stemmed words
				wor=unicode_repr(wor)
				#wor=repr(wor)
				word = wor[1:-1]
				#print(q)
				a[1]=word
				a= (' '.join(a))
				f.write("%s" % a)
				f.write("\n")


	
