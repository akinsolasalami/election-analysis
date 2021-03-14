# print("Hello World")
# countries_tuple = ("Arapahoe", "Denver", "Jefferson")
# print(len(countries_tuple))
# print(countries_tuple[:2])


# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
# voting_data.pop(0)
# voting_data.pop(1)
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

# print(voting_data)


# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")


# IF, IF-ELSE, IF-ELIF-ELSE

# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')


# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# MEMEBERSHIP OPERATORS

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# # 3 logical operators and, or, not

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")


# # Loops 
# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for  num in numbers:
#     print (num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)


                                            #will print the values only 
# for county in counties_dict.values():
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))


                                            #will print key value pairs

# for key, value in dictionary_name.items():
#     print(key, value)

# for county, voters in counties_dict.items():
#     print(f' {county} county has {voters} registered voters')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len((voting_data))):
#     print(voting_data[i])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])


#Using f'string to print over dictionary keys and values 
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
                        #floating variables 
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# rock paper scissor with math?

#Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")