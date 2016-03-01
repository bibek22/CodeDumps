from subprocess import Popen, PIPE

cmd = ['grep', '-e', 'thi']
p = Popen(cmd, stdin=PIPE, stdout=PIPE)
for c in range(10):
    p.stdin.write('this is awesome.\n')
p.stdin.write('things just changed!\n')
output = p.stdout.read()
p.stdin.close()
print(output)
