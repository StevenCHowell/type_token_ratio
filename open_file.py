#!/usr/bin/env python
'''
Application to calculate the Type-Token Ratio from an input speech sample.
'''

import Tkinter, Tkconstants, tkFileDialog

class TkFileDialog(Tkinter.Frame):
    '''
    testing out using Tkinter
    '''
    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        # define button
        Tkinter.Button(self, text='Select Speech Sample',
                       command=self.askopenfile).pack(**button_opt)

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('text files', '.csv'), ('text files', '.txt'), ('all files', '*')]
        # options['initialdir'] = 'C:\\'
        options['initialfile'] = 'sample_utterances.csv'
        #options['parent'] = root
        options['title'] = 'Select Speech Sample'

    def askopenfile(self):
        """Returns an opened file in read mode."""

        return tkFileDialog.askopenfile(mode='r', **self.file_opt)


if __name__ == '__main__':
    app = Tkinter.Tk()
    TkFileDialog(app).pack()
    app.mainloop()
