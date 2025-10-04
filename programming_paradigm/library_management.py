class Book:
    """Représente un livre avec un titre, un auteur et son état (emprunté ou non)."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # attribut privé : True si le livre est emprunté

    def check_out(self):
        """Marque le livre comme emprunté."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marque le livre comme disponible."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Vérifie si le livre est disponible."""
        return not self._is_checked_out


class Library:
    """Gère une collection de livres et leurs opérations."""

    def __init__(self):
        self._books = []  # liste privée des livres

    def add_book(self, book):
        """Ajoute un livre à la bibliothèque."""
        self._books.append(book)

    def check_out_book(self, title):
        """Permet d’emprunter un livre si disponible."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # (Optionnel) Tu pourrais afficher un message si le livre n'existe pas ou déjà emprunté

    def return_book(self, title):
        """Permet de retourner un livre emprunté."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """Affiche tous les livres disponibles."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
