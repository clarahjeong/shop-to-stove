d=open('src/data.js').read(); s=open('src/shell.html').read()
open('index.html','w').write(s.replace('/*DATA*/', d))
