'https://py.checkio.org/en/mission/microwave-ovens/'

'''
There is a lunch place at your work with the 3 microwave ovens (Мicrowave1, Мicrowave2, Мicrowave3), 
which are the subclasses of the MicrowaveBase class. Every microwave can be controlled by a RemoteControl. The RemoteControl uses the next commands:

set_time ("xx:xx"), where "xx:xx" - time in minutes and seconds, which shows how long the food will be warming up. For example: set_time("05:30");
add_time ("Ns"), add_time ("Nm"), where N - the number of seconds("s") or minutes("m"), which should be added to the current time;
del_time ("Ns"), del_time ("Nm"), where N - the amount of the seconds("s") or minutes("m"), which should be subtracted from the current time;
show_time() - shows the current time for the microwave.
'''

class MicrowaveBase:
    pass

class Microwave1(MicrowaveBase):
    pass

class Microwave2(MicrowaveBase):
    pass

class Microwave3(MicrowaveBase):
    pass

class RemoteControl:
    pass



# Best Solution:
# https://py.checkio.org/mission/microwave-ovens/publications/David_Jones/python-3/f-strings/share/d73770a8fd99a4080a8daac31b09d4e9/

class MicrowaveBase:
    def __init__(self):
        self.seconds = 0


class Microwave1(MicrowaveBase):
    pass


class Microwave2(MicrowaveBase):
    pass


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave
    
    def set_time(self, time):
        mm, ss = map(int, time.split(':'))
        self.microwave.seconds = 60 * mm + ss
    
    def add_time(self, time):
        seconds, token = int(time[:-1]), time[-1]
        if token == 'm':
            seconds *= 60
        self.microwave.seconds = min(5400, self.microwave.seconds + seconds)
    
    def del_time(self, time):
        seconds, token = int(time[:-1]), time[-1]
        if token == 'm':
            seconds *= 60
        self.microwave.seconds = max(0, self.microwave.seconds - seconds)
    
    def show_time(self):
        mm, ss = divmod(self.microwave.seconds, 60)
        time = f'{mm:02d}:{ss:02d}'
        if isinstance(self.microwave, Microwave1):
            return '_' + time[1:]
        if isinstance(self.microwave, Microwave2):
            return time[:-1] + '_'
        return time



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")
    
    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")
    
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")