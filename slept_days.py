#This program tells you ,how many days,infact years you have slept
class slept():
    """
    A person sleeps 7hrs a day on an average i.e.,
    7hrs in 24hrs.
    A year have 365 days i.e.,365*24 hrs
    but a leap year consists of 366 days
    """
    def __init__(self,age):
        self.total_hrs = 7*int(age)
        years = int(self.total_hrs) / 24
        print("You have slept {:.3f} years!".format(years))
def main():
    ag = input("What is your age?\n")
    you = slept(ag)
if __name__=="__main__":
    main()
