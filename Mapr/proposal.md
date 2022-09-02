

# <name of app>

## Overview
Register users and locations and organizes them. Dsiplay usrs and their locations on an interactiv e map. Sort users by social group. 

## Functionality
- Allow users to join groups
- Users can signup/login
    - Store user's initial location on signup
- Allow users to set their profile to private
- Show a map of given users (group)

#### Libraries
- Django
- JavaScript

## Data model
User
- username
- password
- location (ForeignKey)
- groups (ManyToMany)
- private

Location
- latitude
- longitude
- timezone (nullable)

Group
- name
- private
- events (default=None)

Event
- tbd


