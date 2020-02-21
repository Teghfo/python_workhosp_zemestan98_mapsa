# # list


# # my_list = [5, 'ashkan', 5.77, ['akbar', 6], ('asghaar', 5), {'name': 'ashkan'}]
# # my_list.append('asgharGholi')
# # my_list.insert(3 , 'sakineh')

# # my_list2 = my_list.copy()

# # my_list.append('Mapsa')
# # print(my_list2)
# # # my_list.clear
# # # print(my_list)

# class Khodro():
#     def __init__(self, color, charm):
#         self.color = color
#         self.charkh = 'sport'
# #         self.charm = charm

# #     def start(self):
# #         print("mashin roshan shod!")

# #     def print_color(self):
# #         print(self.color)

# # khodro1 = Khodro('blue', True)
# # khodro2 = Khodro('red', False)

# # khodro1.start()
# # khodro2.print_color()
# # print(khodro1.charm)


# # def my_fun(*arg):
# #     pass



# # Condition

# num = 501

# # if num > 5 :
# #     # num = num +1
# #     num += 1
# #     print('num bozorgtar az 5 and num={}'.format(num))
# #     # print(f'num bozorgtar az 5 and {num}')   python3.7+

# # print("end")


# # if num > 500 :
# #     # num = num +1
# #     num += 1
# #     print('num bozorgtar az 5 and num={}'.format(num))
# #     # print(f'num bozorgtar az 5 and {num}')   python3.7+
# # else:
# #     # num %= 3    baghimandeh
# #     # num **= 3    tavan resandan
# #     # num //= 3    taghsim ba kharej ghesmat
# #     print('num kamtar az 5 and numjadid={}'.format(num))

# # print("end")
# num1 = 206
# num2 = 209

# if num > 500 :
#     # num = num +1
#     num += 1
#     # print('num bozorgtar %d az 500 %d and num %d '% (num, num1 , num2))   python piremarda

#     # print('num bozorgtar {2} az 500 {1} and num {0} '.format(num, num1 , num2))
#     # print(f'num bozorgtar az 5 and {num}')   python3.7+

# elif 400<num<500:
#     # num %= 3    baghimandeh
#     # num **= 3    tavan resandan
#     # num //= 3    taghsim ba kharej ghesmat
#     print('num kamtar az 500 bishtar az 400 and numjadid={}'.format(num))

# print("end")

# my_set = {1, 2 , 'ashkan'}


# for_arg = [i for i in range(1,10)]

# for kooft in my_set:
#     print(kooft) 




# num = 1
# while 1:
#     num +=0.1
#     print(num)


# return used in function 

# def fun1(num):
#     num += 1
#     print(num)
#     if num > 10:
#         print('more than 10')
#         return 12
#     print('out of if ')
#     return 'Nokaram!'

# return_fun = fun1(10)
# print(return_fun)


#  break , continue

# my_list = ['ashkan', 'akbar', 'sakineh', 'mahmood', 'gelareh', 'gelavij']

# for name in my_list:
#     if name == 'sakineh':
#         continue

#     print(name)


def range_step_float(start, end , step):
    result = [start]
    counter = 0
    temp_step =  step - int(step)
    while temp_step < 1:
        temp_step *= 10
        counter += 1
    while start < end - step :
        start += step
        result.append(round(start, counter))
    
    return result


# for i in range_step_float(1.0,10.0,1.001):
#     print(i)
