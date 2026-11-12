# a=10
# b=20
# print(a+b)
# a="Trisha"
# b="Utpal"
# print(a+b)
# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    #Operator Overloading
    def __add__(self,other):                 
        # thr=self.hr+other.hr
        # tmin=self.min+other.min
        # tsec=self.sec+other.sec
        # to=Time(thr,tmin,tsec)
        tsec=self.sec+other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr+other.hr+ehr
        return Time(thr,tmin,tsec)
    
    def __sub__(self,other):                 
        tsec=self.sec-other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min-other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr-other.hr+ehr
        return Time(thr,tmin,tsec)

    def __mul__(self,other):                 
        tsec=self.sec*other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min*other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr*other.hr+ehr
        return Time(thr,tmin,tsec)

    def __div__(self,other):                 
        emin=tsec//60
        tsec=self.sec/other.sec
        tsec=tsec%60
        tmin=self.min/other.min+emin
        ehr=tmin//60
        tmin=tmin%60
        thr=self.hr/other.hr+ehr
        return Time(thr,tmin,tsec)
    
x=Time(12,33,55)
y=Time(6,30,56)
a=x/y
print(a)
