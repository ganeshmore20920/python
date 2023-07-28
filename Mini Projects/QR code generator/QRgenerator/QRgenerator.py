from turtle import bgcolor
import qrcode
import image
qr = qrcode.QRCode(
    version= 15, #15 means the version of the qr code high the bigger the code image and complicated picture
    box_size= 5, # size of the box where qr code will displayed
    border= 5 # It is the white part of the image -- border in all 4 sides with white color
)
data = "Sonu"
#above data will be converted into qr, we can make it user friendly also

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill= "black", back_color = "White")
img.save("test2.png")























# from textwrap import fill
# import qrcode
# import image
# qr = qrcode.QRCode(
#     version = 15,
#     box_size= 10,
#     border=5
# )
# data ="तू लय भारी दिसतेस लखा तृप्ती..."
# qr.add_data(data)
# qr.make(fit= True)
# img = qr.make_image(fill = "Black", back_color = "white")
# img.save("userinputqr.png")