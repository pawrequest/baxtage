import phonenumbers as phonenumbers



number = '07878867844'
z = phonenumbers.parse(number, 'GB')
print(z)
phonenumbers.is_possible_number(z)  # too few digits for USA
phonenumbers.is_valid_number(z)

phonenumbers.is_possible_number(z)
phonenumbers.is_valid_number(z)  # NPA 200 not used