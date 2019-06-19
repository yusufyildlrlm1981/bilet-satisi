
CREATE TABLE User<br />
(<br />
  Email VARCHAR(20) NOT NULL,<br />
  Password VARCHAR(20) NOT NULL,<br />
  Name VARCHAR(20) NOT NULL,<br />
  Surname VARCHAR(20) NOT NULL,<br />
  PRIMARY KEY (Email)<br />
);<br />
<br />
CREATE TABLE Types<br />
(<br />
  Type VARCHAR(20) NOT NULL,<br />
  PRIMARY KEY (Type)<br />
);<br />
<br />
CREATE TABLE Cities<br />
(<br />
  City VARCHAR(20) NOT NULL,<br />
  PRIMARY KEY (City)<br />
);<br />
<br />
CREATE TABLE ShowroomMain<br />
(<br />
  ID NUMERIC(5, 2) NOT NULL,<br />
  Name VARCHAR(20) NOT NULL,<br />
  City VARCHAR(20) NOT NULL,<br />
  PRIMARY KEY (ID),<br />
  FOREIGN KEY (City) REFERENCES Cities(City)<br />
);<br />
<br />
CREATE TABLE ShowroomCapacity<br />
(<br />
  Name VARCHAR(20) NOT NULL,<br />
  Capacity NUMERIC(5, 2) NOT NULL,<br />
  City VARCHAR(20) NOT NULL,<br />
  PRIMARY KEY (Name, City),<br />
  FOREIGN KEY (City) REFERENCES Cities(City)<br />
);<br />
<br />
CREATE TABLE Activity<br />
(<br />
  ID NUMERIC(5, 2) NOT NULL,<br />
  Name VARCHAR(20) NOT NULL,<br />
  Date DATE NOT NULL,<br />
  TicketsLeft NUMERIC(5, 2) NOT NULL,<br />
  Type VARCHAR(20) NOT NULL,<br />
  ID NUMERIC(5, 2) NOT NULL,<br />
  PRIMARY KEY (ID),<br />
  FOREIGN KEY (Type) REFERENCES Types(Type),<br />
  FOREIGN KEY (ID) REFERENCES ShowroomMain(ID)<br />
);<br />
<br />
CREATE TABLE Reservations<br />
(<br />
  ID NUMERIC(5, 2) NOT NULL,<br />
  NumberOfPeople NUMERIC(2, 0) NOT NULL,<br />
  Email VARCHAR(20) NOT NULL,<br />
  ID NUMERIC(5, 2) NOT NULL,<br />
  FOREIGN KEY (Email) REFERENCES User(Email),<br />
  FOREIGN KEY (ID) REFERENCES Activity(ID)<br />
);<br />
For the two views that we described previously, we generated two DDL statements as follows: <br />
CREATE VIEW rezs AS <br />
(SELECT Name, Date, Price, SName, City, NumberOfPeople <br />
FROM ((ACTIVITY NATURAL JOIN SHOWROOM) <br />
NATURAL JOIN RESERVATIONS));<br />
<br />
CREATE VIEW search AS <br />
(SELECT Name, Date, TicketLeft, SName, City, Capacity <br />
FROM (ACTIVITY NATURAL JOIN SHOWROOM));<br />
<br />



<br />
Django, web framework written in Python, is used to connect MySQL Database and Web Page. Below, two DML examples are given from our implementation to register a user and to check whether they enter the correct user email and password.
<br />
 def insertUser(email, name, surname, password):<br />
   with connection.cursor() as cursor:<br />
       cursor.execute( <br />
           "INSERT INTO TicketDb.user values (%s,%s,%s,%s)" % ( <br />
               "'{}'".format(email), "'{}'".format(name), "'{}'".format(surname), "'{}'".format(password)))<br />
<br />
def loginCheck(email, password):<br />
   cursor = connection.cursor()<br />
   query = ("Select email, Password from TicketDb.user where email= %s and Password = %s" % (<br />
       "'{}'".format(email), "'{}'".format(password)))<br />
   cursor.execute(query)<br />
<br />
   for (email, password) in cursor:<br />
       if email != "" and password != "":<br />
           return True<br />
       else:<br />
           return False<br />
   cursor.close()<br />
<br />
Below there are 2 other DML commands for viewing reservations of a given user and for doing a search among the activities. 
<br />
SELECT * FROM rezs;<br />
SELECT * FROM search;<br />
<br />
Currently in our design for the implementation we are not planning to implement User account, Showroom, Activity, City, Type deletion system. That is why we did not write deletion statements for these tables. However, to make user be able to cancel a reservation, we have to write a delete command which is:
<br />
DELETE FROM RESERVATION WHERE <br />
EMAIL = ‘User Email’ AND <br />
ACTIVITYID = ‘Activity ID of the Activity that desired to be canceled’<br />
<br />
Each time new tickets is bought from a user we need to update TicketsLeft at our Activity table. Also, we need to update Reservations when a user increases or decreases the number of tickets bought.
<br />
UPDATE Activity  <br />
SET ticketleft = ticketleft - x   (x is the number of tickets bought)<br />
WHERE ActivityID = ‘the ID of the activity which will be updated’<br />

<br />
UPDATE RESERVATION<br />
SET NumberOfPeople = NumberOfPeople + x (where x is the input from user)<br />
WHERE ActivityID = ‘the ID of the activity which will be updated’ AND<br />
Email = ‘Email address of the user logged in’<br />
<br />
Note that, when an update in Reservations table happens, we also need to update the Acitivty table because the amount of people joining to an activity is directly connected with number of tickets left. TicketsLeft in the Activity table will increase by x if NumberOfPeople in Reservations table decrease by x. Similarly, if TicketsLeft decrease by x, NumberOfPeople will increase by x.
<br />
