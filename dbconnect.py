import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter Word: ")

query = cursor.execute("select DEFINITION from Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()  # This will return list of tuples
if results:
    for result in results:
        print(result[0])
else:
    print("No Word Found!")
