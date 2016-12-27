import inspect

level = 0
filename = "RecViz.log"

fileHandle = open(filename, "w")

class EnableLogging:
    def __init__(self, frame):
        global level
        fileHandle.write("    " * level + "<node>\n")
        level += 1
        fileHandle.write("    " * level + "<input>" + str(inspect.getargvalues(frame)[3])[1:-1] + "</input>" + "\n")
        fileHandle.write("    " * level + "<children>\n")
        level += 1

    def LogAndReturn(self, v):
        fileHandle.write("    " * level + "<output>" + str(v) + "</output>" + "\n")
        return v

    def __del__(self):
        global level
        level -= 1
        fileHandle.write("    " * level + "</children>\n")
        level -= 1
        fileHandle.write("    " * level + "</node>\n")