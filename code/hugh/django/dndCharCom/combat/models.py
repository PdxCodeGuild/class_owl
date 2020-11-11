from os import O_TRUNC
from django.db import models
from django.db.models.enums import IntegerChoices
from django.db.models.fields import DecimalField

# Create your models here.

#dndCharCom is meant to recreate tabletop RPG combat including random dice rolls by click.

#Character model will have normal range of stats

class Char_Model(models.Model):
    name = models.CharField(max_length=24)
    background = models.CharField()
    available_actions = models.IntegerField(default=1)
    #author = username if i were supporting multiple users
    hp = models.IntegerField(default=1)
    wpn_dmg_dice = models.IntegerField(default=???) #need to figure out what to multipy dice by.
    #a d4 is literally 1 thru 4 all equally likely, but weapon damage is fixed. so a javeline
    #always does d6 damage + other stuff
    #should I just have a weapons list?
    #to make this work at first I could let the user set it, then later on build the weapon library
    #and have the user pick from the dropdown of weapons, then apply the correct damage
    modifiers = models.Integer()
    spell_slots = class sorcerer{spell_slots}



    charModel:
    hp: integer (represent hit points)
    name: string
    available_actions: integer (most characters have one action and one bonus action per turn plus a free action)
    wpn_dmg_dice: d2,d3,d4,d6,d8,d10,d12
    modifiers: integer that interacts with wpn_dmg_dice
    spell_slots: 1st:0,2nd:0,3rd:0,4th:0,5th:0,6th:0,7th:0,8th:0,9th:0 
    # spell slots are used to cast spells, no slots, no spells
    special_actions: integer (some classes like fighter allow the use of additional dice, would use that here)
    race: from char creation
    height: for flavor?
    size: (small, medium, large, giant, behemoth?) important for combat rules
    mvmt_speed: (advanced goal is to figure out combat arena and movement)
    armor_type: light, medium, heavy
    armor_penalty: non_casting for casters in heavy plate for example
    str_stat: int
    con_stat: int
    int_stat: int
    wis_stat: int
    char_stat: int
    dex_stat: int
    armor_Class: int
    status: this will be important for spell / fighting due to prone condition and fighter combat manuevers

    #stats will be set at character creation and stored in the character model

    #for combat the two character models will "attack" each other by rolling a d20
    
    #12 on the Die 

    #combat equation
    attack_roll = d20_roll + str/dex mod + (offhand modifier if relevant)
    #damage will be applied to the models on a hit 
    if attack_roll is higher than armor_Class then apply attack damage:

    attack = str/dex mod + wpn_dmg_dice(modifiers go here)
    
    charModel_fighter loses attack amount of hp

    NEED TO FLESH OUT:

    action rules: since some characters can forego actions, take secondary actions, can have additional actions granted to them
    
    armor_class rules: can simply ignore and only go on AC set dsuring character creation, but there are goofy rules that alter combat
    
    spellcasting rules: depending on what type of spellcaster the character is they get a different number of spell slots and can use them separately. 
    those should go in the spellcaster classes as much as possible but some rules apply to all spellcaster generally
    spellcasting_equation = d20_roll + caster_class_mod + modifiers (spellcasting equation only used for "roll to hit spells")

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

    class fighter {
        #fighter pretty much just whack stuff until they get combat manuevers and secondary actions
        #secondary action rules go here
        #combat manuevers
        #dual wielding?
        #offhand rules?
    }

    class barbarian {
        rage rules
        reckless attack rules need to go here, using it gives opportunity on all attacks against you for the round
        #dual handing rules? is that a class specific thing?
        #dex vs str thing dont forget #barbarians can pick str or dex as their weapon stat, so there are dex barbarian builds. I think this is not a unique class feature. pretty sure fighters have this to.
    }

    class wizard{
        #spell stuff is a stretch goal, there are so many effects spells can have, and a lot depend on area being a thing
        #meaning I need a battlegroung and spacing to really show spells correctly
        #thankfully most of the combat casters just use their spell slots as extra damage on hits
    }

    class sorcerer {
        spell_slots = 2
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