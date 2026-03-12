class smartphone:
    def __init__(self, brand: str, model: int) -> None:
        self.brand = brand
        self.model = model

mobile: smartphone = smartphone(brand='oneplus', model=2021)

print(mobile)
print(mobile.brand)
print(mobile.model)

fold: smartphone = smartphone(brand='oneplus', model=2024)

print(fold)
print(fold.brand)
print(fold.model)

