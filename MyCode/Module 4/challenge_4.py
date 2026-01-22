class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population
    
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Capital: {self.capital}")
        print(f"Population: {self.population}")


class DevelopedCountry(Country):
    def __init__(self, name, capital, population, gdp):
        super().__init__(name, capital, population)
        self.gdp = gdp

    def get_info(self):
        super().get_info()
        print(f"GDP: {self.gdp}")


class DevelopingCountry(Country):
    def __init__(self, name, capital, population, hdi):
        super().__init__(name, capital, population)
        self.hdi = hdi

    def get_info(self):
        super().get_info()
        print(f"HDI: {self.hdi}")


class World:
    countries = []

    def add_country(self, country):
        self.countries.append(country)
    
    def get_country_info(self, name):
        for country in self.countries:
            if country.name == name:
                country.get_info()


world = World()
# 
usa = DevelopedCountry("United States", "Washington, D.C.", 331000000, 22512000)
india = DevelopingCountry("India", "New Delhi", 1380004385, 0.645)
china = DevelopingCountry("China", "Beijing", 1444216107, 0.758)

world.add_country(usa)
world.add_country(india)
world.add_country(china)
# 
world.get_country_info('China')
