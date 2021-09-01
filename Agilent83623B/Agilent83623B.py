"""package for Agilent 83623B"""


import time
import pyvisa


__author__ = "Yuta Kawai <pygo3xmdy11u@gmail.com>"
__status__ = "production"
__version__ = "0.0.0"
__date__ = "2021/09/01"


class Agilent83623B:
    def __init__(self, gpib_address):
        """establishe communication with the Agilent 83623B

        Parameters
        ----------
        gpib_address : int
            GPIB address of the Agilent 83623B
        """
        self.gpib_address = gpib_address
        self.instrument = None
        self.time_interval = 0.5
        self.time_out = 1.0
        self.connect(gpib_address=gpib_address)

    def __del__(self):
        """close communication with the Agilent 83623B if the program shutdown 
        suddenly by error
        """
        self.close()

    def set_time_interval(self, time_interval):
        """set time interval

        Parameters
        ----------
        time_interval : float
            time interval of command
        """
        self.time_interval = time_interval

    def get_time_interval(self):
        """get time interval

        Returns
        -------
        float
            time interval of command
        """
        return self.time_interval

    def set_time_out(self, time_out):
        """set time out

        Parameters
        ----------
        time_out : float
            The time taken to forcibly terminate a process or data transfer in the 
            middle when it is taking too long.
        """
        self.time_out = time_out

    def get_time_out(self):
        """get time out

        Returns
        -------
        float
            The time taken to forcibly terminate a process or data transfer in the 
            middle when it is taking too long.
        """
        return self.time_out

    def connect(self, gpib_address):
        """establishe communication with the Agilent 83623B

        Parameters
        ----------
        gpib_address : int
            GPIB address of the Agilent 83623B
        """
        if gpib_address != self.gpib_address:
            if self.instrument != None:
                self.close()
            self.gpib_address = gpib_address
        if self.instrument == None:
            rm = pyvisa.ResourceManager()
            self.instrument = rm.open_resource(
                "GPIB0::{}::INSTR".format(self.gpib_address)
            )
            time.sleep(self.time_interval)

    def close(self):
        """close communication with the Agilent 83623B"""
        if self.instrument != None:
            self.instrument.close()
            self.instrument = None

    def write_command(self, command):
        """write command to the Agilent83623B

        Parameters
        ----------
        command : str
            command sent to Agilent 83623B
        """
        time.sleep(self.time_interval)
        self.instrument.write(command)
        time.sleep(self.time_interval)

    def read_command(self, command):
        """read command to the Agilent83623B

        Parameters
        ----------
        command : str
            command sent to Agilent 83623B

        Returns
        -------
        str
            string returned from Agilent 83623B
        """
        time.sleep(self.time_interval)
        response = self.instrument.read(command)
        time.sleep(self.time_interval)
        return response

    def query_command(self, command):
        """query command to the Agilent83623B

        Parameters
        ----------
        command : str
            command sent to Agilent 83623B

        Returns
        -------
        str
            string returned from Agilent 83623B
        """
        time.sleep(self.time_interval)
        response = self.instrument.query(command)
        time.sleep(self.time_interval)
        return response

    def on(self):
        """set output state ON"""
        command = "OUTPut:STATe ON"
        self.write_command(command)

    def off(self):
        """set output state OFF"""
        command = "OUTPut:STATe OFF"
        self.write_command(command)

    def set_frequency_mode(self, frequency_mode):
        """set frequency mode of 83623B
        
        Parameters
        ----------
        frequency_mode : str
            frequency mode of 83623B
        """
        command = "FREQuency:MODE {}".format(frequency_mode)
        self.write_command(command)

    def get_frequency_mode(self):
        """get frequency mode of 83623B
        
        Returns
        -------
        str
            frequency mode of 83623B
        """
        command = "FREQuency:MODE?"
        return self.query_command(command)

    def set_frequency(self, frequency):
        """set frequency of 83623B
        
        Parameters
        ----------
        frequency : float
            frequency of 83623B
        """
        command = "FREQuency:CW {} Hz".format(int(round(frequency)))
        self.write_command(command)

    def get_frequency(self):
        """get frequency of 83623B
        
        Returns
        -------
        float
            frequency of 83623B
        """
        command = "FREQuency:CW?"
        return float(self.query_command(command))

    def set_power_level(self, power_level):
        """set power level of 83623B
        
        Parameters
        ----------
        power_level : float
            power level of 83623B
        """
        command = "POWer:LEVel {} dBm".format(power_level)
        self.write_command(command)

    def get_power_level(self):
        """get power level of 83623B
        
        Returns
        -------
        float
            power level of 83623B
        """
        command = "POWer:LEVel?"
        return float(self.query_command(command))
