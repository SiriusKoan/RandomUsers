import abc
import csv
from typing import Dict
from .Exceptions import CsvAndInstanceError


class Model(abc.ABC):
    """
    Basic person class.
    """

    @abc.abstractmethod
    def get_available(self):
        return NotImplementedError

    @abc.abstractmethod
    def generate(self):
        return NotImplementedError

    @abc.abstractmethod
    def bulk_generate(self, n, csv_file):
        return NotImplementedError


class Instance(object):
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)


class BasicModel(Model):
    def __init__(
        self,
        information: dict() = None,
        instance=None,
        **kwargs,
    ) -> None:
        """
        :param information: other user information, such as `{"is_admin": True}`
        :param instance: a container that contain the fields data. The function will return a dict if instance is not given.
        :param kwargs: fields which is dynamic
        """
        self.instance = instance
        self.information = information
        self.fields = kwargs

    def get_available(self) -> list:
        """
        Return all available fields of the data model.

        :return: <list>
        """
        return [key for key in list(self.fields.keys())]

    def write_csv(self, data, csv_file) -> None:
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.get_available())
            for d in data:
                writer.writerow(list(d.values()))

    def generate(self):
        """
        Generate random data object.
        You can access to the user data by using its attributes.
        """
        info = dict()
        for key, field in self.fields.items():
            info[key] = field.generate()
        if self.information:
            for key, value in self.information.items():
                info[key] = value
        if self.instance:
            return self.instance(**info.copy())
        else:
            return info.copy()

    def bulk_generate(self, n=100, csv_file=False):
        """
        Generate as many random data as you want.
        """
        if csv_file and self.instance:
            raise CsvAndInstanceError
        data = []
        for _ in range(n):
            data.append(self.generate())
        if csv_file:
            self.write_csv(data, csv_file)
        return data

    def ordered_generate(
        self,
        n: range = range(1, 101),
        ordered_fields: dict[str, str] = None,
        csv_file=False,
    ):
        """
        Generate data in a specific order of numbers.
        """
        if csv_file and self.instance:
            raise CsvAndInstanceError

        info = dict()
        data = []
        fields = self.fields.copy()
        for key in ordered_fields.keys():
            fields.pop(key, None)
        for i in n:
            for attr, prefix in ordered_fields.items():
                info[attr] = prefix + str(i)
            for key, field in fields.items():
                info[key] = field.generate()
            if self.information:
                for key, value in self.information.items():
                    info[key] = value
            if self.instance:
                data.append(self.instance(**info))
            else:
                data.append(info.copy())

        if csv_file:
            self.write_csv(data, csv_file)
        return data
