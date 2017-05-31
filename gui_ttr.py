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

import datetime
import subprocess
from appJar import gui
import type_token_ratio

def run_ttr(name):
    # select the input the file
    fname = app.openBox(title='Select Speech Sample',
                        fileTypes=[('text files', '*.csv'),
                                   ('text files', '*.txt'),
                                   ('all files', '*')],
                        asFile=False)
    app.setLabel('input', 'Speech Sample: {}\n'.format(fname))  # maybe split this

    # output = subprocess.run(['./type_token_ratio.py', fname],
                            # stdout=subprocess.PIPE)
    results = type_token_ratio.main(fname)

    app.clearTextArea('results', callFunction=False)
    app.setTextArea('results', '{}'.format(results), callFunction=False)


def exit_ttr(name):
    app.stop()


# create the GUI & set a title
app = gui('Type Token Ratio Calculator')

# display license information
license = [
    '='*80,
    '\n Copyright (C) 2013 Steven C. Howell\n',
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
    '='*80,
]
# app.infoBox('License', license)

app.addButtons(['Select Speech Sample', 'Exit'], [run_ttr, exit_ttr])
app.addEmptyLabel('input')
app.addScrolledTextArea('results')
app.setTextArea('results', ''.join(license))

copyright = 'Copyright (C) 2013 Steven C. Howell'
version = 'v 0.1.1'
today = datetime.date.today()
build = 'updated on {}'.format(today.strftime('%d %b %Y'))

app.addLabel('copyright', '{}   -   {}   -   {}'.format(copyright, version,
                                                        build))
app.setGeometry(670, 300)

app.go()
