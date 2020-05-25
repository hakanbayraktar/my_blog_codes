
"""
    )   (           (                                   
 ( /(   )\      )   )\   (         )           )   (    
 )\()) ((_)  ( /(  ((_)  )\ )   ( /(   (    ( /(   )(   
((_)\   _    )(_))  _   (()/(   )(_))  )\   )(_)) (()\  
| |(_) | |  ((_)_  | |   )(_)) ((_)_  ((_) ((_)_   ((_) 
| '_ \ | |  / _` | | |  | || | / _` | (_-< / _` | | '_| 
|_.__/ |_|  \__,_| |_|   \_, | \__,_| /__/ \__,_| |_|   
                         |__/                           

"""


from PyQt5.QtWidgets import *
import sys
'''Uygulamanızın ana penceresini özelleştirmek için alt sınıf QMainWindow'''
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)#Pencere başlığımız
        self.setWindowTitle("Pencerede Neler Varmış???")
        
        
layout = QVBoxLayout()
        widgets = [QCheckBox,
            QComboBox,
            #QCalendarWidget,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QListWidget,
            QLineEdit,
            QDialogButtonBox,
            QProgressBar,
            QPushButton,
            QRadioButton,
            #QTimer,
            QSlider,
            QSpinBox,
            QTimeEdit]
            
            
            
for w in widgets:
        layout.addWidget(w())
               
        widget = QWidget()
        widget.setLayout(layout)
        
        
self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show() # Onemli!!!!! Pencere default olarak gizli durumda.
app.exec_()
