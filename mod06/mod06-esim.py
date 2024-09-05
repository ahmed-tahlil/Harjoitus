# funktio-esimerkkejä
'''
def do_something():
    print("Doing ")
    print("Something")
    return "tässä on palautettava arvo, voi olla ihan minkä tyyppinen vaan"

return_value = do_something()
print(return_value)
'''
'''
#funktio, jolla parametreja (argumentteja)
def combine_strings(string1, string2):
    combination = f"{string1}, {string2}"
    #print(combination)
    return combination

print(combine_strings("auto", "ajaa"))
combination = combine_strings("kuski", "jarruttaa")
combination = combine_strings(combination, "nopeasti")
print(combination)'''


# yksinkertainen laskin, jolle voi antaa tasan 3 parametria
#listat ja funktiot
''''
def calculate_sum(numbers):
    print(numbers)
    total_sum = 0
    for i in range(len(numbers)):

        total_sum = total_sum + numbers[i]
    #for number in numbers:
  #      total_sum = total_sum + number
    return total_sum

nums =  [3, 4, 5]
print(nums)
print(calculate_sum(nums))
'''
#print(calculate_sum([3, 4, 5, 10]))

#vaihtuva määrä parametreja
# * tekee kaikista syötetyistä parametreista (arvoista) listan
# ja sijoittaa listan numbers-muuttujaan
def calculate_sum2(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2(2,3,8, -10, 4.67))


