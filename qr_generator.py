import qrcode
from datetime import datetime
from input import get_data

data = get_data()
qr = data.to_qr()

print("\n---- GENERATED DATA FOR QR --------")
print(qr)

img = qrcode.make(qr)
filepath = f"img/{datetime.now()}.png"
img.save(filepath)
img.show()
