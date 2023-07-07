def int_str(num):
    """Takes an integer under 1015 and returns the name of the integer in English"""
    num_str = ''
    dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
             60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
             16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    if num >= 1000:
        num_str += 'a thousand '

    digit = num // 100 % 10
    if digit != 0 and digit != 1:
        num_str += dict1[digit] + ' '
    elif digit == 1:
        num_str += 'a '
    if digit != 0:
        num_str += 'hundred and '

    digit = num // 10 % 10 * 10
    if digit != 0 and digit != 10:
        num_str += dict1[digit] + ' '
    elif digit == 10:
        num_str += dict1[num % 100] + ' '
    elif digit == 0 and num % 10 != 0:
        num_str += dict1[num % 10] + ' '

    if digit != 0 and digit != 10:
        digit = num % 10
        num_str += dict1[digit]

    return num_str


numbers = [1022, 654, 18, 98, 564, 105]
for i in numbers:
    print(int_str(i))

