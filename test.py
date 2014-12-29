#!/usr/bin python3

import sys
import pymoji

exitcode = 0

# This fails for every emoji not supported by program/font/OS

for e, a in pymoji.codes.items():
  print("# Testing: {} ( {} ) => {}".format(e.ljust(5), pymoji.Emoji(e).char, a).ljust(60), end="")
  if not pymoji.Emoji(e).is_supported:
    print(" ... not supported")
    continue
  try:
    assert(pymoji.Emoji(e).aliases == a)
    assert(pymoji.Emoji(e).alias == a[0])
    assert(pymoji.Emoji(e).char == bytes("\\u"+e, "ascii").decode("unicode-escape"))
    assert(pymoji.Emoji(pymoji.Emoji(e).char).escape == e)
  except:
    exitcode += 1
    print(" ... FAILED")
  else:
    print(" ... done")

print("")

print("# Testing replacement functions", end="")
try:
  text = "I :heart: Python :bangbang:"
  textnew = pymoji.replaceAliases(text)
  assert(pymoji.replaceEmoji(textnew) == text)
  textnew = pymoji.replaceAliases(text, 1)
  assert(pymoji.replaceEmoji(textnew, 1) == text)
except:
  exitcode += 1
  print(" ... FAILED")
  raise
else:
  print(" ... done")

print("")

if exitcode == 0:
  print("No failed tests.")
else:
  print("{} failed test(s).".format(exitcode))

sys.exit(exitcode)
