# Type-Token Ratio

## Introduction
`type_token_ratio.py` is an application designed to calculate the Type-Token Ratio from speech sample.  To process a speech sample, it must be saved as a text file containing a list of utterances.  Two common text file formats are `.csv` and `.txt` and can be created using [MS Excel](https://support.bigcommerce.com/articles/Public/What-is-a-CSV-file-and-how-do-I-save-my-spreadsheet-as-one) or any text editor, such as [TextEdit](http://www.macworld.com/article/3030198/software/hurray-for-textedit-a-secret-powerhouse-of-rich-text.html) on Mac OS X, Microsoft [Notepad](https://en.wikipedia.org/wiki/Microsoft_Notepad) or [WordPad](https://en.wikipedia.org/wiki/WordPad) on Windows, and [gedit](https://wiki.gnome.org/Apps/Gedit) on Linux.


## Running this application
To calculate the Type-Token Ratio for a word sample saved with the filename `sample_utterances.csv` will be:
```
user@my_mac:~$ python ~/path/to/type_token_ratio.py ~/path/to/sample_utterances.csv
```
The output will have the following information:
```
Counter({'chicken': 3, 'good': 2, 'ate': 1, 'for': 1, 'i': 1, 'is': 1, 'the': 1})

unique words:     ['ate', 'for', 'i', 'is', 'good', 'chicken', 'the'] 

total utterances: 3
total words:      10
unique words:     7
unique/total:     0.7
output saved to:  sample_utterances.out
```

### Intro Example (Mac OS X specific): 
For those using Mac OS X that may be unfamiliar with using a unix terminal, these steps can be followed to simplify the process:

1. Create a spreadsheet of all the utterances you want to analyze and no other information (this can be a copy of another worksheet with everything but the utterances removed)
2. From the **File** menu, select **Save As**.  Save the file as a **csv** file on your **Desktop**.  For this example, we will say you saved it as `sample_utterances.csv`
3. Save a copy of `type_token_ratio.py` on your 'Desktop'
4.  On your Mac, open up 'Launchpad', then choose the 'Utilities' menu, and run the 'Terminal' program (which has an icon similar to a TV screen)
5. In the screen that opens, type the command `cd`
6. Type the command `cd Desktop/` and hit `Enter`
7. Type the command `python type_token_ratio.py sample.csv` and hit 'Enter'
8. The result are shown in the terminal window.  Additionally a text file containing the results will be created on the desktop with the same file name as the imput but with the extension changed to `.out`.  For this example, the output file will be called `sample.out`

##Known Bugs
1. If the input file extension is `xlsx`, `xls`, `doc`, `docx`, or any other non-text, binary file format, the program will not function properly and the output will not represent the Type-Token Ratio of the language sample.

2. If the a correct path and filename are not provided for both the `type_token_ratio.py` program, and the language sample text file (ie `sample.csv` in the above example), python will output an error similar to one of the two following errors:
```
python: can't open file 'type_token_ration.py': [Errno 2] No such file or directory
```
or
```
Traceback (most recent call last):
  File "type_token_ratio.py", line 41, in <module>
    f = open(sys.argv[1])      # open the file
IOError: [Errno 2] No such file or directory: 'sample_uterances.csv'
```