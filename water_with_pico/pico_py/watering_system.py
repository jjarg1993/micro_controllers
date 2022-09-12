import machine
import utime
from machine import Pin

adc_pico = machine.ADC(26)
motor = Pin(22, Pin.OUT)
trocken = 600
feucht_genug = 350


def average_humidity():
    average = 0;
    for x in range(8):
        average = average + adc_pico.read_u16()
        utime.sleep(1)
    return average/8
      
print(average_humidity())

def too_dry_average():
    if average_humidity()>trocken:
        return 1
    else:
        return 0
    
print(too_dry_average())

def too_dry_once():
    humidity = adc_pico.read_u16()
    if humidity < feucht_genug:
        return 1
    else:
        return 0

def water_plant():
    motor.value(1)
    utime.sleep(1)
    motor.value(0)
    utime.sleep(5)
    
def watering_system():
    if too_dry_average() == 1:
        while too_dry_once():
            water_plant()

watering_system()            