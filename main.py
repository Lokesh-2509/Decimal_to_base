def decimal_to_base(decimal_num, base):
    if decimal_num == 0:
        return "0"
    result = ""
    while decimal_num > 0:
        remainder = decimal_num % base
        result = str(remainder) + result
        decimal_num //= base
    return result
A = int(input("Enter the decimal number: "))
B = int(input("Enter the base: "))
print(f"The equivalent number in base {B} is: {decimal_to_base(A, B)}")
