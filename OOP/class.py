class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


class OurClass:
    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAttt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.OurAtt = val

if __name__ == '__main__':
    x = A()
    print(x.pub)
    print(x._prot)
    try:
        print(x.__priv)
    except AttributeError:
        print("'A' object has no attribute '__priv'")

    print()

    y = OurClass(10)
    print(y.__OurAtt)
