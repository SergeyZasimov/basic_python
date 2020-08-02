class Date:
    def __init__(self, date):
        self.date = date
        Date.date = date
        print(Date.validator())

    @classmethod
    def separator(cls):
        day, month, year = map(int, cls.date.split('-'))
        return day, month, year
    
    @staticmethod
    def validator():
        monthes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day, month, year = Date.separator()
        if month in range(1, 13) and day in range(1, monthes[month] + 1) and len(str(year)) == 4:
            return 'Правильная дата'
        else: return 'Неверный формат'

if __name__ == "__main__":
    date = Date('01-01-2001')
    print(date.date)
    date2 = Date('13-14-2025')
    date3 = Date('01-02-20')