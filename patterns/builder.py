from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
import math


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_avg(self) -> None:
        pass

    @abstractmethod
    def produce_sum(self) -> None:
        pass

    @abstractmethod
    def produce_max(self) -> None:
        pass


class MetricsAnalyticsBuilder(Builder):
    _product: MetricsAnalytics

    def __init__(self, init_data: list = None) -> None:
        self._init_data = init_data
        self.reset()

    def reset(self) -> None:
        self._product = MetricsAnalytics()

    @property
    def product(self) -> MetricsAnalytics:
        product = self._product
        self.reset()
        return product

    def produce_avg(self) -> None:
        avg = sum(self._init_data) / len(self._init_data)
        self._product.add(key='avg', value=avg)

    def produce_sum(self) -> None:
        self._product.add(key='sum', value=sum(self._init_data))

    def produce_max(self) -> None:
        self._product.add(key='max', value=max(self._init_data))


class MetricsAnalytics:
    def __init__(self) -> None:
        self._report_data = {}

    def add(self, key, value: Any) -> None:
        self._report_data[key] = value

    def get_report(self) -> None:
        print(self._report_data)


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, _builder: Builder) -> None:
        self._builder = _builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_avg()

    def build_full_featured_product(self) -> None:
        self.builder.produce_avg()
        self.builder.produce_sum()
        self.builder.produce_max()


if __name__ == "__main__":
    director = Director()
    builder = MetricsAnalyticsBuilder(init_data=[1, 2, 3, 4, 5])
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.get_report()

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.get_report()

    builder.produce_sum()
    builder.produce_avg()
    builder.product.get_report()
