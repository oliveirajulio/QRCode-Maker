import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://oliveirajulio.github.io/mn-transparency/#/list")
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

logo = Image.open("snglogo.png")
logo_size = 400
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

qr_img.paste(logo, pos, mask=logo)

qr_img.save("qrcodelist.png")
