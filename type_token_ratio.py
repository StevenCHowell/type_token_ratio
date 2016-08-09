#!/usr/bin/python
'''
Calculate the Type-Token Ratio from a speech sample.

Copyright (C) 2013 Steven C. Howell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Please report any issues on-line at: https://github.com/stvn66/type_token_ratio/issues
'''

import collections
import sys
import string

print('Copyright (C) 2013 Steven C. Howell\n',
      '\n',
      'This program is free software: you can redistribute it and/or modify\n',
      'it under the terms of the GNU General Public License as published by\n',
      'the Free Software Foundation, either version 3 of the License, or\n',
      '(at your option) any later version.\n',
      '\n',
      'This program is distributed in the hope that it will be useful,\n',
      'but WITHOUT ANY WARRANTY; without even the implied warranty of\n',
      'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n',
      'GNU General Public License for more details.\n',
      '\n',
      'You should have received a copy of the GNU General Public License\n',
      'along with this program.  If not, see <http://www.gnu.org/licenses/>.\n',
      )

# import nltk
# w = nltk.word_tokenize(l)  # this splits at all the different punctuation where split does not

def checkline():
    global l
    global wordcount
    global words
    w = l.split()     #flines[1].split()   # this splits the string at all the white space and makes an array of the words
    w = [x.lower() for x in w]   # convert everything to lowercase
    wordcount += len(w)
    if 'words' in globals():     # combine all the lines into one list
       words += w
    else:
       words = w

wordcount = 0              # initialize the variable
f = open(sys.argv[1])      # open the file
flines = f.readlines()     # read in the lines of the file
linecount = len(flines)    # count the lines
for l in flines:           # for each line
    checkline()            # combine the lines and split into words

# remove all punctuations #
for place, item in enumerate(words):
   for c in string.punctuation:
       words[place] = words[place].replace(c,'')


repWords = collections.Counter(words)
uniqueWords = list(set(words))
print repWords, '\n'
print 'unique words:    ', uniqueWords, '\n\n'
print 'total utterances:', linecount
print 'total words:     ', wordcount
print 'unique words:    ', len(repWords)
print 'unique/total:    ', len(repWords)/float(len(words))

textStrings = ['.csv','.tex','.txt']
writeFile = sys.argv[1]
for ext, item in enumerate(textStrings):
    writeFile = writeFile.replace(item, '.out')
print 'output saved to: ', writeFile
fw = open(writeFile, 'w')
s1 = '\n\n' + str(repWords)+'\n'
s2 = 'total utterances: ' + str(linecount) + '\n'
s3 = 'total words:      ' + str(wordcount) + '\n'
s4 = 'unique words:     ' + str(len(repWords))+ '\n'
s5 = 'Type-Token Ratio: ' + str(len(repWords)/float(len(words)))+ '\n'


fw.write(s5 + s2 + s3 + s4)
for place, word in enumerate(uniqueWords):
    fw.write(str('%d\t %s\n' % (repWords[word],word)))
fw.write(s1)



