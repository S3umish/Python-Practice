from countryinfo import CountryInfo

# name = "India"
name2 = "Spain"

# country = CountryInfo(name)
country = CountryInfo(name2)

# data1 = country.alt_spellings()
# print(data1)

# data2 = country.capital()
# print(data2)

# data3 = country.currencies()
# print(data3)

# data4 = country.languages()
# print(data4)

# data5 = country.area()
# print(data5)

# data6 = country.calling_codes()
# print(data6)

# data7 = country.borders()
# print(data7)

# data8 = country.wiki()
# print(data8)

# data9 = country.timezones()
# print(data9)

data10 = country.info()
for x,y in data10.items():
    print(f'{x} --> {y}')