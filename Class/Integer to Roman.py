class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        # Mapping of Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ""
        i = 0
        num = self.number
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num


# Example usage:
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    converter = IntegerToRoman(number)
    print("Roman numeral:", converter.convert())
