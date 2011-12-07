#=[site officiel]=======================
#<<<<<mod_unicode by W3YZOH0RTH>>>>>
#=========[http://progject.free.fr/]======
def encode(unicod):
    """Convertie une chaine de type unicode en type string"""
    if type(unicod) != type(""): return unicod.encode("cp1252")
    return unicod

def decode(string):
    """Convertie une chaine de type string en type unicode si possible"""
    if type(string) != type(u""): return unicode(string, "cp1252")
    return string

def force_encode(unicod):
	"""Convertie une chaine de type unicode en type string en remplacant les caracteres non convertissable en "_" """
	if type(unicod) != type(""):
		try:
			return unicod.encode("cp1252")
		except:
			string = ""
			for c in unicod:
				try: string += c.encode("cp1252")
				except: string += "_"
			return string

	return unicod
