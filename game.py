import json

#load map data from json
map_data = json.loads(open("map.json").read())

#player data
player = {
    'hp': 100,
    'name': 'Player',
    'location': '0',
    'weapon': '0'
}

#function to print the current room
def print_room(room):
    print(room['roomName'])
    print(room['roomDescription'])
    print('Connected Rooms: ' + ', '.join(room['connectedRooms']))
    print('Monsters: ' + ', '.join(room['monsters']))
    print('Items: ' + ', '.join(room['items']))

#function to move to a new room
def move_to_room(room_id):
    global player
    if room_id in map_data['rooms'][player['location']]['connectedRooms']:
        player['location'] = room_id
        print('You have moved to ' + room_id)
    else:
        print('You cannot move to that room.')

#function to attack a monster
def attack_monster(monster_id):
    global player
    if monster_id in map_data['rooms'][player['location']]['monsters']:
        #monster is in the room
        monster = map_data['monsters'][monster_id]
        weapon = map_data['weapons'][player['weapon']]
        print('You attack the ' + monster['monsterName'] + ' with your ' + weapon['weaponName'])
        print('You deal ' + str(weapon['damage']) + ' damage!')
        #remove monster from room
        map_data['rooms'][player['location']]['monsters'].remove(monster_id)
        #add items from monster to room
        map_data['rooms'][player['location']]['items'] += monster['inventory']
        print('You have defeated the ' + monster['monsterName'])
    else:
        print('There is no monster here to attack.')

#function to pick up an item
def pick_up_item(item_id):
    global player
    if item_id in map_data['rooms'][player['location']]['items']:
        #item is in the room
        item = map_data['items'][item_id]
        print('You pick up the ' + item['itemName'])
        #remove item from room
        map_data['rooms'][player['location']]['items'].remove(item_id)
        #add item to player inventory
        player['inventory'].append(item_id)
    else:
        print('There is no item here to pick up.')

#function to check for a puzzle
def check_for_puzzle():
    global player
    if player['location'] == '5':
        #player is in the boss room
        puzzle = map_data['puzzle']
        print(puzzle['puzzleDescription'])
        answer = input('What is the answer? ')
        if answer == puzzle['solution']:
            print('You have solved the puzzle!')
            #remove final boss from room
            map_data['rooms'][player['location']]['monsters'].remove('5')
            #add items from final boss to room
            map_data['rooms'][player['location']]['items'] += map_data['finalBoss']['inventory']
            print('You have defeated the final boss!')
        else:
            print('Incorrect answer!')
    else:
        print('There is no puzzle here.')

#main game loop
while True:
    #print current room
    print_room(map_data['rooms'][player['location']])
    #get user input
    command = input('What do you want to do? ')
    #parse command
    if command == 'move':
        room_id = input('Where do you want to move? ')
        move_to_room(room_id)
    elif command == 'attack':
        monster_id = input('Which monster do you want to attack? ')
        attack_monster(monster_id)
    elif command == 'pick up':
        item_id = input('Which item do you want to pick up? ')
        pick_up_item(item_id)
    elif command == 'puzzle':
        check_for_puzzle()
    elif command == 'quit':
        break
    else:
        print('Invalid command!')
