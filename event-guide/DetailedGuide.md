We've uploaded example events that will help you understand how to build events. 


Available groupActions with parameters:

    heal(players: list)
    -------
    revive(players: list, effects: list[dict] = [])
    Each effect dictionary should have the following structure:
    {
        "effect": "effect_name",
        "duration": int
    }
    -------
    add_item(name: str)
        example: "add_item": {"name": 'fabled_chest'}

    -------
    add_random_item(self, items: list, weights: list)
        example: "add_random_item": {"items": ['fabled_chest', 'mythical_chest'], 'weights': [25,25]}
    
    -------
    remove_item(name: str, amount: int)

    -------
    remove_random_item(amount: int)
        avaliable items: coin_stack, wooden_chest, decorated_chest, fabled_chest, mythical_chest
    
    -------
    add_tool(name: str)

    -------
    add_fame(players: list, value: int)

    -------
    start_pvp_battle(team_1: list, team_2: list, difficulty_multiplier: float, faint=True)
    
    -------
    start_pve_battle(players: list, monsters: list, difficulty_multiplier: float)
    
    -------
    remove_random_negative_effects(amount: int)

    -------
    remove_effect(players: list, effect: str)

    -------
    apply_global_effect(effect: str, duration: int)

    -------
    # You can add monsters as companion. The parameter monster can also be used for the name of a predefined NPC. If you don't specify a monster you get a random human companion
    add_companion(monster=None, classification:str, gender:str, effects=[]) # effects is here the same as playerEffects below but added on creation.
    remove_companion(players: list) # remove companion.

    -------
    # trigger a specific event in x rooms
    queue_event(name: str, room_offset_min: int, room_offset_max: int)

Available requirements:

    "requirements": {"max_morale": 30}  # morale needs to be below 30
    "requirements": {"min_morale": 80}  # morale needs to be between 80 and 100
    "requirements": {"coin_stack": 2}   # group needs 2 coin stacks

Available statCheck:

    wisdom, strength, dexterity, luck, vitality, fame, armor, mag_resistance, agility, smith, alchemist, cook, morale

Stat check has a characters ability against a difficulty level and then decides the outcome. 
It's like the dice in Boulders gate and should be used in some events if fitting.

If the statCheck is morale then statCheckTarget is "party". Otherwise, any of the statCheckTarget below need to be specified!

If there are multiple statChecks then it needs to have an outcome for every combination of failed and successful checks. Multiple stat checks should be the exception, often one is enough.

Available statCheckTarget:

    leader, player0, player1, player2, player3... 

There can't be a player1 without a player0 already existing and so one. Always start with 0 and if there are more player involved then increase the number.

You can choose from these available effects. If there is nothing fitting add a new effect. For example buffs or debuffs
New effects need to be explained in json as comment. A comment is just a # with the explanation behind it like in Python. 
For example: 
```
"PlayerEffects": [
   {"target": "player0", "effect": "upset", "duration": 2},
   {"target": "player1", "effect": "upset", "duration": 2}
],
```
PlayerEffects are only applied


Adventure Conditional Events
Adventure events are triggered based on specific conditions. By default, events check if there are enough players with more than 0 HP who are neither banished nor bots.

Possible Conditions:
```
{"lobbySize": 30}: Triggers only if more than 30 people joined an adventure
{"morale_below": 20}: Triggers when morale is between 0 and 19.
{"morale_above": 60}: Triggers when morale is 61 or higher.
{"monster_lvl_below": 50}: Triggers when the monster's level is below 50.
{"monster_lvl_above": 75}: Triggers when the monster's level is above 75.
{"items": {"coin_stack": 1}} # Triggers the event if at least the specified amount of items or more are in the current Adventure inventory
{"all_previous_events": ["a_dire_prediction", "arena_betting_spectacle"]}: Triggers only if both specified events have occurred in this adventure. You can specify an unlimited number of prerequisite events, allowing for complex sequences.
{"any_previous_events": ["a_dire_prediction", "arena_betting_spectacle"]}: Triggers if any of the specified events have occurred in this adventure.
{"leaderEffect": ["deserter", "training",  "banished", 'unavailable', 'petrified', "fainted"]}: Event only triggers when the leader has any of these effects
```

PlayerCondition
```
{"playerEffect": ["plagued"]}: Triggers if at least one player has one of the specified effect(s). The affected player will be designated as Player0. If multiple have that effect one Player gets Chosen by random and the remaining ones also by random
{"partyEffect": ["wounded", "badly_wounded", "maimed"]}: Triggers only if enough players in the party have one of the specified effects. For example, if the event requires three players, but only two have these effects, the event will not trigger.
{"partyClass": ["knight", "ranger"]}: Triggers only if enough players in the party have the specified class. For example, if the event requires three players, but only two have that class, the event will not trigger.
{"partyRace": ["human", "elf", "demon"]}: Triggers only if enough players in the party have the specified class. For example, if the event requires three players, but only two have that class, the event will not trigger.
```

All conditions can be combined, for example you can require a previous event and additionally 80 more or higher. 


A list of all effects and tools in the game can be found here: https://github.com/EmbervaleTV/embervale-public-translations/blob/main/base-en/adventureData.txt
