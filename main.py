from pyscript import document, display


# ICT Tech Club directory. Checks case-insensitive.
MEMBER_NAMES = {'Christopher Francis, De Vera','Jan Immanuel, Cabading','Carlos Eziquel, Borromeo','Jericho, Magsalin','Louie Vonn, Lee','Gerthy, Bausa',}

#lookup process
def add_member(e):
    first_name = document.getElementById("first-name-input").value.strip().lower()
    last_name = document.getElementById("last-name-input").value.strip().lower()
    input_name = f"{first_name}, {last_name}"
    membernames_upper = {name.upper() for name in MEMBER_NAMES}
    membernames = membernames_upper.union({input_name.upper()})

    
    display(membernames, target = "output1")

