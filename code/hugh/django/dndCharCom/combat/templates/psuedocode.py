#At first this was in the models.py file but then I realized I should just pseudo the whole thing and then start putting pieces where they need to be

#dndCharCom is meant to recreate tabletop RPG combat including random dice rolls by click.

#using a character creator that was partially written out before with the class I will store characters in the the DB

#character models will include the list below but the initial implementation of the combat similator will be very simple

#get two fighter character models completed, all stats coded, all manuevers and special actions written out as rules that direct the characters available choices

#at first the only choice will be "attack" since special manuevers are restricted to higher level characters

#however any character can technically try to wrestle another one, so those rules should be second at least

#the attacks will follow the same equations as in DnD, which I need to write out

#the attacks will remove health from the character model, check if they died or a special status was applied, and then pass the turn

#who takes first turn will greatly impact how fights go, so it will be a random coin flip or the user can give one fighter first turn

#each turn the first character takes an action, a bonus action, and may move once I make the grid for them to move on

#then the second character, if still alive, takes an action, a bonus action, and may move if possible

#then just keep going until a character dies or the player exits the game

Timeline for project

End of week one complete character entry / character model
End of week two complete combat app for single fighter combat
End of week three have functional combat display, full user login, storage
and review of characters

scope for project
combat app
    retrieve character models
    by turn sequence allow models to attack one another
    apply damage until one "dies"
    congratulate winner #AND give a summary of the battle? 
    store win / loss record
character creation 
    allow full character creation
    store character
    allow user to login and see their characters
    #allow user to edit characters? (stretch)

mad lib combat description flavor adder?

out of scope for combat app
#saving games
#saving character models post combat status
#all combat will use the character model as entered into the DB, and will not allow alterations

#potential scope for character app
#modifying character models after creation

so it will be two apps working together to first build the character model, and then store it in the DB

then retrieve the model from the DB and apply changes to it on screen for the user

I would like to have some "flavor" for combat descriptions similar to dwarf fortress "you hit him with the axe" vs "you deliver a glancing blow, but still manage to cut open their forearm".
#severity of bow can be based on total percentage of possible damage done. so a d12 die rolling a 4 would be a glancing blow, but a 12 would be a "solid hit, the other character looks shaken"
#just put a bunch of phrases into a dictionary and based on percentage of damage of die grab the index value. so roll a d6 or d8, divide the roll by highest possible value, add descriptor for flavor
# 10: 'barely connected', 
# 20: 'the blow lands but didn't have much force'
# 30: 'you strike but not true, doing less damage than you had hoped. they are still bleeding though"
# 40: 'hey, there's some new red on them'
# 50: 'that hurt'
# 60: 'you hear things crack as the blow lands solidly'
# 70: 'by GAWD the man had a family'
# 80: 'if there was a crowd they would have gasped at the sound that made
# 90: 'you hit them as hard as you could, and they know it'
# 100: 'SHOOKETH'

#just goofin around with the above, not sure a dictionary / index is the right way to do this. 

Hey, here is a thought, could I bring in the madlib app????
# don't recreate the wheel, just run the attack description through the mad-lib app to spice it up

#meaning I would also need to tie in the madlib app, write the flavor wording however is easiest, and make it a 3 app party

Character model will have normal range of stats, class, and all relevant data from a standard character sheet
    #charModel:
    #hp: integer #represent hit points
    #name: string 
    #class: (fighter, wizard, cleric, druid, barbarian, bard, rogue, sorcerer, paladin) #gotta build each of these classes with any special rules like paladins getting smite, sorcerer spellslot limits, fighter combat shenanigans
    #available_actions: integer (most characters have one action and one bonus action per turn plus a free action)
    #wpn_dmg_dice: d2,d3,d4,d6,d8,d10,d12
    #wpn_modifiers: integer that interacts with wpn_dmg_dice
    #char_modifiers: blinded in one eye?
    #spell_slots: 1st:0,2nd:0,3rd:0,4th:0,5th:0,6th:0,7th:0,8th:0,9th:0 
    # spell slots are used to cast spells, no slots, no spells
    #special_actions: integer (some classes like fighter allow the use of additional dice, would use that here)
    #race: from char creation
    #height: for flavor?
    #size: (small, medium, large, giant, behemoth?) important for combat rules
    #mvmt_speed: (advanced goal is to figure out combat arena and movement)
    #armor_type: light, medium, heavy
    #armor_penalty: non_casting for casters in heavy plate for example
    #str_stat: int
    #con_stat: int
    #int_stat: int
    #wis_stat: int
    #char_stat: int
    #dex_stat: int
    #armor_Class: int
    #status: like prone, sickened, entangled, constricted, swallowed, poisoned etc this will be important for spell / fighting due to prone condition and fighter combat manuevers

    #stats will be set at character creation and stored in the character model

    #for combat the two character models will "attack" each other by rolling a d20
    
    #12 on the Die 

    #combat equation
    #attack_roll = d20_roll + str/dex mod + (offhand modifier if relevant)
    #damage will be applied to the models on a hit 
    #if attack_roll is higher than armor_Class then apply attack damage:

    #attack = str/dex mod + wpn_dmg_dice(modifiers go here)
    
    #charModel_fighter loses attack amount of hp

    NEED TO FLESH OUT:

    #action rules: since some characters can forego actions, take secondary actions, can have additional actions granted to them
    
    #armor_class rules: can simply ignore and only go on AC set dsuring character creation, but there are goofy rules that alter combat based on type of armore being worn
    
    #spellcasting rules: depending on what type of spellcaster the character is they get a different number of spell slots and can use them separately. 
    #those should go in the spellcaster classes as much as possible but some rules apply to all spellcaster generally
    
    spellcasting_equation = d20_roll + caster_class_mod + modifiers (spellcasting equation only used for "roll to hit spells")

    #class_models:

    paladin {
        #spellslots like cleric, similar spell selection list
        #need domains
        #smite equation should go here, only allow smiting from within the class #(remember they get to pick whether to smite after the die is rolled but not before the hit is known .... right? double check)
        #requires spell focus
    }

    cleric {
        #unique class feature all spells immediately available, just gotta pick them each combat #in game its one prayer session per day I think
        #requires spell focus
    }    

    fighter {
        #fighter pretty much just whack stuff until they get combat manuevers and secondary actions
        #secondary action rules go here
        #combat manuevers
        #dual wielding?
        #offhand rules?
    }

    barbarian {
        rage rules
        reckless attack rules need to go here, using it gives opportunity on all attacks against you for the round
        #dual handing rules? is that a class specific thing?
        #dex vs str thing dont forget #barbarians can pick str or dex as their weapon stat, so there are dex barbarian builds. I think this is not a unique class feature. pretty sure fighters have this to.
    }

    wizard{
        #spell stuff is a stretch goal, there are so many effects spells can have, and a lot depend on area being a thing
        #meaning I need a battlegroung and spacing to really show spells correctly
        #thankfully most of the combat casters just use their spell slots as extra damage on hits
    }

    sorcerer {
        #gotta be honest, I know like nothing about sorcs
        #gotta learn the rules
    }

    rogue{
        #sneak attack rules
        #hidden status can be a modifier
        #technically a hidden character has a 50/50 shot of being hit even on a successful attack roll, so that will complicate things
        #an observed character can't hide, and this is single combat at least to start
        #hiding rules are a stretch goal! lol 
    }