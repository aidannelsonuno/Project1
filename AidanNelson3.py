import formulas
import sys

def main():
    input_list = sys.argv[1:]
    if len(input_list) < 1:
        sys.exit("Need to provide operator")
    elif len(input_list) < 3:
        sys.exit("Need to provide at least two values")
    op_name = input_list[0].lower()
    nums = []
    for i in input_list[1:]:
        nums.append(float(i))
    if op_name == 'add':
        print(f"Answer = {formulas.add(nums):.2f}")
    elif op_name == 'subtract':
        print(f"Answer = {formulas.subtract(nums):.2f}")
    elif op_name == 'multiply':
        print(f"Answer = {formulas.multiply(nums):.2f}")
    elif op_name == 'divide':
        print(f"Answer = {formulas.divide(nums):.2f}")
    elif op_name == 'choose':
        print(f"Answer = {formulas.choose(nums):.2f}")
    else:
        print("Valid operator names (add, subtract, multiply, divide, choose)")



if __name__ == "__main__":
    main()