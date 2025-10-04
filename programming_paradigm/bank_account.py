class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialise le compte avec un solde optionnel (par défaut 0)."""
        self.__account_balance = initial_balance  # attribut privé

    def deposit(self, amount):
        """Ajoute de l'argent au compte."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        """Retire de l'argent si le solde est suffisant."""
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
            return False

        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Affiche le solde actuel."""
        print(f"Current Balance: ${self.__account_balance}")
