# print("_________________________________________________________________________________________________________________________________________________________")
# print("-----------------------------------------------------------------!! OM GANESHAYE NAMAH !! ------------------------------PYTHON ")
# print("__________________________________________________________________________________________________________________________________________________________")


# # 1. -------------------------------------------------------------------LIST -------------------------------------------
# # List: Ordered, mutable, allows duplicate elements, heterogeneous.
# # Common methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
# # Types: Can contain any data type (int, str, float, list, etc.)
# # Example: a = [1, 2, "hello", True]

# # a = [1, 3, 4, "name", True, print()]  # heterogenus nature
# # print(a[3::])  # :: this means from were , nd two were . 0:: , :: , ::3 slicing


# #  list traversing and methods

# # 1st way - using index '
# # a = [13, 25, 85, 3, 67, 39, 74, 75]
# # for i in range(len(a)):
# #     print(i)  # return only index
# #     print(a[i])  # return values of index

# # # 2nd way - directly on  value
# # for i in a:  # print all  the values of the index direclty wihout accesing the index
# #     print(i)

# # help(list)

# a = [13, 25, 85, 3, 67, 39, 74, 75, -3, -6, -7]

# for i in a:

#     if i <= 0:
#         print(i)

# for i in a:
#     if i >= 0:
#         print(i)

#  find mean
# l = [12, 4, 56, 78, 100]
# temp = l[0]
# Index = 0
# for i in range(len(l)):
#     if l[i] > temp:
#         temp = l[i]
#         Index = i
# # # came out form the loop
# # print(f"largest vaue is {temp} at th index of {i}")

# #  check list is sorted or not

# # Q. l = [12, 3, 45, 47, 89]
# # l=[1,2,3,4,5,6,7,8,9]

# # for i in range(len(l)-1):
# #     if l[i] < l[i+1]:
# #         continue
# #     else:
# #         print("not sorted ")
# #         break
# # else:
# #     print("sorted ")

# # ________________________________________________--------------------------______TUPLE_________________________________
# # Tuple: Ordered, immutable, allows duplicate elements, heterogeneous.
# # Common methods: count(), index()
# # Types: Can contain any data type (int, str, float, list, etc.)
# # Example: t = (1, 2, "hello", True)

# # immutable
# # a,b,c,d=(1,2,3,4) # a=1,b=2,c=3,d=4

# __________________________________________________------------------------------------------------____set___________________________________
# Set: Unordered, mutable, does not allow duplicate elements, heterogeneous.
# Common methods: add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference()
# Types: Can contain any immutable data type (int, str, float, tuple, etc.)
# Example: s = {1, 2, 3, "hello"}
# a = {1, 4, 3, 4, 5, 6, 7, }
# b = {3, 4, 5, 7, 4, 7}
# s = a.union(b)
# s=a|b # shordt form of uniun'

# s=a.intersection(b)
# s=a&b short form of intersection

# s=a.difference(b)
# s=a-b short form of diffrence

# s=a.symmetric_difference(b)
# s=a^b
# print(s)


# # Dictionary = in simple words this is the hashmap - it contain data in the form of keys and values
# # mutable
# # duplicates - key will unique but the value can be duplicates
# # order
# # heterogeneous
# # d = {1: "one", 2: "two"}
# # print(d)  # outpu v{1: 'one', 2: 'two'}

# # updating values
# d[2] = "updated two"
# print(d[2])  # output  "updated two"

# # create value
# d[3] = "cretd three"
# # print(d) #{1: 'one', 2: 'updated two', 3: 'cretd three'}

# # delete value
# del d[3]
# print(d) #{1: 'one', 2: 'updated two'}
# names = {
#     1: "Aarav",
#     2: "Priya",
#     3: "Kabir",
#     4: "Isha",
#     5: "Rohan",
#     6: "Meera",
#     7: "Yash",
#     8: "Simran",
#     9: "Dev",
#     10: "Ananya"
# }
# # for i in names:
# #     # print(names[i]) # itrate over the keys
# # for i in names.values():
# #     print(i)


# # d1={1:1,2:2,3:3}
# # sum =0
# # for i in d1:
# #     sum=sum+d1[i]
# # print(sum)

# # print the frequency of nubers appear in the list
# # a = [1, 3, 5, 3, 2, 5, 7, 8, 7, 6, 5, 4, 2, 1, 3, 4, 5, 6, 8, 9, 9, 9]
# # d = {}
# # for i in a:
# #     if i in d.keys():
# #         d[i] += 1
# #     else:
# #         d[i] = 1

# # print(d)

# # combining two dictionary
# # Dictionary 1: keys and values from 1 to 10

# d1 = {1: 1, 2: 2, 3: 3}
# d2 = {1: 1, 2: 2, 3: 3}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)