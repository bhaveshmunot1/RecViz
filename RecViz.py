import inspect

level = 0
filename = "RecViz.log"

fileHandle = open(filename, "w")

class EnableLogging:
    def __init__(self, frame):
        global level
        fileHandle.write("\t" * level + "<node>\n")
        level += 1
        fileHandle.write("\t" * level + "<input>" + str(inspect.getargvalues(frame)[3])[1:-1] + "</input>" + "\n")
        fileHandle.write("\t" * level + "<children>\n")
        level += 1

    def LogAndReturn(self, v):
        fileHandle.write("\t" * level + "<output>" + str(v) + "</output>" + "\n")
        return v

    def __del__(self):
        global level
        level -= 1
        fileHandle.write("\t" * level + "</children>\n")
        level -= 1
        fileHandle.write("\t" * level + "</node>\n")