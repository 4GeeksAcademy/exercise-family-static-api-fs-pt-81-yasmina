
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {"id": self._generateId(), "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": self._generateId(), "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": self._generateId(), "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]}
        ]
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name 
        self._members.append(member)
        return member  

    def delete_member(self, id):
        self._members = [m for m in self._members if m["id"] != id]
        return {"done": True}  

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        return None  

    def update_member(self, member_id, updated_data):
        for member in self._members:
            if member["id"] == member_id:
                member.update(updated_data) 
                return member 
        return None  

    def get_all_members(self):
        return self._members
