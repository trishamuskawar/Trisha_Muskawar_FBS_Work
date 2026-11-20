def decore(x):
    print("Inside decore function")
    def innerFun():
        print("Logger Added")
        print("Time Started")
        x()
    