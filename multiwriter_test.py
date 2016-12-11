from mklibpy.file.out import MultiWriter

__author__ = 'Michael'

with MultiWriter(True, "multiwriter.out") as writer:
    writer.writeline("Hello world!")
    writer.writeline("This is {} speaking.", "captain")
    writer.writelines("1", "2", "3")

writer.add_file("mw2.out", "a")
with writer:
    writer.writeline("I'm back!")
