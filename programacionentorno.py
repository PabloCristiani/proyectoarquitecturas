import psycopg2
from psycopg2 import Error
connection= psycopg2.connect(user="pi",password="123456",host="127.0.0.1",port="5432",database="pi")
cursor=connection.cursor()

import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
print("\nTemperature: %0.1f C" % bme280.temperature)
print("Humidity: %0.1f %%" % bme280.humidity)
print("Pressure: %0.1f hPa" % bme280.pressure)
print("Altitude: %0.2f m" %bme280.altitude)
temperature=[]
humidity=[]
pressure=[]
altitude=[]
val=0
tiempo=[]

from ventana1 import *
import matplotlib.pyplot as plt

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        #actualizar()
        self.pushButton.clicked.connect(self.actualizar)
        
         
    def actualizar(self):
        global temperature,humidity,pressure,altitude,tiempo,val
        
        temperature.append(bme280.temperature)
        humidity.append(bme280.humidity)
        pressure.append(bme280.pressure)
        altitude.append(bme280.altitude)
        tiempo.append(val)
        val+=1
        print(temperature)
        print (tiempo)
        print("Valor Temperatura")
        self.label_8.setText(str(float(bme280.pressure)))
        self.label_3.setText(str(float(bme280.temperature)))
        self.label_5.setText(str(float(bme280.humidity)))
        self.label_7.setText(str(float(bme280.altitude)))
        self.pushButton.setText("Accionado")
        plt.title('Mi grafica')
        plt.plot(tiempo,temperature,tiempo,humidity,tiempo,pressure,tiempo,altitude)
        plt.grid(True)
        plt.show()
        
                
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



