#Day_08<Tuples and sets >

#1.difference between list , tuple and set 

#List 
my_list =[1,2,3,2,1] #[1, 2, 3, 2, 1]
print(my_list)
my_list[0] = 10  #[10, 2, 3, 2, 1]
print(my_list)
my_list.append(5) #[10, 2, 3, 2, 1, 5]
print(my_list)

#Tuple 
my_tuple = (1,2,3,2,1)
print(my_tuple)  #(1, 2, 3, 2, 1)
#my_tuple[0] = 10 #Error :Tuples are immutable
print(my_tuple[0]) #1


#Set
my_set = {1,2,3,2,1}
print(my_set)
my_set.add(5)
print(my_set)
#my_set[0] ---Error : Sets are Unordered and unindexed

#2.Find the union and intersection of sets

a = { 1,2,3,4,5}
b = {3,4,5,6,7}
print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

""" Output
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{3, 4, 5}
{3, 4, 5} """

#3.Count the unique elements in the list using set 
l = [1,1,2,3,2,3,4,5,4,5]
unique_l = len(set(l))
print(unique_l)

""" Output 
5 """