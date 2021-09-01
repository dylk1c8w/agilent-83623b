import time
from Agilent83623B.Agilent83623B import Agilent83623B

frequency = 9.6e9  # 9.6 GHz
power_level = -30.0  # -30 dBm
gpib_address = "19"  # GPIB address of Agilent 83623B
agilent_83623B = Agilent83623B(
    gpib_address=gpib_address
)  # # establishe communication with the Agilent 83623B
agilent_83623B.set_frequency_mode("CW")  # set frequency mode
agilent_83623B.set_frequency(frequency)  # set frequency
agilent_83623B.set_power_level(power_level)  # set power level
agilent_83623B.on()  # set output status ON
time.sleep(5.0)  # wait 5 seconds
agilent_83623B.off()  # set output status OFF
frequency = agilent_83623B.get_frequency()  # get the set frequency
power_level = agilent_83623B.get_power_level()  # get the set power level
agilent_83623B.close()  # close communication with the Agilent 83623B
del agilent_83623B
