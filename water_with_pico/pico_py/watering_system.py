import machine
import utime

adc_pico = machine.ADC(26)
val = adc_pico.read_u16()
motor = Pin(26, Pin.OUT)
print(val)
trocken = 600
feucht_genug = 350

def average_humidity:
    average = 0;
    for x in range(8):
        average = adc_pico.read_u16()
    return average/8

def too_dry_average:
    if average_humidity()>trocken:
        return 1
    else:
        return 0
def too_dry_once:
    humidity = adc_pico.read_u16()
    if humidity < feucht_genug:
        return 1
    else:
        return 0

def water_plant:
    motor.value(1)
    utime.sleep(1)
    motor.value(0)
    utime.sleep(5)
    
def watering_system:
    if too_dry_average() == 1:
        while too_dry_once():
            water_plant()