import sys
import os.path
import time

def policzLinieWPliku(nazwaPliku):
	iloscLinii = 0
	f = open(nazwaPliku, 'r')
	for line in f :
		iloscLinii = iloscLinii + 1
	return iloscLinii

def przelicz(sciezka) :
	calkowitaIloscLinii = 0	
	rozszerzenia = '.html', '.txt', '.xhtml', 'java', '.xml', '.sql', '.xcss', '.ini', '.pas', '.css', '.conf', '.h', '.m', '.json', '.py'
	listaPlikow = os.listdir(sciezka)
	
	for plik in listaPlikow :
		if os.path.isdir(sciezka + '/' + plik) :
			calkowitaIloscLinii = calkowitaIloscLinii + przelicz(sciezka + '/' + plik)
		else :
			if os.path.isfile(sciezka + '/' + plik) and plik.endswith(rozszerzenia) :
				calkowitaIloscLinii = calkowitaIloscLinii + policzLinieWPliku(sciezka + '/' + plik)
	
	return calkowitaIloscLinii

t1 = time.time()
print przelicz(sys.argv[1])
print time.time() - t1
		