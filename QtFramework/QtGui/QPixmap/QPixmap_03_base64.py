#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QPixmap사용

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import qUncompress
from PyQt5.QtCore import Qt


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.init_ui()

    def init_ui(self):
        by = b'AAASDHicnVdlUBSO076DOySlUzqkuxuU7pRG8hAE6QY5uhvkaCXlSEGk4TyPUv' \
             b'BoCQlJT+CkO/7+Pr/f3mfm2Zjd2f2wszuzyUYGmiSEDIQAAIBEW0vN5J9W+Y/4' \
             b'eP8k3N135Z8C+T/RNsP/hwh8l6R/PoGPlpU/AEBE+R+BgKISun85D9zNLAMs9f' \
             b'XknL29hBxdvJ1chUK8fABAgLmZhqAM4P9GXkTvF4+/qtegGj4PJUQtfzRxvGj5' \
             b'zKoX8LL2HPJLSsdk2UW2jN6TyoFnbX60PnBS8w9/AN5NNEmGwGmQKZOLzaHszv' \
             b'296JfCQ08KW28/PXvL6rEF9u9Df1aj7qr5RJnqVxPEnd8YzovdXdm3JJ4/Zxm9' \
             b'Jjp8H8ZkD34UlbvNW9/Sqp3bcCLtTG2q5NZ/YZOQDZ/hmv1meStA+XV6z6DwII' \
             b'b36fJkkrtNyi5me6JNI7ac6psIkwtxFsa9Zj/1B8LoUwGDfTL67dvsKOVb11TK' \
             b'1aE/rXA/lnenYY3NXqW0RGznCi6WI60Sxu/yva3ipa2fvfbQC1IyfZbD/r0e5p' \
             b'Zyk7ETYZ5ufqrjbrfkW33JnJcfpqhRekDl5ZOht6zipta2MNwqsW/+Znb85emH' \
             b'1oiIb/TdblzPqeOWe1sbrmbc1EdXuJ9Taysq57G+aTHT0vnlerbypH+TWrjgZq' \
             b'zzHNNW2bzO8+fH1zEr+iWUm4vY9AgyVogsd8+QMIHfXsGvLE6/YHn/lWGhnosF' \
             b'yem7oy8dMpURdnd0b02Ny1mKU4J5PjZBiCWmQyWIF7KfGorbropYP9bfSh7WC1' \
             b'AepO5Hbb0/m0mclgnrGdkyCt0TLb7ssLL6lday5M6DE8Zouhpgt945Nue5rrHI' \
             b'w0A2zhHwduENZSGHswoHBzw9c4tpl5ebf0GH/YdA5NfkllXpJO+2kbJMAZs2AY' \
             b'ufvaO2JKT68PSGrmTFR8Uum3sqgm0Pf3ew08hTGlhL+gmYITT8Y4vefJYYpuu2' \
             b'Rm1abp9pPQqROBKpPp5E/GQL85R73+zLa70hqPAHHYYOcYhi1AxO5mw6z2Kk5c' \
             b'rV9W/AztUskmvp96Ei9TaxlDnd6S+gGRU7rr7nvvZSYKbL0KGw0dZM6ybzwJWq' \
             b'TeP2IfB1L5l45MLiHmUQhFHS9I5FIYVi4K7nge9C91W5QhIuVMD3k4OEmvwvIZ' \
             b'+FtpcVw/UvO5x66kXfojJDstf50kx7HXjQNEA5kE1+YuQLJKV9kn5OfBD0CtkH' \
             b'XxrdbFozLmlp6b0/avMLF/fVQ/tK6EovSTV2v8m8qcuVz4DJ23bkTAQ41Z4att' \
             b'rlmpf6Cz61Hckrt3GXj+SLvLO8uok+ybpSTK2fWNQxQArm3yi+gvxVZWQqZFx0' \
             b'//3xSmilZdOdITWyI+98jfhT0bRa88FlyUEXh+diXSDipUHmi/AIKm6Lj8rdZ5' \
             b'Kn5wMAHDIoAMQKAOKr/H/My+9Z9Q736LcClc6BjfaJ94B2C/KKAsJo2X/3pFhb' \
             b'TdUspGS/WD/N3i1wOGqnhJ++2onayTFtg95QgMvY0fibaIwdzUIVRToFbZ06Hw' \
             b'GeOi84WZ3qHX5+K1R9nisbIeNebQaO0bV8q2NVtWw0WzeGQxNIvUf/0ukx0uUp' \
             b'Z1x1OBazftnbPDDUzJQO3xSCrJyv7Cidy977f7+P+LmTn7TWF/HbQNihNvMcOI' \
             b'8B750cKgHk+6ClSivHAOK/25vKl6MDKXWF8H3RaWXTtsz6xWWp3/C6fcnZpXHP' \
             b'Apid2GzH+F4MvKkYQ29+XV10i1TrUBskZVa4aEK97JoNRegK93HCPSCfhseYRW' \
             b'avZ/dyIZ8q4DASGK9HQt27xzB6viGHFJgjHMbg1O1Yc+9e0Vy3UA/vdvXoj3K9' \
             b'F7Q5EcRduzjcqKjpwXv0zHzfUfyWSFw+L46JLkcFxgBJMQdIACvoYdiSundFCJ' \
             b'PJachVCrzMrD3QvCtgpzR45WTdmwCAVry/cYCHj+0Jj++9L2SatDfSjZlBQ4jb' \
             b'/K0OIjIh/Fo/2stoRcdO8uD9DXBlsbbGyOuzdOm2s+J1qFv/MRP9jNJ7yLljBP' \
             b'mm6poUFF9lSoZXOomVHbqmkoWn3kGWXUWWHGQoAnyLp8cIVMJjBPZ3dHVddr/v' \
             b'P57sCy+Y2pwCRFzbrNJI9n355cjJTC1TAvLazRJVVgU9JQOhpwjVjTQ5fWI80o' \
             b'whfM4UoCc4c7+koiuB/JRHFYhRaWHbzk5ifF3gQbr3TeyiAwtzEho3E8i/5h6v' \
             b'Hqu+X2YwStYJiiYHwwTMpBJv9KeUy9GU42lGhUeCfnQ3D9mUOH3WkfFE3vvLPc' \
             b'Hd5Fav6KC15a+t9fa/sB92cHz5AAwSziAA2bZkQe6d37ArTyqmE4N2sZSI4bdl' \
             b'DUKsWi4LnC/e1PCnRGijlFVQ/rQrvS3t55VLHXGPcNZGucupxHtwLxSYh3GCiH' \
             b'DZYrRqA1OEcOkFiXI/jywWgCl5n2vGAGGEzzmr4Gu/QpvweaCsPWDFhEGWZEyP' \
             b'9PpDaRD0+kR1zTFrGLoczfqLLNpZDSFCddiW8YRCJUTUxyfJZ2yRQZFVYHnHBB' \
             b'tPJ8eMTxZb58Ctuq6pGrccooB3YxAbhfc6Shd40SMcFSrSzvFEgQ+p82GygsyW' \
             b'75hU1dq9C7tQzUV/mzVb2qDRzfNLknAGmM/Cqubwx/2ZuxKNwyeK6ROer83S0t' \
             b'L3kfJsfjYAhbuLjQp4OOoCycNYk2M5624Xi58GxMWRGkgAxXHZjCwKr3i6lv3e' \
             b'OePz+muvvbECTQpaYX8oHwGUafs36+3+yOsmDOESDmI5OJox8PDBYQMVrYCoTd' \
             b'nj5gm2ChuHZMJL63Uc7iqCZfIIOQ2H32LxCppqOAok0/Ao8ug6hWGjQuaStQHo' \
             b'TrTyChWg/LoYnVzYiLygp3u126wNtZzKowISPuRKC2VlO9YqQGn/cHXsZxOzJC' \
             b'nJwMtdykMj8o5TN58Xhsct4Sjh3ixdHu+g91ajThd/dQMuNhNQHCM+5SNJSVvm' \
             b'3yJsRbdF6OQShO+5KOgzPpIlcjt44HGmbx0jUPTqfwVRmh8IyXOqLdkn9VJA59' \
             b'oH+AeCOfqCBNBr5rVpddj7Xe9y+LauwAk5koY1BmGKZwn24KCgf+x3KNePMGMc' \
             b'P5q/7OXNhdF8B+ceYGDrLNHj9aPB+gBm2TCzsT3gmhG3unXEm3s/Gx6iLHasp8' \
             b'pUpxmLZpqYnd8FOebNLLToKIKo/cuW3rwyNitB0edsb4F2bm6u6TfeD5CDn3T0' \
             b'dTKsEjteTsQ1DhmYqvR8bdVaVAmZMHm6LXAmupNholS9pLuoYBEzZu6njFT2pZ' \
             b'bufAxQumRWVVKH0oIgVdSdXOmWtOhHG7jksh259A758+w7+I9Hm6uBi2hZG1rZ' \
             b'5e8bJjJau0klrzWTCZG1MBdSC9/YXUtEwAvU+SNji5LWgVdZF67WL65y5TQIS4' \
             b'eTXNvKEweys9jME7mejjFPNQjW/rj14lSfOcSfxieO4bSfJ/V7wQuIKFKa05aj' \
             b'zKooBd8noMbeUEZZfYxMVQsBbrAeg0MyCBshHu4fJnSQWVjnIDQvpU9dcZ8Cmd' \
             b'ZtrMW/LR29xVbswxHYMDWDM6dX78mz/Ss3Pwz91GTiFqhGMQ+W0CI9RKYDxT7y' \
             b'wwo5d4Q0phveWYF9zmddesvAjFDWqul16hmhAPDrmoDsJ6bJs7mP5ZnJfc73dl' \
             b'1aaJ7UchJwDl+xZ6vRcmnUbduza4xIFDvF4OoCRS4vyJFN79kwnmyBoTlduoVz' \
             b'/EpQyoc0qVISuZT0INpCXPCFTIwVWBlJL8dOiCagG6Tzb6Fiq0lWvRgxAXQadk' \
             b'xvrWIuSZIWnigqP4uLVlouThydk+6MWUDrpFoedPk5y2FWynUdT46SsoeR+//1' \
             b'+8iPtn9mntqdEZOdbUtJJTAFwCDte56t8Th+KE97OKb1p4G6evNJ6vZBqBBB/S' \
             b'f7qQBMzgOChXaqf7Plak2Mdov2oxDTeOnNFpdmib5IQ8kg1rpq2hZ+fh5REXEi' \
             b'Hhmrhjuox31Fvfmuu2pUpR5vQgyuizkJ8EZUbwEOMF5rhpA5BiYMWqc3wBEy/6' \
             b'sThJooeTFUniyiyK1awK20UKZQGEIUbx9OCi5+b8xulSfPq6oTvbFfDYA9vk/H' \
             b'D5bqMPT6Zv0hX32OAk1PZGyOV9nEzolI/5Znh7SRIR7ji36ldjd9qItVJJ7qod' \
             b'X6KHppPGBFAcWUJEXg6IizC6q4jowtd8ulA4vKU8fGldKzXHiJ0qjLrN3Zq735' \
             b'tPCCsn+mSObL/nQuY5w01oQ7fxcEQ3vKtf1RMXOM3RYeTNLCVPqNhvNp8gOAbC' \
             b'0vcXLIqeqzDUvjUjf6ffyfiUp0bk+LNBupZDbHTAAoiVuPHIMOwT9kg0xfN6oI' \
             b'JgdoYlVs6ZxdXhAIra+NFtAlq70lgjP3qQ86EQnG4WRjQd1S4e4tLru6fR3PBc' \
             b'EIGf1aku+aLcrJUwSPeavN/fqx2Ze9Pxm1flxqx4Q9rGGi3y6x08K8whbMVMbP' \
             b'Aj9Tks11JRRYvOIQnd/rZ6RAJ/qE8QKcjhoJXj/ca+bEMpm61eqGqnhYhaidDu' \
             b'bczZWp5nWWT++COzzCcvHMyGuQRqC8ZzxcxMWFc7xMyRey83MmgAsJWbZmgiOL' \
             b'6Np1MT/NmhwnzHj1il1KQqRIgAZBgufDNh5jmEf2VsUp2YNk+gdUNSzV5G6lSN' \
             b'PX2RSVOjnNbG39f86AMsfKbutl4dhQ6h2JF16p+R1dm3FVfUdl3fNLWzuh0Vw5' \
             b'Mz6z3NBlHZCJNL1Pwp+wNphYENaY48GCZLyPZtI0+dGfp6SKAYNB84FAgM+5YF' \
             b'q5mC/PlfmDy8PIywVJ7R5Si0yKSyXRKrW0BZDdlGntX9h8z+FkIIt10cG0Qy/8' \
             b'0psIyot0LXrNiCrHPR9vphFJ4eXW5Xk5zgzUCmN6bEe/ymFcEUdC3dp/v8pcAC' \
             b'DHIJo0M3QbG8+6EZmj7ktTgJurdOn1ph6stfReoqlelM5iyQSN2YolegXjekxS' \
             b'5+09JKqZrOCZ5tASWu8iwEftdsLqBEu10tkruRg7bgB9/+2QFpVF9/o38up51F' \
             b'mbheS9FxAgom7rdFTw9ALkQyVXrTnpu/QVZ4yuv/Xyd1XHViFRiga/LifEu2a5' \
             b'YyYsfASsPR709ZLi6UXhhrC4fR8+3/AngEzwmWcDk0yLJO9wNHXclz6H7Egj2t' \
             b'ybnC3tJlwQLCX3o2YtPLhK1ih3OpHdkT/gT7ChdubsiTXg7pHMQ08m+aC9osVV' \
             b'KQDADV36iPRfHS5KYQMkEz7/+uA3/xFe7MSt16lyXUXbTeQ7OrIcojy2U496n6' \
             b'xJv9V3SxZT7asH8y0ttNGmhgqHqE9BmcsTeMmwmmBb2VFOFpz+uK9YHt/mwdgu' \
             b's82ATxThARNVRtZn+Jw8pmhvqq607ZTavJMOE0jOfQeZMJmfidrKQpOeNAhxda' \
             b'XR0NBgCzIARQBk8PZo3JG653UbIwsPs2oGZuyze9vV/Icosou4QnsI7LCFhA0R' \
             b'Nb0N9PGrDBEsMmwXg80RW/U/JG+rAYD5+fmk/Nn8DlBZ8VTP+TDiWVpdYJXY08' \
             b'caryLomBzzZ+oSNFg+vJgIWWHhVDMI3TkTwemk/DzE2qvi82StsbYszGMJKQwG' \
             b'IIauhj52d7eCj+zWghGViF9Xm4zXJm1yi8+YPTa6v1M7f8MBt2KCGQYEZD0SuZ' \
             b'Hhk4oGFF8GmyNvd6U5FX6iNEZPT9Mt7az6tBazThIQtNzrqrzy6vXw9jnSU8us' \
             b'wT43Mm/W/CInznZkIgPuHfRAfC0csYuQX73ZXl1tOfDJtXH9IT2He3G7uLgYBb' \
             b'iv99HJqlRj1M53ZrCQEqJqPV780G1bv4XvcHDEIBc/0euMNWMVJh3JFPlUFrpd' \
             b'WLzIH/EtKLW5sTEZjjVpN5eMnOfcp/nx+kHICqPiKqg0OJ3U3T9gUc3Ly6aPT4' \
             b'oulqTW/JRaXN4dsgsJwiy4lfdhBlePVokYFUKMZmb0vDLhSm89zotHuc291HeD' \
             b'LvFiMFAaVS/YPQSRcBIOnP0RQGcv2S74aMYw4h7136vw4K0ytu/c3nj2LJW8Pb' \
             b'MYswzvhkPC9feDxJerb4U1xub0T9OKbv2MruNJPrnC74SVLz73tE4EU0PvSYfD' \
             b'7zRN/+K2TBPNYzYiAUFhQPnIG5axlCmO0mvWRsA/aKsbqDU9cYj5Hz3VwP4='

        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        lb = QLabel()
        lb.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        layout.addWidget(lb)

        base64_image = QByteArray.fromBase64(by)
        base64_image = qUncompress(base64_image)
        image = QImage.fromData(base64_image, 'image')
        pixmap = QPixmap.fromImage(image)
        lb.setPixmap(pixmap)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())