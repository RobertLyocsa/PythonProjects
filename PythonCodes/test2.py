#helloworld = 1
#print(helloworld)

# Calculating respective numbers
#days = 792/24
#sec_in_hour = 60*60

# Displaying numbers and their types
#print("Numbers:", days, sec_in_hour)
#print("Types:", type(days), type(sec_in_hour))
#Days = 15689794 / 24
#sec_in_hour = 60*60

#print("Numbers", Days, sec_in_hour)
#print("Types", type(Days),type(sec_in_hour))

#int_num = 11
#real_sum = 16.83

#print(int_num, float(int_num))
#print(real_sum, int(real_sum))

#distance_km = 4677.4
#distance_miles = distance_km / 1.609
#print(distance_miles, int(distance_miles))

#text = "Python"
#print(text)

#course = 'Introduction to Python'
#print(course)

#referencing numbers in a string
#site = "codefinity"
#print(site[1], site[9])

#site = "codefinity"
#print(site[-1], site[-6])

#site = "codefinity"
#print(len(site))

#test = "indexing"
#print(test[-4])

#I am learing ranges of variables
#site = "codefinity"
#greeting = "How are you"

#site = "codefinity"
#print(site [0:4])

#concatenation 
#article = "The"
#country = "Slovak Republic"

#print(article + " " + country)

#greeting = "Hello"
#language = "Python"
#print(language + " " + greeting + "!")

#i want to print the last letter
#a = 'codefinity'
#print(a[len(a)-2])
#print(a[len(a)-1])

#print (1==1)
#print ("abc" == "ABC")
#print (87*731 >=98*712)

#print(0 > 10 and 5 > 2)
#print(2*2 == 5 or 1+1 != 3)

#a= 56
#if a > 60:
#  print('Passed')
#else:
#  print('Failed')

#num = 164 / 20
#print(num)

#b = 25
#if b > 200:
#  print('Very expensive')
#elif b >= 100:
#  print('Quite expensive')
#else:
#  print('Cheap')

#print(1 > 2 or 2 > 1)

#chapter 3 what is a list?

# Initial and new lists
#US_Info = ["USA", 9629091, 331002651]
#US_Info_new = ["Washington D.C.", 50]

# Add new data using concatenation
#print(US_Info + US_Info_new)

# Add new data using list method
#US_Info.extend(US_Info_new)
#print(US_Info)

#print("Hello Wolrd")

# Two-dimensional list
#countries_2d = [['USA', 9629091], ['Canada', 9984670], ['Germany', 357114]]

# Pull elements
#print(countries_2d[1])
#print(countries_2d[1][0])

#print("Hello Robbie")

#a = 1 + 1
#print(a)

#if a == 2:
#    print("sex")
#else:
#    print("you stupid nigger")

#0 Create tuple
#US_Info = ("USA", 9629091, 331002651)
#print(type(US_Info))

# Create a list 
#list_variable = [1, 2, 3]
# Convert it into a tuple
#tuple_variable = tuple(list_variable)
# Print the type of the converted variable
#print(type(tuple_variable))

#hello = [1,2,3,"USA"]
#hello2 = tuple(hello)
#print(type(hello2))

# Initial tuple
#US_Info = ("USA", 9629091, 331002651)
# New data
#US_Info_new = ("Washington D.C.", 50)
# Concatenate two tuples and save the result
#US_Info_upd = US_Info + US_Info_new
#print(US_Info_upd)

# Initial dictionary
#countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
#            'Germany': (357114, 83783942)}

# Update dictionary with two countries
#countries_dict["Brazil"] = (8515767, 212559417)
#countries_dict["India"] = (3166391, 1380004385)
#print(countries_dict)

# Initial dictionary
#people = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175)}

# Add new people to the dictionary
#people['John'] = (41,185)
#people['Michelle'] = (35,165)

# Print the dictionary
#print(people)

# Assign starting number (counter)
i = 1

# While loop will print all the numbers to 10
#while i < 10: # Condition
#  print(i, end = ' ') # Action
#  i = i + 1 # Increasing variable

# Create variable
#i = 1

# Use while loop
#while i < 10:
  # Print number i squared
 # print(i**2)
  # Increment variable i by 1
  #i = i + 1

  # Initial string
#word = 'Codefinity'

# Initialize a for loop
#for i in word:
 # print(i, end = ' ')

 # Initial list
#values = [1, [2, 3], 4, "code"]

# Initialize a for loop
#for el in values:
  #print(el, end = ' ')

  # List from previous tasks
#people = ["Alex", "Noah", "Peter", "John", "Michelle"]
# Use for loop to iterate over list
#for i in people:
 # print(i, end = ' ')

# Range with three arguments
#for i in range(10, 30, 5):
  #print(i, end = ' ')
  
# Use for loop to print numbers from 10 to 20 squared
#for i in range(10,21):
#  print(i**2)


# Initial list
#values = [1, [2, 3], 4, "code"]

# Initialize a for loop over indexes
#for i in range(len(values)):
 # print("Index:", i)
  #print("Value:", values[i])
  #print("----") # Delimiter

  #hello = "absc"
#print(len(hello))
##   hello = len(hello) + 1
  #  print(len(hello))

  # Countries data
#countries = [['USA', 9629091, 331002651],['Canada', 9984670, 37742154], ['Germany', 357114, 83783942],['Brazil', 8515767, 212559417], ['India', 3166391, 1380004385]]


# Iterate over list
#for country in countries: 
  # Iterate over nested list
 # for j in country:
  #  print(j, end = ' ')
 # print('\n') # Print new line after nested loop finish



# Initial data
#countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154],
#            ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417],
#            ["India", 3166391, 1380004385]]

# Iterating over external list
#for i in range(len(countries)):
#    if type(countries[i]) is list:
#        # Computing population density for a country
#        pop_dens = countries[i][2]/countries[i][1]
#        print(countries[i][0], pop_dens, 'people per km²')

# Data
#people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]

# Iterating over external list
#for i in range(len(people)):
#    if type(people[i]) is list:
#        # Calculate and round height in inches
#        ht_in = round(people[i][1]/2.54, 2)
#        print(people[i][0], 'is', ht_in, 'inches tall')


# Define your own function
#def my_first_function(a, b, c):
#  return ((a*3)+b*2+c)**2

# Testing the function
#print(my_first_function(5, 4, 3))

#function

# Define a function
#def is_odd(n):
#  if n % 2 == 0:
#    return "even"
#  else:
#    return "odd"

# Testing function
#print('2 is', is_odd(2))
#print('3 is', is_odd(3))

# Define a function
#def is_positive(n):
#  if n>0:
 #   return('positive')
#  elif n < 0:
#    return('negative')
#  else:
#   return('zero')

# Test your function on -5, 0 and 5
#print('Number -5 is', is_positive(-5))
#print('Number 0 is', is_positive(0))
#print('Number 5 is', is_positive(5))

# Data (i dont fully understand it)
#countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
 #                 'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
 #                 'India': (3166391, 1380004385)}

# Defining a function
#def country_information(d, name):
#  print('Country:', name)
#  print('Area:', d[name][0], 'sq km')
#  print('Population:', round(d[name][1]/1000000, 2), 'MM')

# Testing the function
#country_information(countries_dict, 'Brazil')
#country_information(countries_dict, 'Germany')

# People dictionary
#people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Define the function
#def people_information(d, name):
  #print("Name:", name)
  #print("Age:", d[name][0], "y.o.")
  #print("Height:", d[name][1], "cm")

# Testing the function
#people_information(people_d, "Alex")
#people_information(people_d, "Michelle")



# Data
#countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
#                 'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
#                  'India': (3166391, 1380004385)}

# Modify our function
#def country_information_mod(d, name):
 # if name not in d.keys():
 #   print("There is no information about", name)
 # else:
 #   print("Country:", name)
#    print("Area:", d[name][0], 'sq km')
#    print("Population:", round(d[name][1]/1000000, 2), 'mln')
        
# Testing the function
#country_information_mod(countries_dict, "USA")
#country_information_mod(countries_dict, "Ukraine")


# People dictionary
#people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Update the function
#def people_information_mod(d, name):
  #if name not in d.keys():
    # Check if name doesn't exist in the dictionary keys
   # print("There is no information about", name)
  #else:
    #print("Name:", name)
    #print("Age:", d[name][0], "y.o.")
    #print("Height:", d[name][1], "cm")

# Test your function
#people_information_mod(people_d, "Alex")
#people_information_mod(people_d, "Richard")

# Define a lambda function
#fun = lambda a, b, c: (a*3+b*2+c)**2

# Testing the function
#print(fun(1, 2, 3))
#print(fun(3, 2, 1))

# Define integer variables
#var1 = 91_400_000
#var2 = 238_855

# Print the variables
#print("The initial var1 was 91,400,000 and the corrected is:", var1)
#print("The initial var2 was 238 855 and the corrected is:", var2)

#completed = 60 // 7
#minutes = 60 % 7
# Set the number of remaining tasks
#remaining_tasks = 10 - 60//7
# Set the number of minutes you need to complete all tasks
#required_time = 10*7

# Print the result
#print("The number of remaining tasks is", remaining_tasks)
#print("The number of minutes for completing the tasks is", required_time)

# Cities population
#city_popul = {
    #'New York': 8419600,
    #'Los Angeles': 3980400,
   # 'Chicago': 2716000,
  #  'Houston': 2328000,
 #   'Phoenix': 1690000,
#    'Smalltown': 15000
#}
#min_popul = 5000000
#filtered_cities = {
#    city: population for city, population in city_popul.items() if population > min_popul
#}

#print(filtered_cities)

# Creating a set
#set_1 = {1, 5, 10, 15}
# Updating a set
#set_1.update([20, 25, 100])
# Printing the result
#print(set_1)

#set_1 = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

#print("pear" in set_1)
#print("banana" in set_1)
#print("lemon" in set_1)