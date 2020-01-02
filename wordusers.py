# -*- coding: utf-8 -*-
import sys
import string
import re
from unicodedata import normalize

wordlist = open('wordlist-users.txt', 'w')


if len(sys.argv) < 2:
    print(">> Para usar esse script, siga o exemplo, informando a lista de nomes que possui.")
    print("\n  -- Exemplo: python3 "+ sys.argv[0] + " listadenomes.txt \n")
    sys.exit(0)
else:
  with open(sys.argv[1]) as file:
    for line in file:
      line = normalize('NFD',line).encode('ASCII', 'ignore').decode('ASCII')
      line = re.sub(r'[-./?!,":;()\']', ' ', line)
      line=line.rstrip('\n')
      hack_name=line.split()
      last_name=len(hack_name)-1
      last_letter=len(hack_name[0])-1

      #preparacao das linhas com os nomes retirando as quebras de linha
      a=line.replace(' ', '.')+'\n'
      x=a.rstrip('\n')
      b=line.replace(' ', '')+'\n'
      y=b.rstrip('\n')
	
      #grava as concatenacoes de nome + todos sobrenomes
      wordlist.write(a.lower())
      wordlist.write(b.lower())
      
      #grava as concatenacoes da primeira letra do primeiro nome + ultimo nome
      h=hack_name[0][0]+hack_name[last_name]+'\n'
      wordlist.write(h.lower())

      #grava as concatenacoes do primeiro nome e da primeira letra do ultimo nome
      h=hack_name[0]+hack_name[last_name][0]+'\n'
      wordlist.write(h.lower())

      #grava as concatenacoes com numero de 4 digitos
      for casa in range(9999):
        number='{:d}'.format(casa).zfill(4)
        t=hack_name[0][0]+hack_name[last_name]+str(number)+'\n'
        g=hack_name[0][0]+hack_name[0][last_letter]+str(number)+'\n'
        h=hack_name[0]+hack_name[last_name][0]+str(number)+'\n'
        wordlist.write(h.lower())   
        wordlist.write(t.lower())
        wordlist.write(g.lower())
      #grava as concatenacoes com numero de 3 digitos
      for casa in range(999):
        number='{:d}'.format(casa).zfill(3)
        t=hack_name[0][0]+hack_name[last_name]+str(number)+'\n'
        g=hack_name[0][0]+hack_name[0][last_letter]+str(number)+'\n'
        h=hack_name[0]+hack_name[last_name][0]+str(number)+'\n' 
        wordlist.write(t.lower())
        wordlist.write(g.lower())
        wordlist.write(h.lower())
      #grava as concatenacoes com numero de 2 digitos
      for casa in range(99):
        number='{:d}'.format(casa).zfill(2)
        t=hack_name[0][0]+hack_name[last_name]+str(number)+'\n'
        g=hack_name[0][0]+hack_name[0][last_letter]+str(number)+'\n'
        c=x+str(casa)+'\n'
        d=y+str(casa)+'\n'
        h=hack_name[0]+hack_name[last_name][0]+str(number)+'\n'
        wordlist.write(h.lower()) 
        wordlist.write(t.lower())
        wordlist.write(g.lower())
        wordlist.write(c.lower())
        wordlist.write(d.lower())

      #grava as concatenacoes com numero de 1 digito
      for casa in range(9):
        number='{:d}'.format(casa).zfill(1)
        t=hack_name[0][0]+hack_name[last_name]+str(number)+'\n'
        g=hack_name[0][0]+hack_name[0][last_letter]+str(number)+'\n'
        c=x+str(casa)+'\n'
        d=y+str(casa)+'\n'
        h=hack_name[0]+hack_name[last_name][0]+str(number)+'\n'
        wordlist.write(h.lower()) 
        wordlist.write(t.lower())
        wordlist.write(g.lower())
        wordlist.write(c.lower())
        wordlist.write(d.lower())

        wordlist.close()

print("\n<><> Desejar gerar a concatencao com o dominio da empresa? \n Sim(s) \n Nao(n) \n")
op = input("<><> ")
op = op[0].lower()

if op == 's':
  domain = input("<><> Informe o dominio da empresa: ")
  wordlistdomain = open('wordlist-users-domain.txt', 'w') 
  with open('wordlist-users.txt') as file:
    for line in file:
      line=line.rstrip('\n')
      userdomain=line+'@'+domain.lower()+'\n'
      wordlistdomain.write(userdomain)
  wordlistdomain.close()
  print ('\n \n [+][+] Finalizado com sucesso. Usuarios gravados em wordlist-users.txt [+][+]')
else:
  print ('\n \n [+][+] Finalizado com sucesso. Usuarios gravados em wordlist-users.txt e wordlist-users-domain.txt [+][+]')
