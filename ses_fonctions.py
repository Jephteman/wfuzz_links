import requests as rq
import requests

# n'avoir que le lien de la racine
def racine(url):
	i=0;x=''
	n=0
	try:
		while i != 3:
			x+=url[n]
			if x[n] == '/':
				i+=1
			n+=1
			if i == 3:
				return x
	except:
		return x


def racine2(url):
	i=0;x=''
	n=0
	try:
		while i != 3:
			x+=url[n]
			if x[n] == '/':
				i+=1
			n+=1
			if i == 3:
				url=x
				break
	except:
		url=x

	"""
	i=0
	s=''
	l=[]
	try:
		while True:
			if x[i] == '/':
				break
			elif x[i] == '.':
				l.append(s)
				s=''
			else:
				s+=url[i]
				print(s)
			i+=1
	except:
		pass"""
	return url


#fonction  obtenir les liens
def search_links(url):
	try:
		x=rq.get(url)
		text=x.text
		i=0
		links=[]
		while True:
			i+=1
			if text[i] == 'h':
				i+=1
				if text[i] == 'r':
					i+=1
					if text[i] == 'e':
						i+=1
						if text[i] == 'f':
							i+=1
							if text[i] == '=':
								i+=1
								if text[i] == '\'' or text[i] == '\"' or text[i] == '\t' or text[i] == '\n':
									i+=1
								boucle2=True
								m=''
								while boucle2:
									m+=text[i]
									if text[i] == '\'' or text[i] == '\"' :
										if 'javascript:' not in m:
											links.append(m[0:-1])
											m=''
											boucle2=False	
									i+=1	
	except IndexError:
		try:
			links_ok=[x for x in links if x[0:4] == 'http']
			links_no=[racine(links_ok[0])+x for x in links if x[0:4] != 'http' and racine(links_ok[0])+x not in links_ok]	
			links=links_ok+links_no
			return links
		except:
			pass
	except requests.exceptions.ConnectionError:
		try:
			links_ok=[x for x in links if x[0:4] == 'http']
			links_no=[racine(links_ok[0])+x for x in links if x[0:4] != 'http' and racine(links_ok[0])+x not in links_ok]	
			links=links_ok+links_no
			return links
		except:
			pass		


# compare deux noms des domaines s'ils sont du meme reseaux
def compare(url1,url2):
	def foct(x):
		o=0
		for i in x:
			if i == '.':
				o+=1
				return o
			o+=1
	
	
	url2=url2[foct(url2):len(url2)]

	if url2 in url1:
		return True
	if url2 not in url1:
		return False

def verif(x):

	if 'https://' in x[0:8] or 'http://' in x[0:8]:
		return True
	
	else:
		return 'http://'+x