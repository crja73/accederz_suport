import requests


def main(arg):
	link = 'https://leakcheck.io/api?key=de0310edbe87ea0e30cd6d7ec1887ec49ee681da&check=' + arg + '&type=email'
	res = requests.get(link)

	return res.text

def second(arg):
	link = 'https://leakcheck.io/api?key=de0310edbe87ea0e30cd6d7ec1887ec49ee681da&check=' + arg + '&type=login'
	res = requests.get(link)

	return res.text
