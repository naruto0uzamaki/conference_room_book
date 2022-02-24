#BOOK 15:15 12:15 12 INCORRECT_INPUT
#VACANCY 15:30 16:00 C-Contact S-Sharing
#BOOK 09:30 13:15 2
from datetime import date, datetime

avail_slots ={'C-Contact':'3','S-Sharing':'7','T-Team':'20'}
buffer_time = [['09:00','09:15'], ['13:15' , '13:45'],['18:45', '19:00']]

booking = input('BookSlot ').split(' ')


booked_slot = []


def input_check():
    time_check_1 = datetime.strptime(booking[1],'%H:%M').time() #18
    time_check_2 = datetime.strptime(booking[2],'%H:%M').time() #19

    end_time = (booking[2])
    start_time = (booking[1])

    interval_1 = int(end_time[3:]) 
    interval_2 = int(start_time[3:])

    for i in range(3):
        if datetime.strptime(buffer_time[i][0],'%H:%M').time() <= time_check_1 < datetime.strptime(buffer_time[i][1],'%H:%M').time() or datetime.strptime(buffer_time[i][0],'%H:%M').time() < time_check_2 < datetime.strptime(buffer_time[i][1],'%H:%M').time():
            return 'NO_VACANT_ROOM' 

        elif time_check_1 < time_check_2:  # correct input end time greter than start time 
            if interval_1 % 15 == 0 and interval_2 % 15 == 0: # time interval check of 15 min atleast multiples of 15 
                return True
            else:
                print ('INCORRECT_INPUT')
            

    if len(booking) == 4:
        
        if int(booking[3]) < 2 or int(booking[3]) > 20 : # range of max alloted seats 
            return 'NO_VACANT_ROOM'

        elif time_check_1 < time_check_2:  # correct input end time greter than start time 
            if interval_1 % 15 == 0 and interval_2 % 15 == 0: # time interval check of 15 min atleast multiples of 15 
                return True
            else:
                print ('INCORRECT_INPUT')

        else:
            return('INCORRECT_INPUT')


def slot_booking():
    empty_hall = []

    for i in avail_slots:
        if int(booking[3]) <= int(avail_slots[i]):
            empty_hall.append(i)

    a=[]
    a.append(booking[1])
    a.append(booking[2])
    booked_slot.append(a)

    return (empty_hall[0])


def vacant_slot():
    empty_slot_any = []
    input = input_check()

    if input == True:
        if len(booked_slot) >0:
            for i in range(len(booked_slot)):
                for j in range(len(booked_slot)):
                    if booked_slot[i][j] == booking[1] or booked_slot[i][j] == booking[2]:
                        return('NO_VACANT_ROOM')
                    else:
                        for i in avail_slots:
                            if int(avail_slots[i]) > 0:
                                empty_slot_any.append(i)
        else:
            for i in avail_slots:
                if int(avail_slots[i]) > 0:
                    empty_slot_any.append(i)

    if len(empty_slot_any) > 0:
        return empty_slot_any
    else:
        return input
    

    
def book_slot():
    if input_check() == True:
        if len(booked_slot)> 0:
            for i in range(len(booked_slot)):
                for j in range(len(booked_slot)):
                    if booked_slot[i][j] == booking[1] or booked_slot[i][j] == booking[2]:
                        return('No_vacant_room')
                    else:
                        return(slot_booking())
        else:
            return( slot_booking())



if booking[0] == 'BOOK':
    print(book_slot())

elif booking[0] == 'VACANCY':
    empty = vacant_slot()
    print(empty)