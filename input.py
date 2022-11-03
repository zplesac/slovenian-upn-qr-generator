from models import SlovenianQRCode


def get_data() -> SlovenianQRCode:
    iban = input(f"Enter IBAN: ")
    reference = input(f"Enter reference: ")
    date = input(f"Enter date: ")
    description = input(f"Enter description: ")
    code = input(f"Enter code: ")
    name = input(f"Enter name: ")
    street = input(f"Enter street: ")
    city = input(f"Enter city: ")
    amount = input(f"Enter amount: ")

    if amount:
        amount = float(amount)
    else:
        amount = 0.0

    return SlovenianQRCode(iban=iban, reference=reference, date=date, description=description, code=code, name=name,
                           street=street, city=city, amount=amount)
