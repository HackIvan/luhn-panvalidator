import time
import random

while True:
    def luhn_algorithm(digits):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digit_array = digits_of(digits)
        odd_digits = digit_array[-1::-2]
        even_digits = [sum(digits_of(d * 2)) for d in digit_array[-2::-2]]

        checksum = sum(odd_digits) + sum(even_digits)

        return checksum % 10 == 0
    card_number = input(" Please enter your 16-digit card number:   ")
    is_valid = luhn_algorithm(card_number)
    if is_valid == True:
        card_number = str(card_number)

        def insert_dash_every_4_chars(card_number):

            chunks = [card_number[i:i+4]
                      for i in range(0, len(card_number), 4)]

            result = '-'.join(chunks)

            return result

        modified_card_number = insert_dash_every_4_chars(card_number)
        print(f"VALID CARD \t{modified_card_number}")
