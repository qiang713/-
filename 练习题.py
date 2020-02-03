from sys  import argv
from os.path import exists

script, 文档.txt, 文档r.txt = argv

in_file = open(文档.txt)
indata = in_file.read()


out_file = open(文档r.txt,'w')
out_file.write(indata)

out_file.close()
in_file.close()
