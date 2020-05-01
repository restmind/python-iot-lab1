import datetime

class PromotionalProduct:
    duration_of_promotion_to = datetime.datetime(2121, 12, 12)

    def __init__(self, name_of_good = "Laptop", percent_of_discount = "20%", starting_price = 2000.00,
                 promotional_price = 1600.00, weight_of_goods_in_kg = 2.00,
                 type_of_goods = "Technique", food_stuff = False):
        self._name_of_good = name_of_good
        self._percent_of_discount = percent_of_discount
        self._starting_price = starting_price
        self._promotional_price = promotional_price
        self._weight_of_goods_in_kg = weight_of_goods_in_kg
        self._type_of_goods = type_of_goods
        self._food_stuff = food_stuff

    def __del__(self):
        print("Good " + self._name_of_good + " was successfully deleted!")

    def __str__(self):
        return "Name of good: {}\n" \
               "Percent of discount: {}\n" \
               "Starting price: {}\n" \
               "Promotional price: {}\n" \
               "Weight of goods in kg: {}\n" \
               "Type of goods: {}\n" \
               "Food stuff: {}\n".format(self._name_of_good, self._percent_of_discount, self._starting_price,
                         self._promotional_price, self._weight_of_goods_in_kg, self._type_of_goods,
                         self._food_stuff)

    @staticmethod
    def get_duration_of_promotion_to():
        return PromotionalProduct.duration_of_promotion_to


    @staticmethod
    def main():
        apple = PromotionalProduct("Apple", "10%", 20.00, 15.00, 1.00, "Food", True)
        toilet_paper = PromotionalProduct("Toilet papper", "20%", 8.00)
        laptop = PromotionalProduct()
        goods = [apple, toilet_paper, laptop]
        for good in goods:
            print(good)