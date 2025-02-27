class New:
    """
    Classe permettant de simuler le mot-clé 'new' en Python.

    Exemple d'utilisation :
    >>> new_person = New("Person", "John", 30)
    >>> print(new_person.get_instance())
    John, 30 ans
    """

    def __init__(self, class_name, *args):
        """
        Initialise une instance de la classe spécifiée par `class_name`.

        :param class_name: Le nom de la classe à instancier.
        :param args: Les arguments à passer au constructeur de la classe.
        """
        self.class_name = class_name
        self.args = args

    def get_instance(self):
        """
        Crée et retourne une instance de la classe spécifiée.

        :return: Une instance de la classe.
        """
        cls = globals().get(self.class_name)
        return cls(*self.args) if cls else None
