from py2neo import Graph, Node, Relationship
from datetime import datetime
import uuid

graph = Graph("bolt://localhost:7687", user="neo4j", password="belalraouf")


class User:

    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.nodes.match("User", username=self.username).first()
        return user

    def register(self, password):
        if not self.find():
            user = Node("User", username=self.username, password=password)
            graph.create(user)
            return True

        return False

    def verify_password(self, password):
        user = self.find()
        if not user:
            return False

        return password == user["password"]
