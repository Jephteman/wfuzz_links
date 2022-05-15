"""
Auteur : Jephte Man as Mr me
mail : jephte_man@protomail.com
Version : 0.0.2
"""

import argparse
import os
import sys
import time
import ses_fonctions as sf  # module cree pour ce programme

def chrono():
	time=time.localtime()
	t=((((((((time.tm_year*365)+time.ydays)*24)+time.hour)*60)+time.tm_min)*60)+time.tm_sec)
	return t


def start(parser):
	cible=parser.url
	fichier=parser.f
	ichier='O'
	if fichier.name == '<stdout>':
		fichier_Q='N'
	count=parser.c
        temps=(chrono())+parser.t
        if type(temps) != type(None):
                stop=chrono()
	print(' Nous commmencons ')
	deja_visiter=[]
	try:

		while True:
			trouver=sf.search_links(cible)
			if len(trouver) != 0:
				break
		
		while len(trouver) != 0:
			if sf.compare(str(cible),str(sf.racine(str(trouver[0])))) is True:
				if trouver[0] not in deja_visiter:
					x=sf.search_links(trouver[0])
					if fichier_Q == 'O':
						fichier.write(str(trouver[0])+'\n')
					deja_visiter.append(trouver[0])
					print(n,trouver[0])
					if type(count) != type(None):
						if n == count:
					                exit()
                                        if type(temps) != type(None):
                                                if temps <= stop:
                                                        exit()
				        fi	
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
		pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Auteur : Jephte Mangenda \n Mail : jephte_man@proto.com \n Git : https://github.com/'
		)
	parser.add_argument(
		'url', type=str,help='Lien vers la cible'
		)
	parser.add_argument(
		'-c', default=None, type=int ,
		help='le nombre de resultat attendu'
		)
	parser.add_argument(
		'-f', type=str, help='le fichier ou sera stocker le resultat',
		type=argparse.FileType('a')
		)
	parser.add_argument(
		'-t', default=None, type=int,
		help='la durée de la recherche en secode'
		)
	parser.add_argument(
		'--exp', default='', type=str,
		help='expression rechercher sur le page du lien'
		)
	parser.add_argument(
		'-v' ,default='', help='Affiche la version'
	)
	args = parser.parse_args()
        start(args)
        
