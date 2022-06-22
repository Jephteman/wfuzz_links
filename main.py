#/bin/python3
"""
Auteur : Jephte Man as Mr me
mail : jephte_man@protomail.com
Version : 1.0
"""
import argparse
import os
import sys
import time
import ses_fonctions as sf  # module cree pour ce programme

def chrono(): # 
	timeloc=time.localtime()
	t=((((((((timeloc.tm_year*365)+timeloc.tm_yday)*24)+timeloc.tm_hour)*60)+timeloc.tm_min)*60)+timeloc.tm_sec)
	return t

def start(parser):
	cible=parser.url
	if sf.verif(parser.url) != True:
		cible=sf.verif(parser.url)
	
	if type(parser.u) != type(None):
		def f():
			return parser.u
		sf.rq.utils.default_user_agent=f

	if type(parser.p) != type(None):
		if cible[0:5] == 'https':
			sf.rq.utils.DEFAULT_PORTS['https']=parser.p
		else:
			sf.rq.utils.DEFAULT_PORTS['http']=parser.p
	
	fichier=parser.o
	fichier_Q=''
	if type(fichier) != type(None):
		fichier_Q='O'
		if fichier.name == '<stdout>':
			fichier_Q='N'
		
	count=parser.c
	print(' Nous commmencons ')
	deja_visiter=[]
	n=0
	
	if type(parser.w) == type(None):
		try:
			
			trouver=sf.search_links(cible)
			while len(trouver) != 0:
				if type(parser.c) != type(None):
					if count == n:
						exit(0)
				if sf.compare(str(cible),str(sf.racine(trouver[0]))) is True:
					if trouver[0] not in deja_visiter:
						x=sf.search_links(trouver[0])
						if fichier_Q == 'O':
							fichier.write(str(trouver[0])+'\n')
						deja_visiter.append(trouver[0])
						print(n,trouver[0])
						n+=1
						del trouver[0]
						try:
							for y in x :
								if y not in trouver and y not in deja_visiter:
									trouver.append(y)
						except:
							pass
					else:
						deja_visiter.append(trouver[0])
						del trouver[0]
				else:
					del trouver[0]
		except KeyboardInterrupt:
			print('bye, bye !')
		except TypeError:
			print('Aucun resultants')
		print(truver)

	elif type(parser.w) == type(sys.stdin):
		i=0
		try:
			while True:
				while True:
					link=str(parser.w.readline())
					if link[:2] != ('\n' and '# '):
						if link == '#':
							pass
						else:
							break
				if link == '':
					break
				if link[:1] != '/':
					link='/'+link
				if str(sf.requests.get(cible+link).status_code)[:2] != '40':
					i+=1
					print(i,cible+link)
					if count == i:
						break
						if type(parser.o) != type(None):
							parser.o.write(cible+link+'\n')
		except ValueError:
			pass
		except KeyboardInterrupt:
			print('bye, bye !')

				
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', type=str,help='Lien vers la cible')
	parser.add_argument('-c', default=None, type=int ,help='le nombre de resultat attendu')
	parser.add_argument(
		'-w',help='Wordlist pour le bruteforce',
		type=argparse.FileType('r')
	)
	parser.add_argument(
		'-o', help='le fichier où sera stocker le resultat',
		type=argparse.FileType('a')
		)
	parser.add_argument(
		'-u', default=None , help='User-agent',type=str
		)
	parser.add_argument(
		'-p',default=None,help='Desctination port',type=int
	)
	parser.add_argument(
		'-v' ,default='', help='Affiche la version'
	)
	args = parser.parse_args()
	start(args)
