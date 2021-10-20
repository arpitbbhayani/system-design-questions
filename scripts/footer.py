import re
import sys

def readfile(fname):
  with open(fname, "r") as f: return f.read()


def writefile(fname, content):
  with open(fname, "w") as f: return f.write(content)


footer = readfile("./scripts/footer.md")
content = "\n" + readfile(sys.argv[1]) + "\n"
content = re.sub('<!--fs-->?(.*?)<!--fe-->', '<!--fs-->' + footer + '<!--fe-->', content, flags=re.DOTALL)
writefile(sys.argv[1], content)
