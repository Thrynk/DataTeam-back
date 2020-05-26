
class Button:
    """
    Pour les boutons dans la nav bar

    Button(name,href,active=False)
        name : nom du bouton a afficher
        href : nom de l'url qui renvois
        active : si il est actif ou non (couleur)
    """
    def __init__(self,name,href,active=False):
        self.name=name
        self.href=href
        self.active=active

class URL:
    home='home'
    login='appUser.login'
    register='appUser.register'
    logout='appUser.logout'