turkish_numbers = {
    "0": "sıfır",
    "1": "bir",
    "2": "iki",
    "3": "üç",
    "4": "dört",
    "5": "beş",
    "6": "altı",
    "7": "yedi",
    "8": "sekiz",
    "9": "dokuz",
    "10": "on",
    "20": "yirmi",
    "30": "otuz",
    "40": "kırk",
    "50": "elli",
    "60": "altmış",
    "70": "yetmiş",
    "80": "seksen",
    "90": "doksan"
}

def get_turkish_number(num):
    if num <= 10:
        return turkish_numbers[str(num)]
    elif num < 100:
        tens = (num // 10) * 10
        ones = num % 10
        if ones == 0:
            return turkish_numbers[str(tens)]
        else:
            return turkish_numbers[str(tens)] + " " + turkish_numbers[str(ones)]