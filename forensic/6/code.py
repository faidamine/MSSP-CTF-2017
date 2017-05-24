import qrtools
import glob


for filed in glob.glob('./qr_img/*.png'):
    qr = qrtools.QR()
    if qr.decode(filed):
         if "msspctf" in qr.data:
           print('result: ' + qr.data)
           break
    else:
         print('error: ')
    


#msspctf{VeryLongKeyYouWillNeverGuess}
