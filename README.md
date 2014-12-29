pymoji
======

[![Build Status](http://img.shields.io/travis/KoffeinFlummi/pymoji.svg?style=flat)](https://travis-ci.org/KoffeinFlummi/pymoji) [![License](http://img.shields.io/badge/license-MIT-red.svg?style=flat)](https://github.com/KoffeinFlummi/pymoji/blob/master/LICENSE)

Convert [emoji-cheat-sheet](http://www.emoji-cheat-sheet.com/) names to unicode and more!

Inspiration: [GitHub's gemoji](https://github.com/github/gemoji)


### Setup

```
python3 setup.py install
```


### Usage

Converting emoji-cheat-sheet aliases to their escape sequences or unicode entities and vice versa:

```python
>>> import pymoji
>>> pymoji.Emoji(":star:").char
'⭐'
>>> pymoji.Emoji(":star:").escape
'2b50'
>>> pymoji.Emoji("2b50").alias
':star:'
>>> pymoji.Emoji("2b50").aliases
[':star:']
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
