def name():
    return "Vector"

def author():
    return "Oliver Vladimir Camargo Lopez"

def authorName():
    return author()

def email():
    return "oliver.ovc@gmail.com"

def description():
    return "vector"

def about():
    return "Vector"

def version():
    return "0.0.1"

def qgisMinimunVersion():
    return "3.0"

def icon():
    return "vector.png"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)