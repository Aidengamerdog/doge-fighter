import random
from enum import Enum

class MoveType(Enum):
    PHYSICAL = "physical"
    SPECIAL = "special"
    STATUS = "status"

class DogeMove:
    def __init__(self, name, move_type, power, accuracy, pp, description):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.max_pp = pp
        self.description = description
    
    def use(self):
        """Use one PP"""
        if self.pp > 0:
            self.pp -= 1
            return True
        return False
    
    def restore_pp(self):
        """Restore PP to max"""
        self.pp = self.max_pp
    
    def __str__(self):
        return f"{self.name} (Power: {self.power}, Accuracy: {self.accuracy}%, PP: {self.pp}/{self.max_pp})"

class Doge:
    def __init__(self, name="Much Doge", level=1):
        self.name = name
        self.level = level
        self.max_hp = 100 + (level * 5)
        self.hp = self.max_hp
        self.attack = 50 + (level * 3)
        self.defense = 45 + (level * 2)
        self.sp_attack = 55 + (level * 3)
        self.sp_defense = 50 + (level * 2)
        self.speed = 60 + (level * 4)
        self.exp = 0
        self.status = None  # "burned", "poisoned", "paralyzed", etc.
        
        # Initialize Doge's custom moves
        self.moves = [
            self.wow_blast(),
            self.such_speed(),
            self.doge_shield(),
            self.meme_strike()
        ]
    
    def wow_blast(self):
        """Much wow! A powerful special attack"""
        return DogeMove(
            name="Wow Blast",
            move_type=MoveType.SPECIAL,
            power=75,
            accuracy=100,
            pp=15,
            description="Much wow! Doge fires a powerful blast of pure meme energy!"
        )
    
    def such_speed(self):
        """Such speed! Increases Doge's speed drastically"""
        return DogeMove(
            name="Such Speed",
            move_type=MoveType.STATUS,
            power=0,
            accuracy=100,
            pp=20,
            description="Doge moves so fast, the opponent can't keep up! Speed greatly increased!"
        )
    
    def doge_shield(self):
        """Much defense! A protective move"""
        return DogeMove(
            name="Doge Shield",
            move_type=MoveType.STATUS,
            power=0,
            accuracy=100,
            pp=15,
            description="Doge creates a protective barrier of doge wisdom!"
        )
    
    def meme_strike(self):
        """So meme! A physical attack infused with meme power"""
        return DogeMove(
            name="Meme Strike",
            move_type=MoveType.PHYSICAL,
            power=90,
            accuracy=95,
            pp=10,
            description="So meme! Doge channels the power of ancient internet memes!"
        )
    
    def take_damage(self, damage):
        """Take damage and return remaining HP"""
        self.hp = max(0, self.hp - damage)
        return self.hp
    
    def heal(self, amount):
        """Heal Doge"""
        self.hp = min(self.max_hp, self.hp + amount)
    
    def is_fainted(self):
        """Check if Doge has fainted"""
        return self.hp <= 0
    
    def gain_exp(self, amount):
        """Gain experience points"""
        self.exp += amount
        if self.exp >= 100 * self.level:
            self.level_up()
    
    def level_up(self):
        """Level up and increase stats"""
        self.level += 1
        self.exp = 0
        self.max_hp += 5
        self.hp = self.max_hp
        self.attack += 3
        self.defense += 2
        self.sp_attack += 3
        self.sp_defense += 2
        self.speed += 4
        print(f"\n🐕 {self.name} leveled up to level {self.level}!")
        print(f"   All stats increased! HP: {self.max_hp}, ATK: {self.attack}, SPD: {self.speed}")
    
    def get_status(self):
        """Return formatted status"""
        return f"""
╔════════════════════════════════════════╗
║          {self.name.upper()} - LEVEL {self.level}           ║
╠════════════════════════════════════════╣
║ HP:  {self.hp}/{self.max_hp}
║ ATK: {self.attack}  |  DEF: {self.defense}
║ SP.ATK: {self.sp_attack}  |  SP.DEF: {self.sp_defense}
║ SPD: {self.speed}
╚════════════════════════════════════════╝
        """
    
    def get_moves_list(self):
        """Return formatted moves list"""
        moves_str = f"\n{self.name}'s Moves:\n"
        for i, move in enumerate(self.moves, 1):
            moves_str += f"{i}. {move}\n"
        return moves_str
    
    def __str__(self):
        return f"{self.name} (Lv. {self.level}) - HP: {self.hp}/{self.max_hp}"
