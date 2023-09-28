user_list=input( "Enter a list of words to be sorted (separated by commas): ")
order=input( "Sort in reverse order? Yes or no: ")
user_list=user_list.split(",")
order=order.lower()

user_list.sort()
if order=="yes": user_list.sort(reverse = True)
print(user_list)
    