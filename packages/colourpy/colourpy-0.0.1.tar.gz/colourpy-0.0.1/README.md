# pyColour

A python function file that colours output strings.

---
## **Contents**
1. [Usage](#usage)
2. [Commands](#commands)
    - [Basic Colours](#basic-colours)
    - [Bright Variants](#bright-variants)
    - [Other Formatting](#other-formatting)
    - [256 Colour Support](#256-colour-support)
    - [Highlighting](#highlighting)
3. [Note](#note)

---


## **Usage**

1. Download the  `pyColour.py`  file into your project's directory, or use git:  `git clone https://github.com/blue-horizons/pyColour/blob/pyColour.py`

2. Call the file into your python project with

```python
from pyColour import *
```

3. Use the following commands in your code.
    Text colour, background colour and formatting can be used at the same time, by stacking (e.g. `bold(red(bgGreen("Hello world!"))))
---
**NOTE**: the outermost colour is the colour that the text will be displayed as (e.g. in `yellow(red(green("hello"))))`, "hello" will be displayed in yellow.

## **Commands**


### **Basic Colours**
**colour**|**command**
:-----:|:-----:
black|`black(string)`
red|`red(string)`
green|`green(string)`
yellow|`yellow(string)`
blue|`blue(string)`
magenta|`magenta(string)`
white|`white(string)`



### **Bright Variants**
**colour**|**command**
:-----:|:-----:
bright black (grey 1)|`bright_black(string)`
bright red|`bright_red(string)`
bright green|`bright_green(string)`
bright yellow|`bright_yellow(string)`
bright blue|`bright_blue(string)`
bright magenta|`bright_magenta(string)`
bright white (grey 2)|`bright_white(string)`



### **Other Formatting**
**Format**|**Command**
:-----:|:-----:
Bold|`bold(string)`
Underline|`underline(string)`
Reverse|`reverse(string)`



### **256 Colour support**

For custom colours, use the following command:
`colour_256(string, [0 -> 255])`

## Highlighting

Highlighting is also possible, and you can use the same commands as before, just with `bg` infront of it (i.e. `bgBlue(string)`, `bgBright_magenta(string)`)

---
---

### Note
> This project is loosely based on the idea of Simple Chalk.