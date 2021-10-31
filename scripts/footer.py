import re
import sys

def readfile(fname):
  with open(fname, "r") as f: return f.read()


def writefile(fname, content):
  with open(fname, "w") as f: return f.write(content)


patterns = [
  ('<!--fs-->', '<!--fe-->', './scripts/footer.md'),
  ('<!--hs-->', '<!--he-->', './scripts/high-level-requirements.md'),
  ('<!--ms-->', '<!--me-->', './scripts/micro-requirements.md'),
  ('<!--ds-->', '<!--de-->', './scripts/dd.md'),
  ('<!--rs-->', '<!--re-->', './scripts/req.md'),
]

for pattern in patterns:
  footer = "\n" + readfile(pattern[2]).strip() + "\n"
  content = readfile(sys.argv[1]).strip()
  content = re.sub(pattern[0] + '?(.*?)' + pattern[1], pattern[0] + footer + pattern[1], content, flags=re.DOTALL)
  writefile(sys.argv[1], content)
