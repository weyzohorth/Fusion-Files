#-*- coding: cp1252 -*-
#=[site officiel]===========
#<<<<<gui by W3YZOH0RTH>>>>>
#=[http://progject.free.fr/]
import PyQt4.Qt as qt
import sys
from mod_file import get_path, get_name, get_ext, file_exists
from mod_base import int_base, base_int
from fusion_gui2 import *
from fusion_files3 import *

class Gui(qt.QWidget):
	def __init__(__, argv=[]):
		qt.QWidget.__init__(__)
		__.setWindowIcon(qt.QIcon("ico/fuz.ico"))
		__.setWindowTitle("Fusion files")
		__.path = get_path(sys.argv[0])
		__.archive = ""
		temp = ""
		if len(argv) > 1: temp = unicode(" ".join(argv[1:]), "cp1252").replace("\\","/")
		if get_ext(temp) == "fuz":
			__.mode = True
			__.archive = temp[:]
		else:
			__.mode = False
		__.archive_ind = ""
		__.index_dir = (0, 0)


		__.Tabs = qt.QTabWidget(__)
		__.Struct = qt.QWidget(__)
		__.Struct.Archive_name = qt.QPushButton(__.archive, __.Struct)
		__.Struct.Add_dir = qt.QPushButton("Ajouter un dossier", __.Struct)
		__.Struct.Add_dir.setVisible(False)
		__.Struct.Add_file = qt.QPushButton("Ajouter des fichiers", __.Struct)
		__.Struct.Ouvrir_dossier = qt.QPushButton("Ouvrir dossier", __.Struct)
		__.Struct.Dossier_parent = qt.QPushButton("Dossier parent", __.Struct)
		__.Struct.Extraire = qt.QPushButton("Tout extraire", __.Struct)
		__.Struct.Extraire_dossier = qt.QPushButton("Extraire dossier", __.Struct)
		__.Struct.Extraire_file = qt.QPushButton("Extraire fichier", __.Struct)
		__.Struct.Action_ouvrir_dossier = qt.QAction(__)
		__.Struct.Name = qt.QLineEdit(__.Struct)
		__.Struct.Name.setReadOnly(True)

		__.Struct.Dossier = qt.QLabel(__.Struct)
		__.Struct.Dossier.setText("Dossiers : 0")
		__.Struct.List_dossier = qt.QListWidget(__.Struct)

		__.Struct.Fichier = qt.QLabel(__.Struct)
		__.Struct.Fichier.setText("Fichiers : 0")
		__.Struct.List_fichier = qt.QListWidget(__.Struct)


		__.Struct2 = qt.QWidget(__)
		__.Struct2.Layout = qt.QGridLayout(__.Struct2)
		__.Struct2.Archive_name = qt.QLineEdit(__.Struct2)
		__.Struct2.Dossier = qt.QLabel(__.Struct2)
		__.Struct2.List_dossier = qt.QListWidget(__.Struct2)
		if is_dir(temp):
			__.Struct2.List_dossier.addItem(temp)
			__.Struct2.Dossier.setText("Dossiers : 1")
		else:
			__.Struct2.Dossier.setText("Dossiers : 0")
		__.Struct2.Add_dir = qt.QPushButton("Ajouter un dossier", __.Struct2)
		__.Struct2.Suppr_dossier = qt.QPushButton("Retirer un dossier", __.Struct2)

		__.Struct2.Fichier = qt.QLabel(__.Struct2)
		__.Struct2.List_fichier = qt.QListWidget(__.Struct2)
		if is_file(temp):
			__.Struct2.List_fichier.addItem(temp)
			__.Struct2.Fichier.setText("Fichiers : 1")
		else:
			__.Struct2.Fichier.setText("Fichiers : 0")
		__.Struct2.Add_file = qt.QPushButton("Ajouter des fichiers", __.Struct2)
		__.Struct2.Suppr_fichier = qt.QPushButton("Retirer un fichier", __.Struct2)
		__.Struct2.Fusionner = qt.QPushButton("Fusionner", __.Struct2)
		__.Struct2.Autoextract = qt.QPushButton("Créer auto-extractible", __.Struct2)

		__.Path = qt.QPushButton(__)
		__.Path.setWhatsThis("Fusionner/Extraire vers")

		#__.Menu = qt.QMenuBar(__)
		#__.Menu_fichier =  __.Menu.addMenu("Fichier")
		#__.Action_ouvrir = __.Menu_fichier.addAction("Ouvrir archive")
		__.Action_ouvrir = qt.QAction("Ouvrir archive", __)

		__.Status_bar = qt.QStatusBar(__)
		__.Status_bar.showMessage("By W3YZOH0RTH")
		__.Status_progress = qt.QProgressBar(__.Status_bar)
		__.Status_bar.addPermanentWidget(__.Status_progress)

		__.Tabs.addTab(__.Struct2, "Fusion")
		__.Tabs.addTab(__.Struct, "Extraction")
		if __.mode: __.Tabs.setCurrentIndex(1)

		__.VLayout = qt.QVBoxLayout(__)
		#__.VLayout.addWidget(__.Menu)
		__.VLayout.addWidget(__.Path)
		__.VLayout.addWidget(__.Tabs)
		__.VLayout.addWidget(__.Status_bar)
		__.setLayout(__.VLayout)

		__.Struct.Layout = qt.QGridLayout(__.Struct)
		__.Struct.Layout.addWidget(__.Struct.Archive_name, 0, 0, 1, 4)
		__.Struct.Layout.addWidget(__.Struct.Name, 1, 0, 1, 4)
		__.Struct.Layout.addWidget(__.Struct.Add_file, 2, 2, 1, 2)
		#__.Struct.Layout.addWidget(__.Struct.Add_dir, 2, 0, 1, 2)
		__.Struct.Layout.addWidget(__.Struct.Fichier, 3, 2, 1, 1)
		__.Struct.Layout.addWidget(__.Struct.Dossier, 3, 0, 1, 1)
		__.Struct.Layout.addWidget(__.Struct.List_dossier, 4, 0, 1, 2)
		__.Struct.Layout.addWidget(__.Struct.List_fichier, 4, 2, 1, 2)
		__.Struct.Layout.addWidget(__.Struct.Ouvrir_dossier, 5, 0, 1, 1)
		__.Struct.Layout.addWidget(__.Struct.Dossier_parent, 5, 1, 1, 1)
		__.Struct.Layout.addWidget(__.Struct.Extraire_dossier, 6, 0, 1, 2)
		__.Struct.Layout.addWidget(__.Struct.Extraire_file, 6, 2, 1, 2)
		__.Struct.Layout.addWidget(__.Struct.Extraire, 5, 2, 1, 2)
		__.Struct.setLayout(__.Struct.Layout)

		__.Struct2.Layout.addWidget(__.Struct2.Archive_name, 0, 0, 1, 4)
		__.Struct2.Layout.addWidget(__.Struct2.Add_dir, 1, 0, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Add_file, 1, 2, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Fichier, 2, 2, 1, 1)
		__.Struct2.Layout.addWidget(__.Struct2.Dossier, 2, 0, 1, 1)
		__.Struct2.Layout.addWidget(__.Struct2.List_dossier, 3, 0, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.List_fichier, 3, 2, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Suppr_dossier, 4, 0, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Suppr_fichier, 4, 2, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Fusionner, 6, 0, 1, 2)
		__.Struct2.Layout.addWidget(__.Struct2.Autoextract, 6, 2, 1, 2)
		__.Struct2.setLayout(__.Struct2.Layout)

		qt.qApp.connect(__.Action_ouvrir, qt.SIGNAL("triggered()"), __.slot_ouvrir)
		qt.qApp.connect(__.Struct.Action_ouvrir_dossier, qt.SIGNAL("triggered()"), __.slot_open_dir)
		qt.qApp.connect(__.Struct.Archive_name, qt.SIGNAL("clicked()"), __.Action_ouvrir.trigger)
		qt.qApp.connect(__.Struct.Ouvrir_dossier, qt.SIGNAL("clicked()"), __.Struct.Action_ouvrir_dossier.trigger)
		qt.qApp.connect(__.Struct.Dossier_parent, qt.SIGNAL("clicked()"), __.slot_retour)
		qt.qApp.connect(__.Struct.Extraire, qt.SIGNAL("clicked()"), __.slot_extraire_all)
		qt.qApp.connect(__.Struct.Extraire_file, qt.SIGNAL("clicked()"), __.slot_extraire_file)
		qt.qApp.connect(__.Struct.Extraire_dossier, qt.SIGNAL("clicked()"), __.slot_extraire_dir)
		qt.qApp.connect(__.Struct.Add_file, qt.SIGNAL("clicked()"), __.slot_add_fichier)
		qt.qApp.connect(__.Struct.Add_dir, qt.SIGNAL("clicked()"), __.slot_add_dossier)
		qt.qApp.connect(__.Struct2.Add_file, qt.SIGNAL("clicked()"), __.slot_add_fichier)
		qt.qApp.connect(__.Struct2.Add_dir, qt.SIGNAL("clicked()"), __.slot_add_dossier)
		qt.qApp.connect(__.Struct2.Suppr_fichier, qt.SIGNAL("clicked()"), __.slot_suppr_fichier)
		qt.qApp.connect(__.Struct2.Suppr_dossier, qt.SIGNAL("clicked()"), __.slot_suppr_dossier)
		qt.qApp.connect(__.Struct2.Fusionner, qt.SIGNAL("clicked()"), __.slot_fusionner)
		qt.qApp.connect(__.Struct2.Autoextract, qt.SIGNAL("clicked()"), lambda fct=create_autoextract: __.slot_fusionner(fct))
		qt.qApp.connect(__.Path, qt.SIGNAL("clicked()"), __.slot_change_path)
		#qt.qApp.connect(__.Struct.List_dossier, qt.SIGNAL("itemSelectionChanged()"), __.Struct.Action_ouvrir_dossier.trigger)
		if __.archive: __.slot_ouvrir(True)

	def slot_add_fichier(__):
		liste = qt.QFileDialog.getOpenFileNames(__, "Ajouter des fichiers à l'archive")
		if __.Tabs.currentIndex() == 0:
			for path in liste:
				__.Struct2.List_fichier.addItem(path)
			__.Struct2.Fichier.setText("Fichiers : " + str(__.Struct2.List_fichier.count()))
		elif liste:
			_type = file(__.archive, "rb").read(1)
			if _type == "0":
				for nom in liste[ : -1]: add_file_in_file(__.archive, nom, False)
				add_file_in_file(__.archive, liste[-1])
				__.show_files()
			elif _type == "1":
				index_dir = __.arborescence[0][__.index_dir[0]][__.index_dir[1]][1]


				fichier = file(__.archive_ind, "rb")
				fichier.readline()
				ind_dossier = base_int(fichier.read(__.arborescence[1]))
				nbr_fichiers = base_int(fichier.readline()[:-1])
				read = None
				while ind_dossier <=index_dir:
					if ind_dossier == index_dir:
						fichier.readline()
						read = base_int(fichier.readline()[ : -1], 254)
						break
					else:
						for j in range(nbr_fichiers*3):
							if not fichier.readline(): ind_dossier = index_dir + 1
					ind_dossier = base_int(fichier.read(__.arborescence[1]))
					nbr_fichiers = base_int(fichier.readline()[:-1])
					if not nbr_fichiers: break
				fichier.close()
				add_files_in_dir(__.archive, liste, read)
				__.show_files_in_dir(index_dir)

	def slot_add_dossier(__):
		dossier  = qt.QFileDialog.getExistingDirectory(__, "Ajouter un dossier à l'archive")
		if dossier:
			if dossier[-1] != "/": dossier += "/"
			if __.Tabs.currentIndex() == 0:
				__.Struct2.List_dossier.addItem(dossier)
				__.Struct2.Dossier.setText("Dossiers : " + str(__.Struct2.List_dossier.count()))

	def slot_suppr_dossier(__):
		if __.Struct2.List_dossier.currentItem():
			__.Struct2.List_dossier.takeItem(__.Struct2.List_dossier.currentRow())
			__.Struct2.Dossier.setText("Dossiers : " + str(__.Struct2.List_dossier.count()))

	def slot_suppr_fichier(__):
		if __.Struct2.List_fichier.currentItem():
			__.Struct2.List_fichier.takeItem(__.Struct2.List_fichier.currentRow())
			__.Struct2.Fichier.setText("Fichiers : " + str(__.Struct2.List_fichier.count()))
	
	def slot_fusionner(__, fonction=fusion):
		__.Status_bar.showMessage("Fusion en cours")
		liste = []
		for i in range(__.Struct2.List_dossier.count()): liste.append(unicode(__.Struct2.List_dossier.item(i).text(), "cp1252")[:-1])
		for i in range(__.Struct2.List_fichier.count()): liste.append(unicode(__.Struct2.List_fichier.item(i).text(), "cp1252"))
		if liste:
			path = unicode(__.Path.text(), "cp1252")
			name = unicode(__.Struct2.Archive_name.text(), "cp1252")
			if path and name:
				if path[-1] != "/": path += "/"
				path += name
			elif path and not name:
				if path[-1] != "/": path += "/"
				path += get_name(liste[0])
			elif not path and name:
				path = get_path(liste[0]) + name
			else:
				if liste[0].count("."): path = ".".join(liste[0].split(".")[:-1])
				else: path = liste[0][:]
			if get_ext(path) != "fuz": path += ".fuz"
			fonction(liste, False, path)
		__.Status_bar.showMessage("Fusion terminée")

	def slot_change_path(__):
		dossier  = qt.QFileDialog.getExistingDirectory(__, "Dossier d'enregistrement de l'archive")
		if dossier:
			if dossier[-1] != "/": dossier += "/"
		__.Path.setText(dossier)

	def slot_ouvrir(__, start=False):
		if not start: __.archive = unicode(qt.QFileDialog.getOpenFileName(__, "Ouvrir archive", __.path*bool(not __.archive)+__.archive, "*.fuz"), "cp1252")
		__.Struct.Archive_name.setText(__.archive)
		if __.archive:
			__.archive_ind = ".".join(__.archive.split(".")[:-1]) + ".zid"
			type_ = int(file(__.archive, "r").read(1))

			__.Status_bar.showMessage("Indexation du contenu")
			if type_:
				if not file_exists(__.archive_ind):
					create_index_dir(__.archive)
				__.Status_bar.showMessage("Création de l'arborescence")
				__.arborescence = __.tri_arborescence(get_arborescence(file(__.archive, "rb")))

				__.show_dirs_in_dir(0, 1, False)
				__.show_files_in_dir(0)
				__.Struct.Name.setText(__.arborescence[0][0][0][-1])

			else:
				if not file_exists(__.archive_ind):
					create_index_file(__.archive)
					__.Status_bar.showMessage("Indexation terminée")
				__.Struct.Name.setText(".".join(get_name(__.archive).split(".")[:-1]))
				__.show_files()
			__.Status_bar.showMessage("Ouverture de l'archive terminée")


	def tri_arborescence(__, arborescence):
		liste = []
		for ind, path in enumerate(arborescence[0]):
			n = path.count("/")
			for i in range(n - len(liste)): liste.append([])
			name = path[:-1].split("/")
			path, name = "/".join(name[:-1])+"/", name[-1]

			#temp = (index_parent, index_self, nom)
			if n > 1:
				temp = (arborescence[0].index(path), ind, name)
			else: temp = (-1, 0, name)
			liste[n - 1].append(temp)
		return liste, arborescence[-1]

	def show_files_in_dir(__, index_dir):
		__.Status_bar.showMessage("Actualistion des fichiers du dossier")
		__.Struct.List_fichier.clear()
		fichier = file(__.archive_ind, "rb")
		fichier.readline()
		ind_dossier = base_int(fichier.read(__.arborescence[1]))
		nbr_fichiers = base_int(fichier.readline()[:-1])
		while ind_dossier <=index_dir:
			if ind_dossier == index_dir:
				__.Struct.Fichier.setText("Fichiers : " + str(nbr_fichiers))
				for j in range(nbr_fichiers):
					__.Struct.List_fichier.addItem(fichier.readline()[:-1])
					fichier.readline()
					if not fichier.readline(): ind_dossier = index_dir + 1
			else:
				for j in range(nbr_fichiers*3):
					if not fichier.readline(): ind_dossier = index_dir + 1
			ind_dossier = base_int(fichier.read(__.arborescence[1]))
			nbr_fichiers = base_int(fichier.readline()[:-1])
			if index_dir: __.Status_progress.setValue(50 + ind_dossier / index_dir * 50)
			else: __.Status_progress.setValue(100)
			if not nbr_fichiers: break
		fichier.close()
		__.Status_bar.showMessage("Actualisation terminée")

	def show_files(__):
		__.Status_bar.showMessage("Actualistion des fichiers")
		__.Struct.List_fichier.clear()
		fichier = file(__.archive_ind, "rb")
		fichier.read(1)
		nom = fichier.readline()
		nbr_fichiers = 0
		while nom:
			nbr_fichiers += 1
			__.Struct.List_fichier.addItem(nom[:-1])
			fichier.readline()
			fichier.readline()
			nom = fichier.readline()
		__.Struct.Fichier.setText("Fichiers : " + str(nbr_fichiers))
		fichier.close()
		__.Status_bar.showMessage("Actualistion terminée")

	def get_index_dir_in_arb(__, index_dir, nbr_slash):
		for ind, i in enumerate(__.arborescence[0][nbr_slash]):
			if i[1] == index_dir:
				__.index_dir = (nbr_slash, ind)
				break

	def get_index_dir_init(__):
		return __.arborescence[0][__.index_dir[0]][__.index_dir[1]][1]

	def show_dirs_in_dir(__, index_dir, nbr_slash=0, get_ind=True):
		__.Status_bar.showMessage("Actualistion des dossiers contenu dans le dossier")
		if get_ind: __.get_index_dir_in_arb(index_dir, nbr_slash-1)
		__.Struct.List_dossier.clear()
		nbr_dossiers = 0
		if nbr_slash < len(__.arborescence[0]):
			progress_max = len(__.arborescence[0][nbr_slash]) - 1.
			for progress, i in enumerate(__.arborescence[0][nbr_slash]):
				if i[0] == index_dir:
					__.Struct.List_dossier.addItem(i[-1])
					nbr_dossiers += 1
				if progress_max: __.Status_progress.setValue(progress / progress_max * 50)
				else: __.Status_progress.setValue(50)
		__.Struct.Dossier.setText("Dossiers : " + str(nbr_dossiers))
		__.Status_bar.showMessage("Actualistion terminée")

	def slot_open_dir(__):
		if __.Struct.List_dossier.currentItem():
			__.Status_bar.showMessage("Ouverture du dossier")
			nbr_slash = unicode(__.Struct.Name.text(), "cp1252").count("/")+1
			index_dir = __.arborescence[0][__.index_dir[0]][__.index_dir[1]][1]
			for i in __.arborescence[0][nbr_slash]:
				if i [0] == index_dir and i[-1] == unicode(__.Struct.List_dossier.currentItem().text(), "cp1252"):
					index_dir = i[1]

			if nbr_slash:
				path = unicode(__.Struct.Name.text(), "cp1252")
				for i in __.arborescence[0][nbr_slash]:
					if i[1] == index_dir:
						if i[-1]:
							if path and path[-1] != "/": path += "/"
							path += i[-1]
						break
				__.Struct.Name.setText(path)
			__.show_dirs_in_dir(index_dir, nbr_slash+1)
			__.show_files_in_dir(index_dir)
		else: __.Status_bar.showMessage("Aucun dossier sélectionné")

	def slot_retour(__):
		if __.index_dir[0]:
			__.Status_bar.showMessage("Ouverture du dossier")
			index_dir_parent = __.arborescence[0][__.index_dir[0]][__.index_dir[1]][0]
			__.get_index_dir_in_arb( index_dir_parent, __.index_dir[0]-1)

			ind = __.arborescence[0][__.index_dir[0]][__.index_dir[1]][1]
			__.show_dirs_in_dir(ind, __.index_dir[0]+1, False)
			__.show_files_in_dir(ind)
			__.Struct.Name.setText("/".join(unicode(__.Struct.Name.text(), "cp1252").split("/")[:-1]))
		else: __.Status_bar.showMessage("Vous êtes déjà à la racine de l'archive")

	def slot_extraire_all(__):
		if __.archive:
			__.Status_bar.showMessage("Defusion en cours")
			path  = unicode(__.Path.text(), "cp1252")
			if not path: path = get_path(__.archive)
			if __.Struct.Name.text() != get_name(__.archive)[ :  -4]: name = unicode(__.Struct.Name.text(), "cp1252")
			else: name = ""
			defusion(__.archive, False,False,path+name)
			__.Status_bar.showMessage("Defusion terminée")
		else: __.Status_bar.showMessage("Aucune archive ouverte")

	def slot_extraire_file(__):
		if __.Struct.List_fichier.currentItem():
			__.Status_bar.showMessage("Extraction du fichier en cours")
			filename = unicode(__.Struct.List_fichier.currentItem().text(), "cp1252")

			fichier = file(__.archive_ind, "rb")
			fichier.readline()

			ind_dossier = base_int(fichier.read(__.arborescence[1]))
			nbr_fichiers = base_int(fichier.readline()[:-1])
			index_dir = __.get_index_dir_init()
			while ind_dossier <= index_dir:
				if ind_dossier == index_dir:
					for j in range(nbr_fichiers):
						temp = fichier.readline()[:-1]
						if  temp == filename:
							start = fichier.readline()[:-1]
							stop = fichier.readline()[:-1]
							extract_file(__.archive, filename, base_int(start, 254), base_int(stop, 254), unicode(__.Path.text(), "cp1252"))
							ind_dossier = index_dir + 1
							break
						else:
							fichier.readline()
							if not fichier.readline(): ind_dossier = index_dir + 1
				else:
					for j in range(nbr_fichiers*3):
						if not fichier.readline(): ind_dossier = index_dir + 1
				ind_dossier = base_int(fichier.read(__.arborescence[1]))
				nbr_fichiers = base_int(fichier.readline()[:-1])
				if index_dir: __.Status_progress.setValue(50 + ind_dossier / index_dir * 50)
				else: __.Status_progress.setValue(100)
				if not nbr_fichiers: break
			__.Status_bar.showMessage("Extraction du fichier terminée")
		else: __.Status_bar.showMessage("Aucun fichier sélectionné")

	def slot_extraire_dir(__):
		if __.archive:
			__.Status_bar.showMessage("Extraction du dossier en cours")
			__.Status_progress.setValue(0)
			nbr_slash = unicode(__.Struct.Name.text(), "cp1252").count("/")+1
			index_dir = __.arborescence[0][__.index_dir[0]][__.index_dir[1]][1]
			if index_dir:
				extract_dir(__.archive, __.get_contenu(index_dir), unicode(__.Path.text(), "cp1252"))
			__.Status_progress.setValue(100)
			__.Status_bar.showMessage("Extraction du dossier terminée")
		else: __.Status_bar.showMessage("Aucun dossier sélectionné")

	def get_index_arborescence_dir(__, nbr_slash, index_dir):
		yield index_dir
		if len(__.arborescence[0]) > nbr_slash:
			for dossier in __.arborescence[0][nbr_slash]:
				if dossier[0] == index_dir:
					for i in __.get_index_arborescence_dir(nbr_slash + 1, dossier[1]): yield i

	def get_contenu(__, index_dir):
		liste_contenu = []
		fichier = file(__.archive_ind, "rb")
		fichier.read(1)
		nbr_c = base_int(fichier.read(1))
		fichier.read(1)
		arborescence = get_arborescence(file(__.archive, "rb"))
		num_dossier = base_int(fichier.read(nbr_c))
		nbr_fichier = base_int(fichier.readline()[:-1], 254)
		while num_dossier != index_dir:
			for i in range(nbr_fichier * 3): fichier.readline()
			num_dossier = base_int(fichier.read(nbr_c))
			nbr_fichier = base_int(fichier.readline()[:-1], 254)
		liste_contenu.append([arborescence[0][num_dossier], []])
		liste_fichier = []
		for i in range(nbr_fichier):
			nom = fichier.readline()[:-1]
			start = base_int(fichier.readline()[:-1], 254)
			stop = base_int(fichier.readline()[:-1], 254)
			liste_contenu[-1][1].append([nom, start, stop])
		dossier = arborescence[0][base_int(fichier.read(nbr_c))][:-1].split("/")
		nbr_fichier = base_int(fichier.readline()[:-1], 254)
		lim = len(liste_contenu[0][0])
		path = get_path(__.archive)
		lim_start = len(path)
		index_slash = len(liste_contenu[0][0][:-1].split("/")) - 1
		name = get_name(liste_contenu[0][0][:-1])
		liste_contenu[0][0] = path + name
		lim_end = lim_start + lim
		while dossier[index_slash] == name:
			liste_contenu.append([path + "/".join(dossier[index_slash:]), []])
			for i in range(nbr_fichier):
				nom = fichier.readline()[:-1]
				start = base_int(fichier.readline()[:-1], 254)
				stop = base_int(fichier.readline()[:-1], 254)
				liste_contenu[-1][1].append([nom, start, stop])
			dossier = arborescence[0][base_int(fichier.read(nbr_c))][:-1].split("/")
			if len(dossier) <= index_slash: break
			nbr_fichier = base_int(fichier.readline()[:-1], 254)
		return liste_contenu

