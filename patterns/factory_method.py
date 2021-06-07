from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self, data):
        pass


class BusCreator(Creator):
    def factory_method(self, data):
        return BusTransport()


class RoadCreator(Creator):
    def factory_method(self, data):
        if data['weight'] >= 100:
            return BusTransport()

        return CarTransport()


class TrainCreator(Creator):
    def factory_method(self, data):
        return TrainTransport()


class Transport(ABC):
    @abstractmethod
    def delivery(self):
        pass


class BusTransport(Transport):
    def delivery(self):
        print('Bus Product')


class CarTransport(Transport):
    def delivery(self):
        print('Car Product')


class TrainTransport(Transport):
    def delivery(self):
        print('Train Product')


def get_delivery_product(creator: Creator, data):
    return creator.factory_method(data)


if __name__ == '__main__':
    train = get_delivery_product(TrainCreator(), {})
    bus = get_delivery_product(RoadCreator(), {'weight': 120})
    car = get_delivery_product(RoadCreator(), {'weight': 20})

    car.delivery()
    bus.delivery()
    train.delivery()
