from Header import *


class Sequencer:
    __seed = 0

    @classmethod
    def reset_seed(cls, new_seed):
        assert new_seed >= 0, 'Seed must be > 0'
        cls.__seed = new_seed

    @classmethod
    def get_gen(cls):
        return np.random.default_rng(cls.__seed)


class IntegerRandom:

    def __init__(self, min_value, max_value):
        assert min_value <= max_value, 'Bad boundaries'
        self.min_value = min_value
        self.max_value = max_value
        self.generator = Sequencer.get_gen()

    def __call__(self):
        return self.generator.integers(self.min_value, self.max_value + 1)


class SignRandom:

    def __init__(self):
        self.generator = Sequencer.get_gen()

    def __call__(self):
        return 1 if self.generator.integers(0, 2) else -1


class Generator:
    __steps_until_break = 10**4

    @classmethod
    def get_steps_until_break(cls):
        return cls.__steps_until_break

    @classmethod
    def reset_steps_until_break(cls, new_steps_until_break_value):
        assert new_steps_until_break_value > 0, 'Steps until break must be positive'
        cls.__steps_until_break = new_steps_until_break_value

    def __init__(self, generator):
        assert callable(generator), 'Generator is not callable'
        self.generator = generator
        self.steps_until_break = Generator.__steps_until_break

    def __call__(self):
        return self.generator()

    def Filter(self, predicate):
        assert callable(predicate), 'Predicate is not a function'
        assert len(
            signature(predicate).parameters) == 1, 'Predicate has too many arguments'
        assert isinstance(predicate(0), bool), 'Predicate does not return bool'

        class FilteredGenerator:
            def __init__(self, generator, predicate, steps_until_break):
                assert callable(generator), 'Generator is not callable'
                assert callable(predicate), 'Predicate is not a function'
                assert len(
                    signature(predicate).parameters) == 1, 'Predicate has too many arguments'
                assert isinstance(
                    predicate(0), bool), 'Predicate does not return bool'

                self.generator = generator
                self.predicate = predicate
                self.steps_until_break = steps_until_break

            def __call__(self):
                result = self.generator()
                count = 0
                while not predicate(result):
                    result = self.generator()
                    count += 1
                    assert count < self.steps_until_break, 'Time exceeded. Please change predicate or reset seed'
                return result

        self.generator = FilteredGenerator(
            self.generator, predicate, self.steps_until_break)
        return self

    def BanZero(self):
        self.Filter(lambda x: x != 0)
        return self

    def Extend(self, values, length):
        assert length >= 0, 'Length can not be negative'
        assert len(values) <= length, 'Too small length'
        count = 0
        while len(values) != length:
            value = self()
            if not value in values:
                values.append(value)
            count += 1
            assert count < self.steps_until_break, 'Time exceeded. Please change predicate or reset seed'

        return values

    def Sequence(self, length):
        assert length >= 0, "Length can not be negative"
        return self.Extend([], length)


def Random(min_value, max_value):
    return Generator(IntegerRandom(min_value, max_value))
