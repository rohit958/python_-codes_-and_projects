#python

#install library in python 3.9
python -m pip install #modulename
------------------------------------------------------------------------
# map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
#map(function, iterables) 
------------------------------------------------------------------------
#The sort() method sorts the elements of a given list in a specific ascending or descending order.
#list.sort(reverse=True) descending order
------------------------------------------------------------------------
#rjust
string.rjust(length, fillchar)
------------------------------------------------------------------------
#backward for loop
for x in range(6,-1,-1):
------------------------------------------------------------------------
#backward loop -2
for x in reversed(range(6))
------------------------------------------------------------------------
#The any() function returns True if any item in an iterable are true, otherwise it returns False. If the iterable object is empty, the any() function will return False

 s = input()
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))

#modes in I/O
"""
Mode
					Description
			
r
					Opens a file for reading. (default)
			
w
					Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
			
x
					Opens a file for exclusive creation. If the file already exists, the operation fails.
			
a
					Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
			
t
					Opens in text mode. (default)
			
b
					Opens in binary mode.
			
+
					Opens a file for updating (reading and writing)
"""


------------------------------------------------------------------------
#######
#spark#
#######


"text search"

textFile = sc.textFile("hdfs://...")

# Creates a DataFrame having a single column named "line"
df = textFile.map(lambda r: Row(r)).toDF(["line"])
errors = df.filter(col("line").like("%ERROR%"))
# Counts all the errors
errors.count()
# Counts errors mentioning MySQL
errors.filter(col("line").like("%MySQL%")).count()
# Fetches the MySQL errors as an array of strings
errors.filter(col("line").like("%MySQL%")).collect()
------------------------------------------------------------------------
#############
#linked list#
#############


# A simple Python program to introduce a linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	'''
	Three nodes have been created.
	We have references to these three blocks as head(1st node),
	second and third

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | None |	 | 2 | None |	 | 3 | None |
	+----+------+	 +----+------+	 +----+------+
	'''

	llist.head.next = second; # Link first node with second

	'''
	Now next of first Node refers to second. So they
	both are linked.

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | null |	 | 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''

	second.next = third; # Link second node with the third node

	'''
	Now next of second Node refers to third. So all three
	nodes are linked.

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | o-------->| 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''




------------------------------------------------------------------------
             
 #reading a text file-done
 
 ------------------------------------------------------------------------
 #reading a csv file-done
 ------------------------------------------------------------------------
 #reading JSON file-done
 ------------------------------------------------------------------------
 #reading a xml file-pending
 ------------------------------------------------------------------------
 
 #connection to teradata
 
 ------------------------------------------------------------------------
 #connection to spark
 ------------------------------------------------------------------------
 
 #coneection to mongoDB
 ------------------------------------------------------------------------
 
 #reading excel file
 import pandas as pd
 import xlrd
 
 with pd.excel.open()
 
 
 ------------------------------------------------------------------------
 #python hive connection-pyhive
 
 from pyhive import hive
cursor = hive.connect('localhost').cursor()
cursor.execute('SELECT * FROM my_awesome_data LIMIT 10')
print(cursor.fetchone())
print(cursor.fetchall())


 #python hive connection-pyh2
import pyhs2
    with pyhs2.connect(host='localhost',
           port=10000,
           authMechanism="PLAIN",
           user='your_user',
           password='your_password',
           database='your_default_db') as conn:
        with conn.cursor() as cur:
            print cur.getDatabases()
            cur.execute("select * from table")
            #Return info from query
            print cur.getSchema()