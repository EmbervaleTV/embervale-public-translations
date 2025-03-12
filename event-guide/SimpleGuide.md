
### 📝 What to Include in Your Submission  
1. **State that you're submitting an event.**  
2. **Describe your event idea.** You can submit just an idea, but providing more details helps:  
   - What is the **scenario**?  
   - What **options** do players have?  
   - What **text** follows each option?  
3. **Specify outcomes.** Each option should mention its effects, such as:  
   - Gained/lost **morale**, **chests**, **effects**, or **tools**  
   - How long effects last  
   - Suggested **skill rolls** and difficulty levels  
   - Multiple possible outcomes for the same choice  

Even if you're not confident in writing, a rough draft of how you imagine it will help ensure the final event fits your vision.  

### 📚 Useful Resources  
- **List of effects & tools:**  
  [adventureData.txt](https://github.com/EmbervaleTV/embervale-public-translations/blob/main/base-en/adventureData.txt)  

### ⚡ Faster Implementation  
Events that use existing game mechanics can be added much quicker than those requiring new features, effects, or filters.  

### ✅ Ticket Status  
- **Seen:** Your ticket will be labeled **adventure-ideas** once reviewed.  
- **Ready for the game:** When marked **solved**, your event is good to go!  

We appreciate your contributions! 🚀  



# Example

Scenario: On the road, the party encounters a burly warrior named Manfred listlessly plucking caterpillars from some weeds. He explains that he's been contracted to harvest materials for some lazy mage, but they barely pay him and he's not entirely sure what a 'brain stool' looks like.

Option 1: 
Pay him a better rate to harvest for you instead. (3 decorated chests)
You arrange a meeting spot and go on your way. That night, Manfred arrives with the materials he's gathered, and you exchange a respectable sum of coin for his harvest. A deal well made!
(gain random materials chest)

Option 2:
Hire him as an adventurer. (1 coin stack)
Manfred gladly drops his bag of caterpillars. “Now that's more like it,” he crows, pocketing your coin. “Was gettin' real tired of catching frogs. Where we headed, chief?”
(gain 5 morale and Manfred, a warrior companion)

Option 3: 
Wish him well.
Manfred gloomily waves to you as you pass him by. You elect not to tell him there's a caterpillar in his hair.
(gain 5 morale)

Option 4: 
Attack him and steal his harvest! (needs less than 50 morale)
“Couple-a thieves, huh?” Manfred hefts his mighty warhammer in response. “Me mum taught me how to deal with you.”
(starts a fight, 3 random players against Manfred, who should be pretty strong)

If you win:

You overpower Manfred and steal his sack of materials. He glumly stares after you before returning to his expedition, scooping a handful of caterpillars into a new, empty sack. You can't help but feel a little guilty... the poor man will be here for another twelve hours at the least.
(lose 10 morale but gain a random materials chest)

If you lose:

Years of hauling pumpkins and mining ore have left Manfred with the muscles of a god, and your party doesn't stand a chance against him. You scatter for the hills, wounded and regretting your recent life decisions immensely. Manfred throws tomatoes after your retreat.
(lose 20 morale)