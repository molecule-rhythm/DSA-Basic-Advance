class Cookie:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    def describe(self):
        return f"A {self.size} {self.flavor} cookie."


cookie_one = Cookie("chocolate chip", "large")
cookie_two = Cookie("oatmeal raisin", "medium")
print(cookie_one.describe())
print(cookie_two.describe())
