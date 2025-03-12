the_vampire_curse = {
    "scenario": "§player0§ is bitten by a vampire while on a hunt. They start showing signs of vampirism.",
    "answers": [
        {
            "answer": "This is clearly a curse, we must get rid of §player0§ as soon as possible.",
            "requirements": {},
            "statCheckTarget": None,
            "statCheck": {},
            "outcomes": [
                {
                    "description": "Without §player0§ the party is undoubtly weakened and not everybody is happy about your decision.",
                    "weights": 100,
                    "morale": -5,
                    "leaderFame": -5,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "player0", "effect": "banished", "duration": 9999}
                    ],
                    "battleOutcome": None
                }
            ]
        },
        {
            "answer": "I'll try to cure the curse myself.",
            "requirements": {},
            "statCheckTarget": "leader",
            "statCheck": {
                "vitality": 16,
                "mag_resistance": 11
            },
            "outcomes": [
                {
                    "description": "The cure is a success, §player0§ is saved from the curse.",
                    "requiredStatCheck": ["vitality", "mag_resistance"],
                    "morale": 5,
                    "leaderFame": 5,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "leader", "effect": "healer", "duration": 5}
                    ],
                    "battleOutcome": None
                },
                {
                    "description": "The cure is a success, but I feel a little odd...",
                    "requiredStatCheck": ["vitality"],
                    "morale": 0,
                    "leaderFame": 2,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "leader", "effect": "vampiristic", "duration": 9999}
                    ],
                    "battleOutcome": None
                },
                {
                    "description": "The cure is a failure, §player0§ is now fully turned into a vampire. At least I am unharmed...",
                    "requiredStatCheck": ["mag_resistance"],
                    "morale": -5,
                    "leaderFame": 0,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "player0", "effect": "vampiristic", "duration": 9999}
                    ],
                    "battleOutcome": None
                },
                {
                    "description": "The cure is a total failure, not only §player0§ is now fully turned into a vampire, but I also start to show symptoms.",
                    "weights": 25,
                    "morale": -10,
                    "leaderFame": -5,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "leader", "effect": "vampiristic", "duration": 9999},
                        {"target": "player0", "effect": "vampiristic", "duration": 9999}
                    ],
                    "battleOutcome": None
                }
            ]
        },
        {
            "answer": "I'll leave the task to §player1§, they have more experience with these matters.",
            "requirements": {},
            "statCheckTarget": "player1",
            "statCheck": {
                "vitality": 16,
                "mag_resistance": 11
            },
            "outcomes": [
                {
                    "description": "§player1§ is successful in curing §player0§ from the curse.",
                    "requiredStatCheck": ["vitality", "mag_resistance"],
                    "morale": 5,
                    "leaderFame": 0,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "player1", "effect": "healer", "duration": 5}
                    ],
                    "battleOutcome": None
                },
                {
                    "description": "§player1§ is unable to cure §player0§ from the curse, and now §player0§ is a vampire for good.",
                    "requiredStatCheck": ["mag_resistance"],
                    "morale": -5,
                    "leaderFame": 0,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "player0", "effect": "vampiristic", "duration": 9999}
                    ],
                    "battleOutcome": None
                },
                {
                    "description": "It turned out player §player1§ had no idea what they were doing, we have a massive vampire problem now!",
                    "weights": 25,
                    "morale": -10,
                    "leaderFame": 0,
                    "groupActions": None,
                    "PlayerEffects": [
                        {"target": "player0", "effect": "vampiristic", "duration": 9999},
                        {"target": "player1", "effect": "vampiristic", "duration": 9999},
                        {"target": "player2", "effect": "vampiristic", "duration": 9999}
                    ],
                    "battleOutcome": None
                }
            ]
        }
    ]
}
