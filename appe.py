'''how to add elements in list'''


'''append method add only 1 element at a time at the end of the list'''
l1=[10,20,30,40]
l1.append(50)
print(l1)
#output [10,20,30,40,50]


l1.append(60)
print(l1)
#output [10,20,30,40,50,60]


'''insert method of the list add one element on the specific position index wise'''

l2=[50,60,70,80]
l2.insert(1,100)
print(l2)
#output [50, 100, 60, 70, 80]


list1=['monu','durga','arun','sunny']
list1.insert(2,'Rahul')
print(list1)

#output ['monu', 'durga', 'Rahul', 'arun', 'sunny']


'''extend method of the list add a sequence in list at a time'''
list2=[1,2,3,4,5]
list2.extend([10,20,30,40])
print(list2)

#output [1, 2, 3, 4, 5, 10, 20, 30, 40]

list3=[30,40,50]
list3.extend(range(20,26))
print(list3)

#output [30, 40, 50, 20, 21, 22, 23, 24, 25]








