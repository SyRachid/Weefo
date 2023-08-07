class Livraison():
    def __init__(self,Client,Livreur,etat_livraison):
        self.Client = Client
        self.Livreur = Livreur
        self.etat_livraison = etat_livraison
    def set_Client(self,newClient):
        self.Client = newClient
    def set_Livreur(self,newLivreur):
        self.Livreur = newLivreur
    
