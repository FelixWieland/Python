#Skript zum erstellen einer .py Datei
import time, socket

def create_py_TEMPLATE():
	datei = open("TEMPLATE.py", "w")
	TEMPLATE_created = '''#SCRIPTNAME - CREATED: ''' + str(time.strftime("%d.%m.%Y %H:%M:%S"))
	TEMPLATE_from = '''\n#CREATED BY: ''' + str(socket.gethostname())
	TEMPLATE_main = '''\n \n \nif __name__ == '__main__':\n	'''
	datei.write(TEMPLATE_created + TEMPLATE_from +  TEMPLATE_main)
	datei.close()

if __name__ == '__main__':
	create_py_TEMPLATE() #Erstelle neue .py datei
