#static methods

class Year:
    @staticmethod
    def is_leap(year):
        """check if the year is a leap year"""
        
        if year % 4 == 0 and (year % 100!=0 or year %400 == 0):
            return True
        else:
            return False
        
year = int(input("please import the year"))

if Year.is_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
            