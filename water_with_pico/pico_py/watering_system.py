import machine
import utime

adc_pico = machine.ADC(26)
val = adc_pico.read_u16()
print(val)