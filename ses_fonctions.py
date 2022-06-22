import requests as rq
import requests
import socket

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
										if m[0:7] != 'http://' or m[0:8] != 'https://':
											if url[0:-1] != '/':
												#url+='/'
												pass
												
										links.append(m[0:-1])
										m=''
										boucle2=False	
									i+=1	
	except IndexError:
		try:
			links_ok=[x for x in links if x[0:7] == 'http://' or x[0:8] == 'https://' ]
			links_no=[racine(url)+x for x in links if (x[0:7] != 'http://' or x[0:8] != 'https://') and x not in links_ok]	
			links=links_ok+links_no
			return links
		except:
			pass
	except requests.exceptions.ConnectionError:
		try:
			links_ok=[x for x in links if x[0:7] == 'http://' or x[0:8] == 'https://' ]
			links_no=[racine(url)+x for x in links if (x[0:7] != 'http://' or x[0:8] != 'https://') and x not in links_ok]
			links=links_ok+links_no
			return links
		except:
			pass		

# compare deux noms des domaines s'ils sont du meme reseaux
def verif(x):

	if 'https://' in x[0:8] or 'http://' in x[0:8]:
		return True
	
	else:
		return 'http://'+x

def compare(url,durl):
	def dec(x):
		c=0
		n=0
		for i in x:
			if i == '/':
				n+=1
			if n == 2:
				break
			c+=1
		x=x[c:len(x)]
		if x[len(x)-1:len(x)] == '/':
			return x[1:len(x)-1]
		else:
			return x[1:len(x)]

	if dec(url) == dec(durl):
		return True
	elif durl[len(dec(durl))-len(dec(url)):len(dec(durl))] == dec(url):
		return True
	else:
		return False 
	