# static methods allow access without the need to initialize a class, you'll therefore be able to execute these methods without executing an object
# They are mainly used as utility methods

class Sum:
    @staticmethod
    def getSum(*args): # name of method with arguments
        sum = 0
        for i in args:
            sum += i
        return sum

def main():
    # executing doesn't need creating an object of that type
    print("Sum: ", Sum.getSum(1, 2, 3, 8, 6))

main()
