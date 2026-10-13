from pyscript import document, display


MEMBER_NAMES = [
    "Christopher Francis, De Vera",
    "Jan Immanuel, Cabading",
    "Carlos Eziquel, Borromeo",
    "Jericho, Magsalin",
    "Louie Vonn, Lee",
    "Gerthy, Bausa",
]


def normalize_name(name):
    return " ".join(str(name).strip().split()).lower()


def add_member(event):
    first_name = document.getElementById("first-name-input").value.strip()
    last_name = document.getElementById("last-name-input").value.strip()
    full_name = f"{first_name}, {last_name}".strip(", ")

    if not first_name or not last_name:
        display("Please enter both names.", target="output")
        return

    exists = any(normalize_name(name) == normalize_name(full_name) for name in MEMBER_NAMES)
    if not exists:
        MEMBER_NAMES.append(full_name)

    sorted_members = sorted(MEMBER_NAMES, key=normalize_name)
    display("Roster", target="output")
    display(sorted_members, target="output")v
