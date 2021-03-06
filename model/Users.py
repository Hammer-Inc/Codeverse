# User
# Return dict with keys as db columns
# Users - get, create


import pymysql

from model.Template import Template


class Users(Template):
    def getUser(self, id):
        cur = self.myConnection.cursor()
        dothisSQL = 'SELECT * '
        dothisSQL += 'FROM Users '
        dothisSQL += 'WHERE User_ID = %s'
        cur.execute(dothisSQL, id)
        self.myConnection.commit()
        queryResult = cur.fetchall()
        resultList = list()
        
        for result in queryResult:

            itemDict = dict()
            itemDict['User_ID'] = result[0]
            itemDict['firstname'] = result[1]
            itemDict['lastname'] = result[2]
            resultList.append(itemDict)

        if len(resultList) < 1:
            return None
        return resultList[0]

    def createUser(self, user_id, firstname, lastname):
        dothisSQL = 'INSERT INTO Users '
        dothisSQL += 'VALUES ( %s, %s, %s)'
        cur = self.myConnection.cursor()
        cur.execute(dothisSQL, (user_id, firstname, lastname))
        self.myConnection.commit()
        return cur.lastrowid

if __name__ == "__main__":
    users = Users() 
    users.createUser("test", "user6")
    print(users.getUser(3))

