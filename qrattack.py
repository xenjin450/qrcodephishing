import qrcode 
import os 
import subprocess 
import requests 
import webbrowser
import qrcode
import PIL 

#Define QRCode
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

#Input QRCodeData 
img = qr.add_data("http://malicioussite.com/")
#Specify Image Data Type
type = (img)
#Creates a Image from the QRData
img = qr.make_image(fill_color="black", back_color="white")
#Save Image File
img.save("QRAttack.jpg")
