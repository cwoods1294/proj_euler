previous_term = 1
next_term = 2
total = 0
while True:
    if next_term < 4000000:
        if next_term%2 == 0:
            total += next_term
        hold = next_term
        next_term = next_term + previous_term 
        previous_term = hold
    else:
        break
print(total)