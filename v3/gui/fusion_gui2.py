#=[site officiel]===================
#<<<<<fusion_gui2 by W3YZOH0RTH>>>>>
#========[http://progject.free.fr/]=
from mod_file import *
from mod_base import int_base, base_int
from mod_string import int_len
from os import mkdir, remove, rename, system

def voir_files(fichier,start=-1,stop=-1,current=0):
      fusioned = file(fichier,"rb")

      if start != stop :
            start, stop = void_read(fusioned,start-current,stop)
            start += current
      else:fusioned.read(1)
      string = fusioned.readline()
      files = []
      ligne = 0
      read = -1

      while string != "":
            if read == -1:
                  if string == "\n":
                        string = fusioned.readline()
                        files[-1] = ligne
                        ligne += 1

                  if string == "": break
                  else:
                        name = string[:-1]
                        if files != [] :
                              files[-1] = ligne
                              yield files
                        files = [name,ligne+2,ligne]

            elif read == -2: read = base_int(string[:-1],254)

            string = fusioned.readline()
            read -= 1
            ligne += 1
            if start > -1 < stop <= ligne: break
      fusioned.close()


def voir_dir(name_fusioned,start=-1,stop=-1,printer=0):
      fusioned = file(name_fusioned,"rb")
      for el in files_in_dir(fusioned,get_arborescence(fusioned,start,stop),start,stop,printer):yield el

def files_in_dir(fusioned,(dirs,nbr_dir,len_nbr),start=-1,stop=-1,printer=0):
	if -1 < start <= stop:
		if start > stop : start, stop = stop, start
		stop -= start
	else: stop = -1
	string = fusioned.read(len_nbr)
	c_dir = dirs[base_int(string)]
	if printer : print c_dir
	nbr_file = base_int(fusioned.readline()[:-1])+1
	ligne = 1 + nbr_dir
	index = 0
	while string != "" and nbr_file:
		string = fusioned.readline()
		read = -1
		ligne += 1
		files = []
		if printer : print c_dir
		while string != "" and nbr_file:
			if read == -1:
				if string == "\n":
					files[-1][-1] = ligne
					if printer : print ligne
					string = fusioned.readline()
					ligne += 1
				elif printer : print ligne - 1

				if string == "":break
				else:
					nbr_file -= 1
					if not nbr_file :break
					name = string[:-1]
					files.append([name,ligne+1])
					if printer : print "\t",name,ligne+1,
			elif read == -2 :
				read = base_int(string[:-1], 254)
				if not read:files[-1].append(ligne)
			elif not read:files[-1].append(ligne)
			string = fusioned.readline()
			read -= 1
			ligne += 1
		if files:
			if len(files[-1]) == 3: yield [c_dir,files]
			else: yield [c_dir,files[:-1]+[files[-1]+[ligne]]]
		if ligne >= stop > -1: break
		if len(string) > len_nbr: c_dir = dirs[base_int(string[ : len_nbr])]
		else:
			string += fusioned.readline()
			c_dir = dirs[base_int(string[ : len_nbr])]
			ligne += 1

		index += 1
		nbr_file = base_int(string[len_nbr : -1])+1
	fusioned.close()


def extract_file(fichier,nom,start,stop, path=""):
	fusioned = file(fichier,"rb")
	if start != stop:
		start, stop = void_read(fusioned,start,stop)

		if not path: path = "/".join(fichier.replace("\\","/").split("/")[:-1])
		if path[-1] != "/": path += "/"
		fichier = file(try_file(path + nom),"wb")
		for i in range(stop):fichier.write(fusioned.readline())
		fichier.write(fusioned.readline()[:-1])
		fichier.close()

def extract_dir(fichier,dirs_listed, path=""):
	fusioned = file(fichier,"rb")
	start, stop = void_read(fusioned, dirs_listed[0][1][0][1], dirs_listed[0][1][0][2])
	name_dossier = dirs_listed[0][0]
	if path:
		if path[-1] != "/": path += "/"
		dirs_listed[0][0] = path + get_name(dirs_listed[0][0])
	racine = name_dossier.replace("\\","/").split("/")[-2]
	for i,el in enumerate(dirs_listed):
		if i: dirs_listed[i][0] = dirs_listed[i][0].replace(name_dossier, dirs_listed[0][0])
		try:
			dossier, erreur = _extract_dir_(fusioned, dirs_listed[i])
			fusioned.readline()
		except Exception, err:
			print err
			erreur = 101
		if erreur <= 100:
			dirs_listed[i][0] = dossier


def _extract_dir_(fusioned, dir_listed):

	start, stop = dir_listed[1][0][1:]
	if start != stop:
		dossier = try_dir(dir_listed[0])
		print dossier
		try:
			mkdir(dossier)
			for n,s,e in dir_listed[1]:
				fichier = file(try_file(dossier+"/"+n),"wb")
				temp = e - s - 1
				if temp >= 0:
					for i in range(temp): fichier.write(fusioned.readline())
					fichier.write(fusioned.readline()[:-1])
				fichier.close()
				fusioned.readline()[:-1]
				fusioned.readline()
			return dossier, 0
		except Exception, err:
			print err
			return dossier,  101

def add_file_in_file(nom_fuz, nom, index=True, avancement=False):
      fusioned = file(nom_fuz,"ab")
      ligne = 0
      print "calcule de la taille du fichier ."
      for i in file(nom,"rb").read_lines(): ligne += 1
      fusioned.write(get_name(nom)+"\n")
      fusioned.write(int_base(ligne,254)+"\n")
      x = 0.
      name = get_name(nom)
      for l in file(nom,"rb").read_lines():
            if avancement:
                  x += 1
                  system("cls")
                  print name
                  print "avancement :",x/ligne * 100,"% ",x,"/",ligne,"lignes"
            fusioned.write(l)
      fusioned.write("\n")
      fusioned.close()
      if index:
            print "creation de l'index du fichier de fusion."
            create_index_file(nom_fuz)

def add_files_in_dir(nom_fuz, noms, start_dir, printer=0):
      #start_dir numero de ligne ou commence le dossier
      fusioned = file(nom_fuz, "rb")
      copy = file(get_path(nom_fuz)+"copy", "wb")
      ligne = 0
      if printer: print "copie du debut du fichier de fusion"
      for i in range(start_dir-3): copy.write(fusioned.readline())
      string = fusioned.readline()[:-1]
      copy.write(int_len(int_base(base_int(string, 254) + len(noms), 254), len(string))+"\n")
      for nom in noms:
            if printer: print nom,"\ncalcule de la taille du fichier"
            ligne = 0
            for i in file(nom, "rb").read_lines(): ligne += 1
            copy.write(get_name(nom)+"\n"+int_base(ligne,254)+"\n")
            if printer: print "copie du fichier"
            for i in file(nom, "rb").read_lines(): copy.write(i)
            copy.write("\n")
      if printer: print "copie de la fin du fichier de fusion"
      for i in fusioned.read_lines(): copy.write(i)
      copy.close()
      remove(nom_fuz)
      rename(get_path(nom_fuz)+"copy", nom_fuz)
      if printer: print "creation de l'index du fichier de fusion"
      create_index_dir(nom_fuz)

def add_dirs_in_dir(nom_fuz, dirs, start_dir, index=True):
	fusioned = file(nom_fuz, "rb")
	copy = file(get_path(nom_fuz)+"copy", "wb")
	ligne = 0

#==================================================================================================
def get_arborescence(fusioned,start=-1,stop=-1,current=0):
      dirs = []
      if start != stop :
            start, stop = void_read(fusioned,start-current,stop)
            start += current
      else:fusioned.read(1)

      len_nbr = base_int(fusioned.read(1))
      nbr_dir = base_int(fusioned.read(len_nbr))
      for i in range(nbr_dir) : dirs.append(fusioned.readline()[:-1]+"/")
      for i,f in enumerate(dirs):
            if i:
                  index = f[:len_nbr]
                  dirs[i] = index.replace(index,dirs[base_int(index)])+f[len_nbr:]
      return dirs, nbr_dir, len_nbr

def void_read(fichier,start,stop):
      if start > stop : start, stop = stop, start
      for i in range(start):fichier.readline()
      stop = stop - start - 1
      return start, stop

def dirs_in_dir(fusioned,racine):
      racine = racine.replace("\\","/")
      list_dirs, nbr_dir, len_nbr = get_arborescence(fusioned)
      dirs = []
      size = len(racine)
      for folder in list_dirs:
            if folder[:size] == racine: dirs.append(folder)

      return dirs, nbr_dir, len_nbr


def create_index_dir(nom, nom_dir="",start=-1, stop=-1):
	if nom_dir:
		name = nom.replace("\\","/")+":"+nom_dir.replace("\\","/").replace("/",":")+".zid"
		fichier = file(name,"wb")
	else: fichier = file(".".join(nom.split(".")[:-1])+".zid","wb")
	fusioned = file(nom,"rb")
	if stop > -1 < start: fusioned.read(1)
	dirs, nbr_dir, len_nbr = get_arborescence(fusioned, start, stop)
	fichier.write("1"+int_base(len_nbr)+"\n")

	for i,files in enumerate(files_in_dir(fusioned,(dirs, nbr_dir, len_nbr), start, stop)):
		c_dir, files = files
		nbr_files = len(files)
		if nbr_files:
			fichier.write(int_len(int_base(dirs.index(c_dir)),len_nbr)+int_base(nbr_files,254)+"\n")
			x = 0
			for f, start, stop in files: fichier.write(f+"\n"+int_base(start,254)+"\n"+int_base(stop,254)+"\n")


def create_index_file(nom, nom_dir="",start=-1, stop=-1):
      if nom_dir:
            name = nom.replace("\\","/")+"."+nom_dir.replace("\\","/").replace("/",".")+".zid"
            fichier = file(name,"wb")
      else: fichier = file(".".join(nom.split(".")[:-1])+".zid","wb")
      fusioned = file(nom,"rb")
      if stop <= -1 >= start: fichier.write("0")

      for f, start, stop in voir_files(nom,start,stop):
            print f
            fichier.write(f+"\n"+int_base(start,254)+"\n"+int_base(stop,254)+"\n")
      fichier.close()
