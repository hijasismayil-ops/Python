# print sum of even and odd number in first 100?

i = 1
even_sum = 0
odd_sum = 0

while i <= 100:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1

print(even_sum,"even sum")
print(odd_sum, "odd sum")