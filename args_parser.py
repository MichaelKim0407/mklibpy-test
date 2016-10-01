from mklibpy.util.args import *

__author__ = 'Michael'

args = ["-mv", "--amend", "time", "123.txt"]
parser = OptionArgList([
    OptionArg("m", "move", "move", True),
    OptionArg("v", "visual", "visual", True),
    OptionArg(None, "amend", "amend", True, 1)
])
parser.set_default(move=False, visual=False, amend=(False, None))
print(parser.default)
print(parser.parse(*args))
