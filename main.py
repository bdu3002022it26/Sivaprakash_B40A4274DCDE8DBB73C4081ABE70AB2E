'''Implement a class called player that represents a cricket player.the player class should have a
method called play() which prints"the player is playing cricket.Derive two classes,batsman and
Bowler,from the player class override the play() method in each derived class to print "the batsman
is batting and the bowler is bowling", respectively write a program to create objects of both the 
Batsman and Bowler classes and call the play() method for each object.'''


# define the base class Player
class Player:
  def play(self):
    print("the Player is playing.")
    
# define the derived class Batsman
class Batsman(Player):
 def play(self):
   print("the Batsman is batting.")

#define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("the Bowler is bowling.")
    
# create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()