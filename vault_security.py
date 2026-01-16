# vault_security.py

def check_password(pwd):
    # Comprovació de longitud mínima (8 caràcters)
    if len(pwd) < 8:
        return False

    # Comprovació de si conté almenys un número
    if not any(char.isdigit() for char in pwd):
        return False

    # Comprovació de si conté almenys una majúscula
    if not any(char.isupper() for char in pwd):
        return False

    # Comprovació de paraules prohibides (admin)
    if "admin" in pwd.lower():
        return False

    # Si passa totes les regles anteriors
    return True
