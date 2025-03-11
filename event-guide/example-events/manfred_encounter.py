manfred_encounter = {
    "scenario": "On the road, the party encounters a burly, bearded warrior named Manfred listlessly picking caterpillars from some weeds. He explains that he's been contracted to harvest materials for some lazy alchemist, but they barely pay him and he's not even sure what a 'brain stool' is.",
    "spawnConditions": {
        "items": {"decorated_chest": 3}
    },
    "answers": [
        {
            "answer": "Offer Manfred some gear to harvest for you instead.",
            "requirements": {"decorated_chest": 3},
            "outcomes": [
                {
                    "description": "You arrange a meeting spot and go on your way. That night, Manfred arrives with the materials he's gathered, and you exchange some of your own supplies for his harvest. A deal well made!",
                    "weights": 100,
                    "morale": 0,
                    "leaderFame": 0,
                    "groupActions": [{"add_random_item": {"items": ["uncommon_material_chest", "epic_material_chest"], "weights": [75, 25]}}],
                    "PlayerEffects": []
                }
            ]
        },
        {
            "answer": "Hire him as a mercenary.",
            "requirements": {"coin_stack": 1},
            "outcomes": [
                {
                    "description": "Manfred gladly drops his sack of caterpillars. “Now that's more like it,” he crows, pocketing your coin. “Was gettin' real tired of picking leaves. Where we headed, chief?”",
                    "weights": 100,
                    "morale": 5,
                    "leaderFame": 0,
                    "groupActions": [{
                        "add_companion": {
                            "monster": "Manfred",
                            "classification": "warrior",
                            "gender": "male",
                            "power_multiplier": 1.2
                        }}]
                    ,
                    "PlayerEffects": []
                }
            ]
        },
        {
            "answer": "Attack him and steal his harvest!",
            "requirements": {"max_morale": 50},
            "outcomes": [
                {
                    "description": "“Couple-a thieves, huh?” Manfred hefts his mighty warhammer in response. “Me mum taught me how to deal with you.”",
                    "weights": 100,
                    "groupActions": [{
                        "start_pvp_battle": {
                            "team_1": ["player0", "player1", "player2"],
                            "team_2": ["Manfred"],
                            "difficulty_multiplier": 1.5
                        }
                    }],
                    "PlayerEffects": [],
                    "battleOutcome": {
                        "win": {
                            "description": "You overpower Manfred and steal his sack of materials. He glumly stares after you before returning to his expedition, scooping a handful of caterpillars into a new, empty sack. You can't help but feel a little guilty... the poor man will be here for another twelve hours at the least.",
                            "morale": -10,
                            "leaderFame": 0,
                            "groupActions": [{"add_random_item": {"items": ["uncommon_material_chest", "epic_material_chest"], "weights": [50, 50]}}],
                            "PlayerEffects": []
                        },
                        "lose": {
                            "description": "Years of hauling pumpkins and mining ore have left Manfred with the muscles of a god, and your party doesn't stand a chance against him. You scatter for the hills, wounded and regretting your recent life decisions immensely. Manfred throws tomatoes after your retreat.",
                            "morale": -20,
                            "leaderFame": -5,
                            "PlayerEffects": [
                                {"target": "player0", "effect": "wounded", "duration": 999},
                                {"target": "player1", "effect": "wounded", "duration": 999},
                                {"target": "player2", "effect": "wounded", "duration": 999}
                            ]
                        }
                    }
                }
            ]
        },
        {
            "answer": "Wish him well.",
            "requirements": {},
            "outcomes": [
                {
                    "description": "Manfred gloomily waves to you as you pass him by. You decide not to tell him there's a caterpillar in his hair.",
                    "weights": 100,
                    "morale": 2,
                    "leaderFame": 0,
                    "groupActions": None,
                    "PlayerEffects": []
                }
            ]
        }
    ]
}
