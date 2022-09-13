from flask import Flask
from flask_restful import Resource,Api,reqparse
import sqlite3

colourList = []
memoryList = []
class handleColour(Resource):
    TABLE_NAME = 'colours'
    def get(self,colour):
        item = self.findByName(colour)
        if item:
            return item
        return {'message' : "Laptop with colour '{}' not found".format(colour)}
    @classmethod
    def findByName(cls,colour):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE colour=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (colour,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'laptop': colour}
    def post(self,colour):
        item = {'laptop': colour}
        if self.findByName(colour):
           return {'message': "Laptop with colour '{}' already exists.".format(colour)}
        try:
            handleColour.insert(colour)
        except:
            return {"message" : "An error occurred inserting the colour for laptop."}
        return item

    @classmethod
    def insert(cls,colour):
        price = 1000
        item =  {'colour': colour,
                 'price': price}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table='colours')
        cursor.execute(query, (colour,price))


        connection.commit()
        connection.close()

    def delete(self, colour):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE colour=?".format(table='colours')
        cursor.execute(query, (colour,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

class handleMemory(Resource):
    TABLE_NAME = 'memory'
    BASE_MEMORY_PRICE = 25 # price per GB
    def get(self,memory):
        item = self.findByName(memory)
        if item:
            return item
        return {'message' : "Laptop with memory '{}' not found".format(memory)}
    @classmethod
    def findByName(cls,memory):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE memory=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (memory,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'memory': row[0],
                    'price' : row[1] }

    def post(self,memory):
        item = {'laptop': memory}
        if self.findByName(memory):
           return {'message': "Laptop with memory '{}' already exists.".format(memory)}
        try:
            handleMemory.insert(memory)
        except:
            return {"message" : "An error occurred inserting the memory for laptop."}
        return item

    @classmethod
    def insert(cls,memory):
        price = int(memory) * cls.BASE_MEMORY_PRICE
        print(price)
        item =  {'memory': memory,
                 'price': price}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table='memory')
        cursor.execute(query, (memory,price))


        connection.commit()
        connection.close()

    def delete(self, memory):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE memory=?".format(table='memory')
        cursor.execute(query, (memory,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

class findCost(Resource):
    def get(self,colour,memory):
        item = self.findByConfig(colour,memory)
        if item:
            return item
        return {'message' : "Laptop with colour '{}' and memory '{}' configuration not found".format(colour,memory)}
    @classmethod
    def findByConfig(cls,colour,memory):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table} WHERE colour=?".format(table='colours')
        result = cursor.execute(query, (colour,))
        foundColour = result.fetchone()

        query = "SELECT * FROM {table} WHERE memory=?".format(table='memory')
        result = cursor.execute(query, (memory,))
        foundMemory = result.fetchone()
        connection.close()
        price = int(foundColour[1]) + int(foundMemory[1])
        if foundColour and foundMemory :
            return {'colour': colour,
                    'memory': memory,
                    'price': price }
