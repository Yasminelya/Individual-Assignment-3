# -*- coding: utf-8 -*-

from flask import Flask, jsonify

server = Flask("phonebook")
        
phonebook = [{"name":"Candela", "phone":353},
             {"name":"pepe", "phone": 1234},
             {"name":"Leila", "phone": 62881}]

@server.route("/Contact")
def Contact():   
    return jsonify(phonebook)

@server.route("/add_contact/<name>/<phonenuber>")
def add_contact(name,phone):   
    new_contact = {"name":name, "phone":phone}
    phonebook.append(new_contact)
            
    return jsonify(new_contact + " is added to the phonebook")

@server.route("/get_phone/<name>")
def get_phone(name):   
    for contact in phonebook:
        if contact["name"] == name:
            number = contact["phone"]
    return jsonify(number)

@server.route("/delete_contact/<name>")
def delete_contact(name):
    index = next(index for index, dictionary in enumerate(phonebook) if dictionary['name'] == name)
    del phonebook[index]
    return jsonify(name + " has been deleted from the phonebook.")

@server.route("/update_phone/<name>/<new_phone>")
def update_phone(name, new_phone):

    for contact in phonebook:
        if contact["name"] == name:
            contact["phone"] = new_phone

    return jsonify("The phone number of " + name + " is now: " + new_phone)
    
server.run()