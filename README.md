# Bash Menu Builder
![PyPI - Version](https://img.shields.io/pypi/v/bash-menu-builder?logo=pypi&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-v3.9-orange?logo=python&logoColor=white)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c69d7c6784144fb8a4e16150165533e6)](https://app.codacy.com/gh/OleksiiPopovDev/Bash-Menu-Builder/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
![PyPI - License](https://img.shields.io/pypi/l/bash-menu-builder)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bash-menu-builder)
![Downloads](https://img.shields.io/github/downloads/OleksiiPopovDev/Bash-Menu-Builder/total")
![GitHub repo size](https://img.shields.io/github/repo-size/OleksiiPopovDev/Bash-Menu-Builder)

<p align="center">
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/logo.png" width="50%">
</p>

This package help you build menu for yours console scripts

[Installation](#installation) | [Usage](#usage) | [Draw menu](#draw-menu) | [How it works](#how-it-works)

## Installation
For install package to your project use this command:
```shell
pip3 install bash-menu-builder
```

## Usage
Script give opportunity use two type views of menu:
 - [Input Menu](#the-input-type-menu)
 - [Select Menu](#the-select-type-menu)

### The Input type Menu

```python
from bash_menu_builder import InputMenu, CommandOptionDto, MenuItemDto

def banner_text() -> str:
    return 'I\'m Banner Text'

def function_one() -> None:
    print('Script One')

def function_two() -> None:
    print('Script Two')

def function_three() -> None:
    print('Script Three')

    
if __name__ == "__main__":
    InputMenu(
        menu=[
            MenuItemDto(
                title='Menu Item One',
                option=CommandOptionDto(
                    long_option='one',
                    short_option='o',
                ),
                handler=function_one,
                priority=2
            ),
            MenuItemDto(
                title='Menu Item Two',
                option=CommandOptionDto(
                    long_option='two',
                    short_option='t'
                ),
                handler=function_two
            ),
            MenuItemDto(
                title='Menu Item Three',
                option=CommandOptionDto(
                    long_option='three',
                    short_option='r'
                ),
                handler=function_three
            ),
        ],
        banner=banner_text()
    )
```
#### View Menu
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/example-input.gif" alt="How it works" style="width:100%;" />

### The Select type Menu
```python
from bash_menu_builder import SelectMenu, CommandOptionDto, MenuItemDto

def banner_text() -> str:
    return 'I\'m Banner Text'

def function_one() -> None:
    print('Script One')

def function_two() -> None:
    print('Script Two')

def function_three() -> None:
    print('Script Three')

    
if __name__ == "__main__":
    SelectMenu(
        menu=[
            MenuItemDto(
                title='Menu Item One',
                option=CommandOptionDto(
                    long_option='one',
                    short_option='o',
                ),
                handler=function_one,
                priority=2
            ),
            MenuItemDto(
                title='Menu Item Two',
                option=CommandOptionDto(
                    long_option='two',
                    short_option='t'
                ),
                handler=function_two
            ),
            MenuItemDto(
                title='Menu Item Three',
                option=CommandOptionDto(
                    long_option='three',
                    short_option='r'
                ),
                handler=function_three
            ),
        ],
        banner=banner_text()
    )
```
#### View Menu
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/example-select.gif" alt="How it works" style="width:100%;" />

## Draw menu
The menu draw via class ``View`` which get params of array with DTOs and text of banner (optional)
The MenuItemDto have 3 params ``def __init__(self, title: str, option_name: str, handler: object):``
 - `title: str` - the title of menu item
 - `option: CommandOptionDto` - add options to command using via ``--`` ex. calling handler of first item menu: ``python3 main.py --three`` or short option ``python3 main.py --r``
   - `long_option: str` - full name of option for calling ex ``python3 main.py --three``
   - `short_option: str` - short name of option for calling like ``python3 main.py --r``
   - `has_value: bool` - is `True` than you can set value in bash command of handler like ``python3 main.py --three some value``
   > [!WARNING]
   > Unfortunately, you can't use **has_value** param in Select type Menu. **Only for Input type Menu!**

 - `handler: object` - the handler of menu item. What exactly script do after select this menu item.



### How it works
After select the menu number and press Enter will run script in function. When script finish process menu will draw again.

Also, you can call script without drawing menu. Just set option when call python script file, ex. ``python3 main.py --three`` or short option ``python3 main.py --r``
In this case will run script for menu **'Menu Item Three'**. When script finish process menu will not draw again and program will close.

<img src="https://github.com/OleksiiPopovDev/Bash-Menu-Builder/blob/main/doc/example-console.png?raw=true" alt="How it works" style="width:100%;" />

## Draw Alerts
You can draw three types od alerts **Error**, **Warning** and **Success**. How use it:
```python
from bash_menu_builder.message import Message

Message.error(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
           '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
           '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. '
)
Message.warning(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
           '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
           '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. '
)
Message.success(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
           '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
           '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. ',
   title='Custom Success Title'
)
```
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/messages.png" alt="How it works" style="width:100%;" />

### Add tabulation to messages
Using `Message.set_tabs({COUNT_OF_TABS})` you can set tabulation ex.:
```python
from bash_menu_builder.message import Message

Message.error(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry...'
)

Message.set_tabs(1)
Message.warning(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry...'
)

Message.set_tabs(2)
Message.success(
   message='Lorem Ipsum is simply dummy text of the printing and typesetting industry...',
   title='Custom Success Title'
)
```
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/messages-tabs.png" alt="How it works" style="width:100%;" />

## Paint Text
Using tags in text allows you to set the color of the text after the tag. Here's how to use it:
```python
from bash_menu_builder import Draw

print(Draw.paint(
   '{Red}Lorem Ipsum {Green}is simply {Blue}dummy text of the {Yellow}printing and typesetting industry...'
   '\n{Purple}Lorem Ipsum has been the {Cyan}industry\'s standard dummy {White}text ever since the 1500s,'
   '\n{BBlue}when an unknown {BBlack}printer took a galley {BRed}of type and scrambled it {BPurple}to make a type specimen book. '
   '\n{UGreen}It has survived not only five centuries, {UYellow}but also the leap into electronic typesetting, {UCyan}remaining essentially unchanged.'
   '\n{On_Blue}It was popularised {On_Yellow}in the 1960s with {IGreen}the release of Letraset sheets {IWhite}containing Lorem Ipsum passages, and more '
   '\n{BIRed}recently with {BIYellow}desktop publishing {ColorOff}software like Aldus PageMaker including versions of Lorem Ipsum.'
))
```
<img src="https://raw.githubusercontent.com/OleksiiPopovDev/Bash-Menu-Builder/main/doc/color-text.png" alt="How it works" style="width:100%;" />

The list of tags you can find in `Color` enum:
```python
class Color(Enum):
    # Reset
    ColorOff = '\033[0m'  # Text Reset

    # Regular Colors
    Black = '\033[0;30m'  # Black
    Red = '\033[0;31m'  # Red
    Green = '\033[0;32m'  # Green
    Yellow = '\033[0;33m'  # Yellow
    Blue = '\033[0;34m'  # Blue
    Purple = '\033[0;35m'  # Purple
    Cyan = '\033[0;36m'  # Cyan
    White = '\033[0;37m'  # White

    # Bold
    BBlack = '\033[1;30m'  # Black
    BRed = '\033[1;31m'  # Red
    BGreen = '\033[1;32m'  # Green
    BYellow = '\033[1;33m'  # Yellow
    BBlue = '\033[1;34m'  # Blue
    BPurple = '\033[1;35m'  # Purple
    BCyan = '\033[1;36m'  # Cyan
    BWhite = '\033[1;37m'  # White

    # Underline
    UBlack = '\033[4;30m'  # Black
    URed = '\033[4;31m'  # Red
    UGreen = '\033[4;32m'  # Green
    UYellow = '\033[4;33m'  # Yellow
    UBlue = '\033[4;34m'  # Blue
    UPurple = '\033[4;35m'  # Purple
    UCyan = '\033[4;36m'  # Cyan
    UWhite = '\033[4;37m'  # White

    # Background
    On_Black = '\033[40m'  # Black
    On_Red = '\033[41m'  # Red
    On_Green = '\033[42m'  # Green
    On_Yellow = '\033[43m'  # Yellow
    On_Blue = '\033[44m'  # Blue
    On_Purple = '\033[45m'  # Purple
    On_Cyan = '\033[46m'  # Cyan
    On_White = '\033[47m'  # White

    # High Intensity
    IBlack = '\033[0;90m'  # Black
    IRed = '\033[0;91m'  # Red
    IGreen = '\033[0;92m'  # Green
    IYellow = '\033[0;93m'  # Yellow
    IBlue = '\033[0;94m'  # Blue
    IPurple = '\033[0;95m'  # Purple
    ICyan = '\033[0;96m'  # Cyan
    IWhite = '\033[0;97m'  # White

    # Bold High Intensity
    BIBlack = '\033[1;90m'  # Black
    BIRed = '\033[1;91m'  # Red
    BIGreen = '\033[1;92m'  # Green
    BIYellow = '\033[1;93m'  # Yellow
    BIBlue = '\033[1;94m'  # Blue
    BIPurple = '\033[1;95m'  # Purple
    BICyan = '\033[1;96m'  # Cyan
    BIWhite = '\033[1;97m'  # White

    # High Intensity backgrounds
    On_IBlack = '\033[0;100m'  # Black
    On_IRed = '\033[0;101m'  # Red
    On_IGreen = '\033[0;102m'  # Green
    On_IYellow = '\033[0;103m'  # Yellow
    On_IBlue = '\033[0;104m'  # Blue
    On_IPurple = '\033[0;105m'  # Purple
    On_ICyan = '\033[0;106m'  # Cyan
    On_IWhite = '\033[0;107m'  # White
```
