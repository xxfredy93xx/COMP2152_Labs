"""
 Fredy Godoy Rodriguez
 Assignment1
"""

# members name
gym_member = "Alex Alliton" #string

#Preferred wight kg
preferred_weight_kg = 20.5 #float

#rep max
highest_reps = 25 #int

#active member?
membership_active = True #boolean

workout_stats={
    #string keys tupples
    "Robbie": (30, 45, 20),#int data
    "Chewy": (0, 10, 50),#int data
    "John": (30, 30, 30)#int data
}
#nesting the totals of each friend
name_total = []

#adding the workout times of each person
for name, workouts in list(workout_stats.items()):#fetching the items (workouts)
    total_minutes = sum(workouts)#Adding the workout times
    workout_stats[f"{name}_Total"] = total_minutes#nesting the name into the corresponding workout total
    name_total.append([name,total_minutes])#append meaning adding into the item

for key, value in workout_stats.items():
    print(f"{key}: {value}")

print(name_total)#printing the name and total time 

print ("combines minutes of running and yoga from all friends: ")
for name, workouts in workout_stats.items():
    if isinstance(workouts, tuple):
        print(workouts[0:2])

print ("weightlifting minutes")
friends = list(workout_stats.items())
for name, workouts in friends[-2:]:
    if isinstance(workouts, tuple):
        print(workouts[2])

print ("frineds who have worked out for 2 hours or more")
for name, value in workout_stats.items():
    if name.endswith("_Total") and value >= 120:
        friend_name = name.replace("_Total", "")
        print (f"Great job staying active, {friend_name}")

friends_name = input ("input a friends name: ")
key = friends_name + "_Total"

if key in workout_stats:
    print(f"{friends_name} has worked out for {workout_stats[key]}")
else:
    print(f"Friend {friends_name} not found in the records")
    
most_minutes = 0
top_friend = ""

print ("name of friend with the most workout")
for name, value in workout_stats.items():
    if name.endswith ("_Total"):
        if value > most_minutes:
            most_minutes  = value
            top_friend = name.replace("_Total", "")

print (f"friends with the most minutes working out is {top_friend}")

lowest_minutes = None
bottom_friend = ""

print ("Name of friend who hasnt worked out much")
for name, value in workout_stats.items():
    if name.endswith("_Total"):
        if lowest_minutes is None or value < lowest_minutes:
            lowest_minutes = value
            bottom_friend = name.replace("_Total", "")
print (f" friend with the least minutes {bottom_friend}")            
