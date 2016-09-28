In this run, we have used first fifty sentences of crowd_out.txt file.
The parses.txt file shows the parsing of each sentence.
The selectedDep.txt file shows the desired 14 dependencies and their multiply occurrences if exist in each sentence.
The score.txt file shows the similarity of each sentence with every other sentence across the 14 dependencies

One can read each line (in a row manner) as

[’s1,s2’,  root,    dep,    nsubj, nsubjpass, dobj,	iobj,  csubj, csubjpass, ccomp, xcomp,  nmod,	  advcl,   advmod, neg ]
['1, 1 ', ' 1.0', ' 0.0', ' 1.0', ' 0.0', '   1.0', ' 1.0', ' 0.0', ' 0.0', ' 0.0', ' 1.0', ' 0.0', ' 0.0', ' 0.0', ' 0.0']

as this is the similarity check of first input sentence with itself; one can check the selectedDep.txt file that the input 1 contains 5 dependencies of 14 desired dependencies and there is no multiple occurrences within these 5 dependencies. 

The values are shown here for ease:

1 need VBP ROOT
1 those DT nsubj
1 give VB xcomp
1 themselves PRP iobj
1 injection NN dobj

so the vector is showing similarity score (calculated using Option 1) against the found dependencies and 0 for absentees.



