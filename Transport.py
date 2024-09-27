discount = {
    "Student": 0.10,
    "Regular": 0,
    "Senior": 0.25
}

class Transport:

    def __init__(self, transport: str, fare: float, gas: int):
        # Complete this method
        
        # Transport class has four attributes
        self.__type = transport
        # List of passengers
        # For example: [Student, Student, Regular]
        self.__passengers = list()

        # Fee for each passenger
        self.__fee = fare

        # Integer value
        # Each passenger consumes 1 level of gas
        self.__gas_level = gas

    # Create getters and setters for all attributes
    # vehicle type
    def get_type(self):
        return self.__type
    def set_type(self, transport: str):
        self.__type = transport

    #passenger
    def get_passengers(self):
        return self.__passengers
    def set_passengers(self, passengers: list):
        self.__passengers = passengers
    
    #gas level
    def get_gas_level(self):
        return self.__gas_level
    def set_gas_level(self, gas_level: int):
        self.__gas_level = gas_level

    
    # Then complete the following methods
    def add(self, passenger_type: str) -> None:
        """
            Adds a new passenger.
        :return:
        """
        if passenger_type in discount:
            self.__passengers.append(passenger_type)
            self.__gas_level -= 1
        else:
            print('INVALID INPUT. NOT IN DISCOUNT')

    def refuel(self) -> None:
        """
            Refuels when gas level is 0.

        :return:
        """
        if self.__gas_level == 0:
            self.__gas_level = len(self.__passengers)

    def totalFare(self) -> float:
        """
            Fare for all users combined.

        :return:
        """
        total = 0.0
        for i in range(len(self.__passengers)):
            total += self.fare(i)
        return total

    def fare(self, index: int) -> float:
        """
            Fare of a particular passenger. Fare = Transport Fee * Discount

        :param index: Passenger to calculate the fare.
        :return: Fare
        """
        passenger_type = self.__passengers[index]
        return self.__fee * (1 - discount[passenger_type])
    
    def __str__(self) -> str:
        """
            Shows a summary of every passenger (how many students, seniors, regulars, etc.), the total fare,
            and how many times it should refuel.

        :return:
        """
        summary = {
            "Student": 0,
            "Regular": 0,
            "Senior": 0
        }
        for passenger in self.__passengers:
            summary[passenger] += 1
        total_fare = self.totalFare()
        refuel_count = (len(self.__passengers) - 1) // self.__gas_level + 1 if self.__gas_level != 0 else 1
        
        return (f"Transport Type: {self.__type}\n"
                f"Passengers Summary: {summary}\n"
                f"Total Fare: {total_fare}\n"
                f"Refuel Count: {refuel_count}")