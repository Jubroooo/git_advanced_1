from typing import List

#Skeleton code for even_list
def even_list(int_list:List[int]) -> List[int]:
    even_numbers = []
    for number in int_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

#Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(int_list:List[int]) -> List[int]:
    sum = 0  
    for number in int_list:
        sum += number ** 2
    return sum    

#Main function
def main():
    #Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_list_list = even_list(int_list)
    output = sum_of_squares_of_even(even_list_list)
    print(output)
    
#Boilerplate code
if __name__=="__main__":
    main()