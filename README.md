# GPT-Generated-Dungeon
A simple text based dungeon game that was entirely generated by Open Ai's GPT-3

## Input

The input was broken into two parts, `JSON game input` and `Game logic`, where `JSON game input` was generated first.

### JSON game input
>generate a fantasy dungeon with 5-10 interconnected rooms. There should be multiple monsters to fight in the dungeon. The dungeon should contain multiple items. There should be a powerful final dungeon boss. The dungeon should contain a puzzle with a valid solution. items should have a mass and value field. weapons should have a damage field. Output a json representation in the following format:
>
>#room
>{
>roomId: roomId,
>roomName: name of room,
>roomDescription: room description,
>connectedRooms: list of connected room IDs,
>items: list of ids of items found in room,
>monsters: list of monsters in room
>}
>
>#item
>{
>itemId: itemId,
>itemName: name of item,
>itemDescription: description of item,
>mass: mass of item,
>value: value of item
>}
>
>#monster
>{
>monsterId: monster id,
>monsterName: name of monster,
>monsterDescription: description of monster,
>inventory: item ids of items held by monster
>}

### Game logic

> generate a text based python game that takes the above json as inputs and runs the game. the player must be able to move between rooms, attack monsters and pick up items. The game is over when the final boss is defeated. The player starts with a weapon.

## Runtime error cleanup

The generated logic *almost* worked without any cleanup. However, there were two issues that needed manual fixing:

- It was using strings to index into json arrays at a handful of locations.
- The player never had it's inventory field initialized.

If you want to see what the initial code generated before cleanup was like, take a look at the initial commit.