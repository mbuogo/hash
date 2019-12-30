import sys
import string


wordlist = open('wordlist-users.txt', 'w')
cont=1


if len(sys.argv) < 2:
    print("\n Exemplo: python "+ sys.argv[0] + " wordlistusuarios.txt \n")
    sys.exit(0)
else:
  with open(sys.argv[1]) as file:
    for line in file:
      line=line.rstrip('\n')
      hack_name=line.split()
      last_name=len(hack_name)-1
      last_letter=len(hack_name[0])-1

      a=line.replace(' ', '.')+'\n'
      x=a.rstrip('\n')
      b=line.replace(' ', '')+'\n'
      y=b.rstrip('\n')
	
      #grava as concatenacoes de nome + todos sobrenomes
      wordlist.write(a.lower())
      wordlist.write(b.lower())

      #grava as concatenacoes da primeira letra do primeiro nome + ultimo nome com e sem numero
      for casa in range(5):
	number='{:d}'.format(casa).zfill(4)
	h=hack_name[0][0]+hack_name[last_name]+'\n'
	t=hack_name[0][0]+hack_name[last_name]+str(number)+'\n'
	g=hack_name[0][0]+hack_name[0][last_letter]+str(number)+'\n'	
	wordlist.write(h.lower())	
	wordlist.write(t.lower())
	wordlist.write(g.lower())

      #grava as concatenacoes de nome + todos sobrenomes + numero
      while (cont < 5):
        c=x+str(cont)+'\n'
        d=y+str(cont)+'\n'
        wordlist.write(c.lower())
        wordlist.write(d.lower())
	
        cont = cont +1

      cont = 0


 
  wordlist.close()
