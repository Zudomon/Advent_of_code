# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(' 1 December !')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#1December_input.txt

with open('1December_input.txt', 'r') as f:
    lines = f.read().splitlines()
    nums = tuple(map(int, lines))

#misuro quanti sono gli incrementi
tot  = sum(b > a for a, b in zip(nums, nums[1:]))
print('Part 1:', tot)

#quanti somme di incrementi sono maggiori della prima finestra di somma ?

#sum_1 = sum(nums[0],nums[1],nums[2])
sum_1 = nums[0] + nums[1] + nums[2]
print("sum_1",sum_1)

print("nums[3:]",nums[3:])

tot2 = sum(b > a for a, b in zip(nums, nums[3:])) # changed nums[1:] -> nums[3:]
print('Part 2:', tot2)