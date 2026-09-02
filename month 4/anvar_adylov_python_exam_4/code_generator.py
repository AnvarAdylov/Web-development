import hashlib
from abc import abstractmethod


class CodeGenerator:
    def make_code(input_str):
        try:
            md = hashlib.md5()
            md.update(input_str.encode())
            return CodeGenerator.convert_to_string(md.digest())

        except Exception as e:
            print(e)
            return ""

    def convert_to_string(array):
        return ''.join(format(i, '02x') for i in array)

    def generate(self, product):
        if 500 > product.price > 0:
            return Cheap.generate(self, product)
        elif 1000 > product.price > 500:
            return Mid.generate(self, product)
        elif product.price > 1000:
            return Expensive.generate(self, product)


class Strategy:
    @abstractmethod
    def generate(self):
        pass


class Expensive(Strategy):
    def generate(self, product):
        return CodeGenerator.make_code("Gold-" + product.id)


class Mid(Strategy):
    def generate(self, product):
        return CodeGenerator.make_code("Silver-" + product.id)


class Cheap(Strategy):
    def generate(self, product):
        return CodeGenerator.make_code("Bronze-" + product.id)
