def intToRoman(num):
    '''整数转换成罗马数字'''
    # 对应关系
    str_dict = {
      1000: 'M',
      900: 'CM',
      500: 'D',
      400: 'CD',
      100: 'C',
      90: 'XC',
      50: 'L',
      40: 'XL',
      10: 'X',
      9: 'IX',
      5: 'V',
      4: 'IV',
      1: 'I',
    }
    s = ''
    for i in str_dict:
      if num // i > 0:
        s += (num//i) * str_dict[i]
        print(s)
        num = num % i
    return s


if __name__ == '__main__':
    a = 999
    res = intToRoman(a)
    print(res)
