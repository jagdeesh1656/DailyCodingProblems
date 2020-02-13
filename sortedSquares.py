ll = [-10, -10, -5, 1, 4, 6, 9, 10, 15]

new_ll = []
neg_ll = []
for i in ll:
    if i >= 0:
        new_ll.append(i * i)
    else:
        neg_ll.append(i * i)

neg_ll = neg_ll[::-1]

final_ll = []
i = 0
j = 0

# merge step in merge sort
while i < len(new_ll) and j < len(neg_ll):

    if new_ll[i] < neg_ll[j]:
        final_ll.append(new_ll[i])
        i += 1
    else:
        final_ll.append(neg_ll[j])
        print (neg_ll[j])
        j += 1
        print (j)

while j < len(neg_ll):
    final_ll.append(neg_ll[j])
    j += 1
while i < len(new_ll):
    final_ll.append(new_ll[i])
    i += 1

print (final_ll)

