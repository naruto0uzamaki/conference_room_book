# conference_room_book
interview question to book a conference room or check for vacancy 
			Conference Room Booking





Your office has dedicated meeting rooms where managers can conduct private discussions. They need a system for scheduling meetings that will be effective for scheduling meetings.
There are currently 3 meeting rooms with varying capacity:
Name	Person Capacity
C-Contact	3 People
S-Sharing	7 People
T-Team	20 People

Person Capacity - Maximum capacity of the meeting room.
Buffer Time - Time used for cleaning up the meeting room. It happens at fixed times from 09:00 - 09:15, 13:15 - 13:45 and 18:45 - 19:00. During buffer time, meeting rooms will not be available for booking.
Rules:
1. Bookings can be made only in a single day from 00:00 to night 23:45. It cannot overlap across days. So you cannot book from 23:00 to 01:00, but can from 23:00 to 23:45.
2. A booking can be started and ended only in 15 minute intervals, i.e. XX:00, XX:15, XX:30, XX:45. This means a booking can be made at 01:15 or 16:00 but not 15:35 or 16:03.
3. The rooms will be allocated only to those who book them, on a first come first serve basis.
4. The most optimal room which can accommodate the number of people will be allocated. For eg., if you asked for a 4 person capacity requirement then the S-Sharing (7 person capacity) will be allocated, provided it is available.
5. In case if the room of desired capacity is not available, the next available capacity room will be allocated. For eg., If you asked for the 4 person capacity room between 12:00 to 13:00 and the S-Sharing is not available then the T-Team will be allocated, provided it is available.
6. No meetings can be scheduled during the buffer time. If the booking time overlaps with the buffer time NO_VACANT_ROOM should be printed.
7. Bookings can be only made for 2 or more people and up to a maximum of 20 people. If the person capacity for booking is outside of 2-20 range NO_VACANT_ROOM should be printed.
8. Time input should follow HH:MM format (24 hours format). If an incorrect time input is provided then INCORRECT_INPUT should be printed.
Input Details
The system will take two types of inputs:
1. Book Meeting Room
As a manager, he/she shall schedule a meeting by giving a time period and capacity requirement.
Format - BOOK <start_time(inclusive)><end_time(exclusive)><person_capacity>
Example - BOOK 14:15 16:00 12
Possible Output:
“<Meeting_Room_Name>” - If the booking is successful
“NO_VACANT_ROOM” - If no room is vacant during the requested time period.

2. View available meeting rooms
As a manager, he/she would like to view a list of available meeting rooms by giving a time period. This should print the rooms in the ascending order of the room capacity. The rooms printed should be separated by a single space character.
Format - VACANCY <start_time(inclusive)><end_time(exclusive)>
Example - VACANCY 14:30 15:00
Output: C-Contact S-Sharing

Input Constraints
1. Time will be in HH:MM (24 hours) format
2. Time input should always consider the 15 minute time interval
3. For all the time inputs end_time>start_time

SAMPLE INPUT-OUTPUT 1
INPUT	OUTPUT
VACANCY 10:00 12:00	C-Contact S-Sharing T-Team
BOOK 11:00 11:45 2	C-Contact
BOOK 11:30 13:00 35	NO_VACANT_ROOM
BOOK 11:30 13:00 15	T-Team
VACANCY 11:30 12:00	S-Sharing
BOOK 14:00 15:30 3	C-Contact
BOOK 15:00 16:30 2	S-Sharing
BOOK 15:15 12:15 12	INCORRECT_INPUT
VACANCY 15:30 16:00	C-Contact S-Sharing
BOOK 15:30 16:30 2	C-Contact
VACANCY 15:45 16:00	S-Sharing
BOOK 16:00 17:00 5	S-Sharing
VACANCY 18:00 19:00	NO_VACANT_ROOM

SAMPLE INPUT-OUTPUT 2
INPUT	OUTPUT
BOOK 09:30 13:15 2	C-Contact
BOOK 13:45 18:45 2	C-Contact
BOOK 12:55 14:00 3	INCORRECT_INPUT
BOOK 13:45 17:15 6	S-Sharing
VACANCY 13:45 15:00	T-Team
BOOK 14:00 15:00 2	T-Team
BOOK 17:00 18:30 12	T-Team
VACANCY 17:00 18:00	NO_VACANT_ROOM
VACANCY 17:30 18:00	S-Sharing
BOOK 17:00 18:30 12	NO_VACANT_ROOM
BOOK 15:35 16:35 12	INCORRECT_INPUT

