from Class.DB import DBAccess as DB
import sys

class Car(DB): 
    def __init__(self): 
        self.idCar = None
        self.dateStockCar = None
        self.dateTechControlCar = None
        self.priceCar = None
        self.nameBrand = None
        self.nameMotor = None
        self.nameType = None
        self.promoCar = None


    @staticmethod
    def NameTable():
        # Return the name table
        return "Car"

    @staticmethod
    def IdColumn():
        # Return the id column
        return "idCar"
    
    @classmethod
    def CarListStock(clss): 
        carList = []
        cursor = DB.DBCursor()
        if cursor != None:
            try:
                cursor.execute("SELECT idCar, STRFTIME('%d/%m/%Y', dateStockCar) as dateStockCar, dateTechControlCar, priceCar, nameBrand, nameMotor, \
                nameType, promoCar \
                FROM Car \
                NATURAL JOIN Brand \
                NATURAL JOIN Motor\
                NATURAL JOIN Type\
                WHERE idCar NOT IN (select idCar FROM deal WHERE isResDeal = 0)")
                resultsQuery = cursor.fetchall()
                for row in resultsQuery:
                    car = clss.LoadResults(cursor, row)
                    carList.append(car)
                return carList
            except:
                print("Error in CarListStock")
                print(sys.exc_info())
                return None 
            finally: 
                DB.DBClose(cursor)

    @classmethod
    def CarListHistory(clss):
        carListHist = []
        cursor = DB.DBcursor()
        if cursor != None:
            try:
                cursor.execute("SELECT idCar, STRFTIME('%d/%m/%Y', dateStockCar) as dateStockCar, dateTechControlCar, priceCar, nameBrand, nameMotor, nameType, promoCar \
                FROM Car \
                NATURAL JOIN Brand \
                NATURAL JOIN Motor\
                NATURAL JOIN Type\
                WHERE idCar  IN (select idCar FROM deal WHERE isResDeal = 0)")
                resultsQuery = cursor.fetchall()
                for row in resultsQuery:
                    car = clss.LoadResults(cursor, row)
                    carListHist.append(car)
                return carListHist

            except:
                print("Error in CarListHistory")
                print(sys.exc_info())
                return None
            finally:
                DB.DBClose(cursor)
    
    @classmethod
    def CarFreePlacesStock(clss): 
        cursor = DB.DBCursor()
        if cursor != None: 
            try: 
                cursor.execute("SELECT count(*) \
                FROM Car \
                NATURAL JOIN Brand \
                NATURAL JOIN Motor \
                NATURAL JOIN Type \
                WHERE idCar NOT IN (select idCar FROM deal WHERE isResDeal = 0)")
                return cursor.fetchone()[0]
            except:
                print("Error in CarFreePlacesStock")
                print(sys.exc_info())
                return None 
            finally: 
                DB.DBClose(cursor)
