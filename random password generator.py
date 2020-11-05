import random
import string
from collections import Counter


letters = [letter for letter in string.ascii_lowercase]

numbers = [number for number in string.digits]

specialCharacters = [sign for sign in string.punctuation]

passwordLength = random.randint(9, 12)
password = str()
upper_letter_counter = 0
lower_letter_counter = 0
number_counter = 0
special_sign_counter = 0
signProbability = {"letters": 0.5,
                   "numbers": 0.3,
                   "specialCharacters": 0.2}

signList = tuple(signProbability.keys())
signRates = tuple(signProbability.values())
signTypes = list()

while (upper_letter_counter == 0) or (lower_letter_counter == 0) or (number_counter == 0) or (special_sign_counter == 0):
    password = ""
    for sign in range(passwordLength):
        sign = random.choices(signList, signRates)[0]
        signTypes.append(sign)
        if (sign == "letters"):
            letter = random.choices(letters)[0]
            randomizer = random.randint(0, 1)
            if (randomizer % 2 == 0):
                letter = letter.upper()
                password += letter
                upper_letter_counter += 1
            else:
                password += letter
                lower_letter_counter += 1
        if (sign == "numbers"):
            number = random.choices(numbers)[0]
            password += number
            number_counter += 1
        if (sign == "specialCharacters"):
            char = random.choices(specialCharacters)[0]
            password += char
            special_sign_counter += 1

TypeDict = Counter(signTypes)  # for debugging purposes

print(password)
