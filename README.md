# Text Token Revealer

I made this to help me study for my American History course AMH2010. And it literally does exactly as it says. Everytime the user presses `enter`, the next word (space delimited) will be revealed. It uses the `Blessed` library to control cursor position and keeps the formatting of the original document in the terminal.

## How to use

To begin, press `enter` to initiate from the first token in the document. To start at a certain section in the document, type the phrase desired and the program will automatically start at the line containing that phrase.

```
> impress
```
```
            .
            .
            .
- Contraband only munitions
- No paper blockades
        Can't pass NavAct to stop trade with FR islands
So they went there

Impressment
```


If `space` is pressed, the cursor will revert to the beginning of the line and the process will continue from there

## When finished

Upon reaching the end of the document or typing `END` and pressing `enter`, a small banner will appear outlining some statistics from the session:
- Line Restarts: The total amount of times the user presses space to review a line
- Number of Lines Studied
- Percent Reviewed: Fraction of the lines reviewed to the total number of lines in the document

It will also visually display the segment of text that has been reviewed.
```
=================== END ===================
 Line Restarts:                         13
 Number of Line Studied:                86
 Percent Reviewed:                  21.34%

├───■■■■■■■■──────────────────────────────┤
===========================================
```
