pymoji
======

[![Build Status](http://img.shields.io/travis/KoffeinFlummi/pymoji.svg?style=flat)](https://travis-ci.org/KoffeinFlummi/pymoji) [![License](http://img.shields.io/badge/license-MIT-red.svg?style=flat)](https://github.com/KoffeinFlummi/pymoji/blob/master/LICENSE)

Convert emoji-cheat-sheet names to unicode and more!

Inspiration: [GitHub's gemoji](https://github.com/github/gemoji)


### Setup

```
python3 setup.py install
```


### Usage

Converting emoji-cheat-sheet aliases to their escape sequences or unicode entities and vice versa:

```python
>>> import pymoji
>>> pymoji.Emoji(":boom:").char
'Ὂ'
>>> pymoji.Emoji(":boom:").escape
'1F4A5'
>>> pymoji.Emoji("1F4A5").alias
':boom:'
>>> pymoji.Emoji("1F4A5").aliases
[':boom:', ':collision:']
```

Replacing emoji-cheat-sheet aliases in text and vice versa:

```python
>>> pymoji.replaceAliases("I :heart: Python:exclamation:")
'I ❤ Python❗'
>>> pymoji.replaceEmoji("I ❤ Python❗")
'I :heart: Python:exclamation:'
>>> pymoji.replaceAliases("I :heart: Python:exclamation:", trailingSpaces=1)
'I ❤  Python❗ '
```
