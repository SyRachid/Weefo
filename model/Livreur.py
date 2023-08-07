class Livreur():
    def __init__(self,nom_utilisateur, mdp,num_fone,num_cnib,dispo):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        self.num_fone = num_fone
        self.num_cnib = num_cnib
        self.dispo = dispo
    def set_nom(self, new_nom):
        self.nom_utilisateur = new_nom
    def set_mdp(self,new_mdp):
        self.mdp = new_mdp
    def set_num_fone(self,new_fone):
        self.num_fone = new_fone
    def set_num_cnib(self,new_cnib):
        self.num_cnib = new_cnib
    def set_dispo(self,new_dispo):
        self.dispo = new_dispo
    