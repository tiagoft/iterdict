
class ParameterIterator:
    def __init__(self, param_dict):
        self.param_dict = param_dict
        for key, value in self.param_dict.items():
            if not isinstance(value, list):
                self.param_dict[key] = [value]
        self.keys = list(param_dict.keys())
        self.values = list(param_dict.values())
        self.combinations = self._get_combinations()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.combinations)

    def _get_combinations(self):
        from itertools import product
        for combination in product(*self.values):
            yield dict(zip(self.keys, combination))
    