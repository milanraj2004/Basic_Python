class Country:
    origin = "India"

print(Country.origin)  # Output: India

Country.is_developed = False

print(Country.is_developed)  # Output: False


#creating objects from Class Country 

country1 = Country()
print(country1.origin)  # Output: India

print(country1.is_developed)  # Output: False

Country.isdeveloped = True
print(Country.isdeveloped)  # Output: True

print(country1.isdeveloped)  # Output: True

country2 = Country()
print(country2.isdeveloped)  # Output: True

Country.flag = "Tricolor"
print(Country1.flag)  # Output: Tricolor