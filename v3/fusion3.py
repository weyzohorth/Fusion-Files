#=[site officiel]===============
#<<<<<fusion3 by W3YZOH0RTH>>>>>
#====[http://progject.free.fr/]=
from gui.fusion_files3 import *
from sys import argv
from os import chdir,getcwd

try:
	len_argv = len(argv)
	if len_argv > 1 and argv[1]:
		ext = argv[1].replace('"',"").split(".")[-1]
		if ext == "fuz" and len_argv == 2:
			defusion(argv[1])
		else:
			print argv
			if getcwd()[0] == "/":	fusion(" ".join(argv[1:]))
			else: fusion(argv[1:])
			#print '''"%s" n'est pas une extension valide .'''%(ext)
	else:
		fichier = raw_input("fichiers ou dossier a fusionner\n\t>>> ").replace('"',"")
		dirfile = []
		while fichier != "":
			try:
				path = getcwd()
				file(fichier).close()
				dirfile.append(fichier)
			except:
				try:
					chdir(fichier)
					chdir(path)
					dirfile.append(fichier)
				except:
					print '''"%s" est introuvable ou vous n'avez pas les droits pour ouvrir ce dossier ou fichier'''%(fichier)
			fichier = raw_input("fichier  ou dossier a ajouter a la fusion (rien pour continuer)\n\t>>> ").replace('"',"")

		if len(dirfile) == 1 and dirfile[0][-3:] == "fuz":
			while 1:
				defuz = raw_input("1 - Defusionner les fichiers '.fuz' presents dans l'archive\n\
0 - Garder fusionne les fichiers '.fuz'\n\t>>> ")
				try:
					defuz = bool(int(defuz))
					break
				except:
					print "Vous devez taper 1 ou 0\n"
			defusion(dirfile[0],defuz)
		else:
			while 1:
				extract = raw_input("1 - Fusionner les fichiers simplement\n\
0 - Créer un auto-extractible\n\t>>> ")
				try:
					extract = not bool(int(extract))
					break
				except:
					print "Vous devez taper 1 ou 0\n"
			if extract: create_autoextract(dirfile)
			else: fusion(dirfile)

	raw_input("\nAppuyez sur entrer pour terminer le programme .")
except Exception, erreur:
	raw_input(erreur)
