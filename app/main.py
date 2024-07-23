class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        revenue = sum(self.calculate_washing_price(car) for car in car_list)

        for car in car_list:
            self.wash_single_car(car)

        return round(revenue, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if self.is_can_wash(car):
            return (car.comfort_class
                    * (self.clean_power - car.clean_mark)
                    * self.average_rating
                    / self.distance_from_city_center)
        else:
            return 0

    def is_can_wash(self, car: Car) -> bool:
        return self.clean_power > car.clean_mark

    def wash_single_car(self, car: Car) -> bool:
        is_can = self.is_can_wash(car)

        if is_can:
            car.clean_mark = self.clean_power

        return is_can

    def rate_service(self, unified_rating: float) -> None:
        total_ratings = self.count_of_ratings + 1
        updated_average = ((self.average_rating
                            * self.count_of_ratings
                            + unified_rating)
                           / total_ratings)
        self.average_rating = round(updated_average, 1)
        self.count_of_ratings = total_ratings
