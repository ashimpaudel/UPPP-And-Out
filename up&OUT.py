#This will be the list of events we will show
List_Of_Events = ['Culture', 'Nightlife', 'Food', 'Random']
#This will be the list of places, it will be dynamic : it will find out based on the location
places = [ 'U-Street', 'Dupont Circle', 'Capitol', 'Washington Monument', 'Smithsonian-Library', 'Dharahara', 'Kathmandu', 'Nepal']
random = ['The RenWick Art Gallery']
#this will be the list of times
times = ['1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM', '11:00 PM', '12:00 PM', '1:00 AM', '2:00 AM', '3:00 AM']


My_Dictionary = {}
def my_program():
    print 'type your name'
    user_name = raw_input()
    print "Here are the list of events one by one"
    user_data = []
    events_list = []
    place_list = []
    time_list = []

    
    for event in List_Of_Events:
        print event
        print "press 'y' if you like it 'n' if you don't like it"
        user_answer = raw_input()
        if user_answer == 'y':
            user_data.append(event)
            break
    
    for place in places:
        print place
        print "press 'y' if you like it 'n' if you don't like it"
        user_answer = raw_input()
        if user_answer == 'y':
            user_data.append(place)
            break
    for time in times:
        print time
        print "press 'y' if you like it 'n' if you don't like it"
        user_answer = raw_input()
        if user_answer == 'y':
            user_data.append(time)
            break
    if calls != 0:
        for key,value in My_Dictionary.items():
            for things in value:
                if event in things:
                    events_list.append(key)
                if place in things:
                    place_list.append(key)
                if time in things:
                    time_list.append(key)
    if len(events_list) == 0:
        print 'looks like we have no who likes the same event you do, come back later'
    else:
        print 'these are the people who wanna do ' + str(event) + ':'
        print events_list
    
    if len(place_list) == 0:
        print 'looks like we have no who wanna go to same place, come back later'
    else:
        print 'these are the people who wanna go to ' + str(place) + ':'
        print place_list 
    
    if len(time_list) == 0:
        print 'looks like we have no who wanna have fun at same time, come back later'
    else:
        print 'these are the people who wanna go to ' + str(time) + ':'
        print time_list 
   
            
        
    
    My_Dictionary[user_name] = user_data
for calls in range(5):
    my_program()





        


