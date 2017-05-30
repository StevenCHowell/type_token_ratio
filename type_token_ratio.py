#!/usr/bin/env python
'''
Application to calculate the Type-Token Ratio from a speech sample.

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

from __future__ import print_function

import collections
import os
import sys
import string

def checkline():
    global l
    global n_words
    global words
    w = l.split()     #flines[1].split()   # this splits the string at all the white space and makes an array of the words
    w = [x.lower() for x in w]   # convert everything to lowercase
    # if 'words' in globals():     # combine all the lines into one list
    try:
        words += w
    except NameError:
        words = w

with open(sys.argv[1]) as f:      # open the file
    flines = f.readlines()     # read in the lines of the file
    n_lines = len(flines)    # count the lines
    for l in flines:           # for each line
        checkline()            # combine the lines and split into words

n_words = len(words)

# remove all punctuations
for i in range(n_words):
    for c in string.punctuation:
        words[i] = words[i].replace(c,'')

# count each word
word_count = collections.Counter(words)

# get the sorted list of unique words
unique_words = list(word_count.keys())
unique_words.sort()

n_unique = len(unique_words)
ttr = len(word_count)/float(len(words))


out_fname = '{}_out.txt'.format(os.path.splitext(sys.argv[1])[0])
print('output saved to: \n{}\n'.format(out_fname))

lines = []
lines.append('Type-Token Ratio (U/T):           {:0.4f}\n'.format(ttr))
lines.append('Number of Utterances:             {}\n'.format(n_lines))
lines.append('Total Number of Words (T):        {}\n'.format(n_words))
lines.append('Total Number of Unique Words (U): {}\n'.format(n_unique))

lines.append('\nUnique Words (frequency):\n')
for word, count in word_count.most_common():
    lines.append('{}\t{}\n'.format(count, word))

lines.append('\nUnique Words (alphabetical):\n')
for word in unique_words:
    lines.append('{}\t{}\n'.format(word_count[word], word))

# lines.append('\n\n{}\n'.format(str(word_count)))
# out_file.write('\n\n' + str(word_count)+'\n')

with open(out_fname, 'w') as out_file:
    for line in lines:
        out_file.write(line)

print(''.join(lines))

print('='*80)
print(' Copyright (C) 2013 Steven C. Howell\n',
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
      'along with this program.  If not, see <http://www.gnu.org/licenses/>.',
      )
print('='*80)
