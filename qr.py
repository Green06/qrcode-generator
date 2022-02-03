from ensurepip import version
import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size =5,
    border = 2
)
data=input("enter text")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save('text3.png')
