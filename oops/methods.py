class laptop:

    storage_type = "ssd"

    def __init__(self, ram , storage):
        self.ram = ram
        self.storage = storage

    @classmethod   # if u not write classmethod then u can acces only by obj that is l1,l2 etc. after adding class method u can acces by class methos ie. laptop.classname().
    def get_str_type(cls):
        print(f" the storage type is {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.ram} and {self.storage} and {self.storage_type}")

l1 = laptop("16gb" , "256gb")
l2 = laptop("32gb" , "512gb")

l1.get_info()
laptop.get_str_type()
# l1.get_str_type()


#######################################################################


class laptop:

    storage_type = "ssd"

    def __init__(self, ram , storage):
        self.ram = ram
        self.storage = storage

    @classmethod   # if u not write classmethod then u can acces only by obj that is l1,l2 etc. after adding class method u can acces by class methos ie. laptop.classname().
    def get_str_type(cls):
        print(f" the storage type is {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.ram} and {self.storage} and {self.storage_type}")

    @staticmethod
    def cal_discount(price , discount):
        final_price =price - (price * discount/100)
        print(f"the final price after discount : {final_price}")

l1 = laptop("16gb" , "256gb")
l2 = laptop("32gb" , "512gb")

l1.cal_discount(40_000 , 10)
