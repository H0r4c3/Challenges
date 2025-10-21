'https://py.checkio.org/en/mission/calculator-v/'
'https://py.checkio.org/mission/calculator-v/publications/o.kovalev/python-3/calculator-5/?ordering=most_voted&filtering=all'

class Calc:
    def __init__(self,maxrange):
        self.maxrange=maxrange
        self.display = "0"
        self.num = True
        self.oper = "="
        self.current = ""
        self.m=""
        self.last=""
        self.error=False

    def remove_last_zero(self,display):
        if len(display)>2 and display[-2:]==".0":
            display=display[:-1]
        return display

    def show_display(self):

        if len(str(self.m)) > self.maxrange:
            if len(str(int(self.m))) < self.maxrange:
                self.m = round(self.m, self.maxrange - len(str(int(self.m))) - 1)
                self.display=self.remove_last_zero(str(self.m))
                if len(self.display) > self.maxrange:
                    self.error = True
                    self.display = "error"
            else:
                self.error = True
                self.display = "error"
        else:
            self.display = self.remove_last_zero(str(self.m))



def calculator(log: str) -> str:
    calc=Calc(5)
    for i in log:
        if i.isdigit() or i == ".":
            if calc.display == "0" or not calc.num :
                calc.display = ""
            if len(calc.display)<calc.maxrange:
                calc.display += i
            calc.num = True
        elif i in "+-*/%=":
            if calc.oper == "=" and calc.current not in "+-=":
                calc.m = eval(calc.display)
            elif calc.current+i == "+=":
                calc.last = calc.oper + calc.display
                calc.m *=2
            elif calc.current+i == "-=":
                calc.last = "-"+str(calc.m)
                calc.m -= calc.m
            elif calc.current+i == "*=":
                calc.last = calc.oper + calc.display
                calc.m *=calc.m
            elif calc.current+i == "/=":
                calc.last = calc.oper + calc.display
                calc.m /= calc.m
            elif calc.current + i == "==":
                calc.m =eval(str(calc.m)+calc.last)
            elif calc.oper == "=":
                calc.m = eval(calc.display)
            elif calc.num and not calc.error:
                calc.last = calc.oper + calc.display
                calc.m = eval(str(calc.m) + calc.last)
            elif calc.error:
                calc.display="error"

            if (calc.oper == "/" and i == "/") or (calc.oper == "*" and i == "*"):
                calc.oper += i
            else:
                calc.oper = i

            calc.num = False

            calc.show_display()

        calc.current=i

    return calc.display

print("Example:")
print(calculator("10//2="))

# These "asserts" are used for self-checking
assert calculator("10/2*2=") == "10."
assert calculator("10/=*=-=") == "0."
assert calculator("100//33**3=") == "27"
assert calculator("10%10=") == "0"
assert calculator("---+++100//3//3+++---") == "11"
assert calculator("27**.3333=") == "3."
assert calculator("0001.1000") == "1.100"
assert calculator("0001.1000-") == "1.1"
assert calculator("999.9999999+=") == "2000."
assert calculator("1.000123") == "1.000"
assert calculator("9999.9999999+=") == "error"
assert calculator("90000+10000=") == "error"
assert calculator("90000+10000-10000=") == "error"
assert calculator("90000+10000-10000") == "10000"
assert calculator("123456789") == "12345"
assert calculator("123456789+5=") == "12350"
assert calculator("5+123456789") == "12345"
assert calculator("50000+=") == "error"
assert calculator("3+=") == "6"
assert calculator("3+2==") == "7"
assert calculator("4-1==") == "2"
assert calculator("3+-2=") == "1"
assert calculator("-=-+3-++--+-2=-") == "1"
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")
