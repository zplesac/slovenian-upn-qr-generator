class SlovenianQRCode:

    def __init__(self, iban, reference, date, description, code,name, street, city, amount):
        self.vodilni_slog = 'UPNQR'
        self.iban = iban
        self.reference = reference
        self.date = date
        self.name = name
        self.description = description
        self.code = code
        self.street = street
        self.city = city
        self.amount = amount
        self.code = code
        self.description = description

    def __str__(self):
        return self.to_qr()

    def to_qr(self):
        return  f"{self.vodilni_slog}\n\n\n\n\n\n\n\n{self._format_amount()}\n\n\n{self.code}\n{self.description}\n{self.date}\
    \n{self.iban}\n{self.reference}\n{self.name}\n{self.street}\n{self.city}\n{self._calculate_control()}"

    def _calculate_control(self):
        control = 0

        for attr, value in self.__dict__.items():
            if attr == "amount":
                control = control+len(self._format_amount())
            else:
                control = control + len(value)

        if control >= 100:
            return control
        else:
            return "0" + str(control)

    def _format_amount(self):
        value = str(int(self.amount * 100))
        value_size = len(value)

        for i in range(value_size, 11):
            value = "0" + value

        return value
