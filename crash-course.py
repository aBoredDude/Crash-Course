import pandas as pandas
import sqlite3 as sqlite3
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

def readHtml(url='https://en.wikipedia.org/wiki/2020_United_States_presidential_election', name='Ballot access'):
    table1 = pandas.read_html(url, match=name)
    return table1[0].fillna(0)


def addToDB(values):
    cursor.execute(f"""
    INSERT INTO election VALUES
        ({str(values).replace("[", "").replace("]", "")})
    """)
    connection.commit()

#for i in range(len(readHtml())):
#    addToDB(readHtml().iloc[[i]].values.flatten().tolist()[1:])

result = cursor.execute("SELECT * FROM election WHERE election.'Party or Label' = 'Republican'")
print(result.fetchall())