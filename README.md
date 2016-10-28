# Type-Token Ratio

## Introduction
`type_token_ratio.py` is an application designed to calculate the Type-Token Ratio from speech sample.  More information about the Type-Token Ratio can be obtained by searching the [ASHA web-site](http://search.asha.org/default.aspx?q=type%20token%20ratio) using the term "type token ratio".

To process a speech sample, it must be saved as a text file containing a list of utterances.  Two common text file formats are `.csv` and `.txt` and can be created using [MS Excel](https://support.bigcommerce.com/articles/Public/What-is-a-CSV-file-and-how-do-I-save-my-spreadsheet-as-one) or any text editor, such as [TextEdit](http://www.macworld.com/article/3030198/software/hurray-for-textedit-a-secret-powerhouse-of-rich-text.html) on Mac OS X, Microsoft [Notepad](https://en.wikipedia.org/wiki/Microsoft_Notepad) or [WordPad](https://en.wikipedia.org/wiki/WordPad) on Windows, and [gedit](https://wiki.gnome.org/Apps/Gedit) on Linux.


## Running this application
### Input
The command to calculate the Type-Token Ratio for a word sample saved with the filename `sample_utterances.csv` will be:
```
python ~/path/to/type_token_ratio.py ~/path/to/sample_utterances.csv
```

### Command line output
The corresponding output will be:
```
================================================================================
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
================================================================================

Counter({'chicken': 3, 'good': 2, 'ate': 1, 'for': 1, 'i': 1, 'is': 1, 'the': 1}) 

unique words:     ['ate', 'for', 'i', 'is', 'good', 'chicken', 'the'] 


total utterances: 3
total words:      10
unique words:     7
unique/total:     0.7
output saved to: sample_utterances.out
```

### Output File

Additionally a text file containing the results will be created in the same directory.  The file name for this output file will match the input file but with the extension changed to `.out`.  For this example, the output file will be called `sample_utterances.out`.  The contents of this file will have the following format:
```
Type-Token Ratio: 0.7
total utterances: 3
total words:      10
unique words:     7
1	 ate
1	 for
1	 i
1	 is
2	 good
3	 chicken
1	 the


Counter({'chicken': 3, 'good': 2, 'ate': 1, 'for': 1, 'i': 1, 'is': 1, 'the': 1})
```

### Step-By-Step Example (Mac OS X specific): 
For those using Mac OS X that may be unfamiliar with using a unix terminal, these steps can be followed to simplify the process:

1. Create a fresh worksheet within a MS Excel spreadsheet of all the utterances you want to analyze and no other information (this can be a copy of another worksheet with everything removed except the utterances you want to analyze).
2. Use **Save As** to save this current worksheet as a `csv` file.  For this example, we will say you saved it as `sample_utterances.csv`:
    1. From the **File** menu, select **Save As**.
    2. Type in the desired file name.
    3. Select the down arrow next to the file name box to choose to places the file on the **Desktop**.  
    4. In the **File Format** drop down menu select the **Comma Separated Values (.csv)** option.
3. Save a copy of [`type_token_ratio.py`](https://raw.githubusercontent.com/stvn66/type_token_ratio/master/type_token_ratio.py) to your **Desktop** (you can download this file by right clicking [here](https://raw.githubusercontent.com/stvn66/type_token_ratio/master/type_token_ratio.py), selecting **save as**, then chosing to save it to the **Desktop**).
4.  On your Mac, open up **Launchpad**, then choose the **Utilities** menu, and run the **Terminal** program (which has an icon similar to a TV screen).
5. In the screen that opens, type the command `cd` and press `Enter`.
6. Type the command `cd Desktop/` and press `Enter`.
7. Type the command `python ./type_token_ratio.py sample.csv` and press `Enter`.
8. The result are shown in the terminal window and the output file, `sample.out` (same name as the input with `csv` changed to `out`), will be located on the desktop.  

##Known Bugs
1. If the input file extension is `xlsx`, `xls`, `doc`, `docx`, or any other non-text, binary file format, the program will fail to run or the output will not represent the Type-Token Ratio of the language sample.

2. If the a correct path and filename are not provided for both the `type_token_ratio.py` program, and the language sample text file (e.g., `sample_utterances.csv` in the above example), on error will be displayed similar to one of the two following errors:
```
bash: ./type_token_ration.py: No such file or directory
```
or
```
Traceback (most recent call last):
  File "type_token_ratio.py", line 41, in <module>
    f = open(sys.argv[1])      # open the file
IOError: [Errno 2] No such file or directory: 'sample_uterances.csv'
```
