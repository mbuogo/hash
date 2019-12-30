import sys
import string

wordlist = open('wordlist-users.txt', 'w')

if len(sys.argv) < 2:
    print("\n Exemplo: python "+ sys.argv[0] + " wordlistusuarios.txt \n")
    sys.exit(0)
else:
  with open(sys.argv[1]) as file:
    for line in file:
      line=line.rstrip('\n')
      print(line)
      print(line.replace(' ', '.'))
      print(line.replace(' ', ''))
      a=line.replace(' ', '')+'01\n'
      wordlist.write(a)
  wordlist.close()
