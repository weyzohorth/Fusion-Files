from os import mkdir, chdir, getcwd
from mod_base import *
from mod_file import *
from mod_unicode import *

def fusion_files(files_list, fusioned, f_out=""):
	if not f_out: f_out = file(try_name(fusioned), "wb")
	for f in files_list:
		print f
		f_in = file(f, "rb")
		f_out.write(f + '\n')
		f_out.write(int_base(f_in.size(), 254) + '\n')
		for i in f_in: f_out.write(i)
	f_out.close()

def defusion_files(fusioned):
	name = try_name(get_name(fusioned, False))
	print name
	fusioned = file(fusioned, "rb")
	mkdir(name)
	chdir(name)
	name = fusioned.readline()
	while name:
		print name
		fi = open(name[ : -1], "wb")
		size = base_int(fusioned.readline()[ : -1], 254)
		fi.write(fusioned.read(size))
		fi.close()
		name = fusioned.readline()
	fusioned.close()
		
#=============================================================================================================
def fusion_dirfile(dirs, files=[], name=""):
	if dirs:
		if not name: name = dirs[0]
		if name[-1] == "/": name = name[ : -1]
		len_ext = len(get_ext(name))
		liste = [encode(get_name(name))]
		paths = [encode(name)]
		if get_ext(name) != "fuz": name += ".fuz"

		for dossier in dirs:
			new_paths = get_paths(dossier)
			lim = (len("/".join(new_paths[0][:-1].split("/")[:-1]))+1)*int(bool(new_paths[0][:-1].count("/")))
			for i in new_paths :
				liste.append(encode(liste[0] + "/" + i[lim:-1]))
				paths.append(i[:-1])

		nbr_dir = int_base(len(liste))
		len_nbr = len(nbr_dir)
		i=0
		while i < len(paths):
			index = len("/".join(liste[i].split("/")[:-1]))+1
			if not i : index -= 1

			dossier = encode(liste[i].split("/")[-1])
			index_dossier = len(dossier)
			path = liste[i][:index+index_dossier]
			for ind, p in enumerate(liste) :
				if p[ : index+index_dossier] == path:
					liste[ind] = p[ : index] +\
								p[index : index+index_dossier].replace(dossier, int_len(int_base(i), len_nbr)) +\
								p[index+index_dossier : ]
			i+=1
		
		liste[0] = encode(liste[0][-len_nbr*2-1:-len_nbr-1]+(get_name(paths[0])+".")[ : -len_ext *bool(len_ext)-1])
		for i,e in enumerate(liste[1 : ]):
			liste[i+1] = e[-len_nbr*2-1:-len_nbr-1]+encode(get_name(paths[i+1]))

		fusioned = file(name,"wb")
		fusioned.write("1"+int_base(len_nbr)+int_len(nbr_dir, len_nbr))

		for i in liste : fusioned.write(i+"\n")

		for i, e in enumerate(liste):
			if i:
				fichiers = get_dirfile(paths[i])[1]
				if fichiers:
					fusioned.write(int_len(int_base(i),len_nbr))
					fusioned.write(int_base(len(fichiers))+"\n")
					print "\n"*2,paths[i]
					print
					fusion_files(fichiers, paths[i], fusioned)
			else:
				fusioned.write("0"*len_nbr)
				if files:
					fusioned.write(int_base(len(files), 254)+"\n")
					fusion_files(files, "", fusioned)
				else: fusioned.write("0\n")

		if files == None:
			fusioned.write(int_len(int_base(len(liste)),len_nbr))
			fusioned.write(int_base(len(files), 254)+"\n")
			fusion_files(files, "", fusioned)
		fusioned.close()
		return name
	else: return fusion_files(files,file_fuz=name)

#=============================================================================================================
def defusion_dir(fusioned, new_path=""):
	if new_path:
		if is_file(new_path): path = try_name(new_path)
		else: path = new_path[:]
		try: mkdir(path)
		except: pass
	else: path = "/".join(fusioned.replace("\\","/").split("/")[:-1])
	if path[-1] != "/": path += "/"
	len_path = len(path)

	fusioned = file(fusioned,"rb")
	fusioned.read(1)
	dirs = []
	len_nbr = base_int(fusioned.read(1))
	nbr_dir = base_int(fusioned.read(len_nbr))
	for i in range(nbr_dir) : dirs.append(fusioned.readline()[:-1]+"/")
	for i,f in enumerate(dirs):
		if i:
			index = f[:len_nbr]
			dirs[i] = force_encode(dirs[base_int(index)])+force_encode(f[len_nbr:])

		erreur = 0
		temp = try_name(path+decode(dirs[i][:-1]))
		mkdir(temp)
		dirs[i] = temp[len_path:]+"/"
		if erreur > 100:break

	string = fusioned.read(len_nbr)
	c_dir = dirs[base_int(string)]
	nbr_file = base_int(fusioned.readline()[:-1])+1
	if erreur <= 100:
		while string != "" and nbr_file:
			print "\n"*2,"\t",c_dir
			print

			string = fusioned.readline()
			read = -1
			while string != "" and nbr_file:
				if read == -1:
					if string == "\n":
						fichier = file(path+c_dir+name,"ab")
						fichier.write("\n")
						fichier.close()
						string = fusioned.readline()

					if string == "":break
					else:
						nbr_file -= 1
						if not nbr_file :break
						name = get_name(try_name(path+c_dir+decode(string[:-1])))
						fichier = file(path+c_dir+name,"wb")
						print "\t"*2,name

				elif read == -2 :read = base_int(string[:-1],254)
				elif read : fichier.write(string)
				else:
					fichier.write(string[:-1])
					fichier.close()

				string = fusioned.readline()
				read -= 1

			if len(string) > len_nbr: c_dir = dirs[base_int(string[ : len_nbr])]
			else:
				string += fusioned.readline()
				c_dir = dirs[base_int(string[ : len_nbr])]
			nbr_file = base_int(string[len_nbr : -1], 254)+1

	fusioned.close()
	return path+dirs[0][:-1]

chdir(r"C:\Documents and Settings\Province\Bureau")
#fusion_files(["__init__.py", "fusion.py", "mod_base.py"], "fuz.fuz")
#defusion_files("fuz.fuz")
fusion_dirfile("PSRemote", name="fuz.fuz")
defusion_dir("fuz.fuz")
