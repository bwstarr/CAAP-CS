# imports random madule form library
from random import randint

suspect = 0
# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):
	
	

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class Room(Scene):
	
	name = 'Room'

	def enter(self):
		print ("You are about to embark on your journey for peanut butter. But first, you must leave.") 
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		print ("1.) Go down the elevator | 2.) Go Down the Stairs | 3.) Repel out your Dorm window")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You meet your RA in the elevator.")     
			return self.exit_scene('Elevator') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Smart, you miss everyone. Smooth brah.")
			return self.exit_scene('Friend_solo') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("As you repel down the side of north, you realize your inability. You fall to your death, being caught in the process.")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Elevator(Scene):
	
	name = 'Elevator'
	global suspect

	def enter(self):
		print ("You realize the danger of your situation. Somehow, you must escape without suspicion.") 
		return self.action()
		
		
	def action(self):
		global suspect
		print ("What will you do?")
		print ("1.) Come up with an excuse | 2.) Remain Silent | 3.) Ask them if they would like to join ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("As you fumble upon your words, you somehow convince them that you are about to work on your foolsball skills.")        #the actions lead to different scenes
			return self.exit_scene('Friend_solo') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("As you stand there awkwardly, your RA starts to wonder about your intentions. Hope this doesn't screw you over.")
			suspect += 1 
			return self.exit_scene('Friend_solo') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("As you talk, your RA takes a hold of your arm. You aren't goin anywhere partner.")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Extra_lock(Scene):
	
	name = 'Extra_lock'

	def enter(self):
		print("You suddenly get a text from roommate, and you realize your room is occupied at the moment...")
		return self.action()

	def action(self):
		print ("What do you do?")
		print("1. Sleep on the dorm sofa | 2. Text Branson | 3. Go to your room anyway")
		choice = input("> ")
		correct = 418

		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)
		   
		if choice == 1:
			print ("You decide to hunker down on the sofa, and call it night. Before you wake up, a starving college student steals your pb for a midnight snack. You have failed your mission")
			return self.exit_scene('death')
		elif choice == 2:
			print ("You text the coolest person you know, and ask if you can crash for the night. The God, in his infinte patience and wisdom, says 'Of course brah, just come on in'" )
			try_f = input("What room do you go to?")
			if try_f == ':q':
				return self.exit_scene(try_f)
			elif try_f == "418":
				print ("You make it to Branson's room, in which your peanut butter is blessed by his presence. Good job trooper.")
				return self.exit_scene('finished')
			else:
				print ("You enter into the wrong room! The person inside is extremely upset that you interupted their 1 am reading, and complain to the RA. You're screwed.")
				return self.exit_scene('death')
		elif choice == 3:
			print("You enter into your room, and see a sight which curses your eyes for all of eternity. You broke the bro code, mission failed.")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
		
class text(Scene):
	
	name = 'text'
	global suspect

	def enter(self):
		print ("While your are searching for PB with your BFF, you suddenly get a text from your RA: 'Where are you?'") 
		return self.action()
		
		
	def action(self):
		global suspect
		print ("What will you do?")
		print("1.) Change The subject | 2.) Tell a white lie | 3.) Tell a black lie")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You respond with 'What are you doing?'. The RA quickly catches on and responds with 'Just hanging outside of the dorm. Star gazing...'. Mission Failed partner.")        #the actions lead to different scenes
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("You respond with 'studying'. An adequte Uchicago reply, but a vanila one for sure. Your RA may be cathcing on...")
			if suspect == 1:
				pointless=eval(input("How many mintues does it take you to get back?"))
				print("You get back to the dorm. It's too late. Cathcing on from the awkard elevator talk, your RA has been able to conncect the dots from your text. Looks like your screwed...")
				return self.exit_scene('death')
			else:
				return self.exit_scene('Reentry_friend_bad_txt') 

		elif int(choice) == 3:
			print ("Saying the first outlandish thing that comes to your mind, you claim that you and your friend are having a staring contest while shirtless in a handstand. Bewildered by the response, the RA responds with 'K lol', and doesn't consider how you sent a text while upsidedown.")
			return self.exit_scene('Reentry_friend_good_txt') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	
class Friend_solo(Scene):
	
	name = 'Friend_solo'

	def enter(self):
		print ("As you leave the lobby, you bump into one of your buddies") 
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		print ("1.) Ignore them | 2.) Ask them to join you | 3.) Do a Handstand")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Being more concerned with your precious peanut butter, you leave your friend in the dust")        #the actions lead to different scenes
			return self.exit_scene('Reentry_solo') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Your friend agrees to come, as long as you buy them some PB as well")
			return self.exit_scene('text') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Trying to advance from the friend zone, you attempt a Handstand. You over swing, landing on your head. Your friend leaves you, and you are discovered unconcious the next morning")
			return self.exit_scene('death') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	
class Reentry_solo(Scene):
	
	name = 'Reentry_solo'
	global suspect

	def enter(self):
		print ("You make it make to your dorm, peaunut butter in hand. Here is your last test: how do you get back in uncaught?") 
		return self.action()
		
		
	def action(self):
		global suspect
		print ("What will you do?")
		print("1.) Attempt to slip in. | 2.) Try to create a distraction | 3.) Tap in and hope for the best ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Realizing the folly in signing in, you try to slip in. However, as you try to sneak by the recptionist catches you. Your RA is called as a matter of course, and you're screwed.")        #the actions lead to different scenes
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Setting your phone in a corner, you set a firealarm recording to blare in 30 sec. In the ensuing confusion, you slip in. You may have lost your phone, but you have successfully attained your pb. Good work soldier!")
			return self.exit_scene('finished') # raise ValueError ('todo')
		elif int(choice) == 3:
			if suspect >= 1:
				print ("Yoy both tap in, make it to your rooms, and enjoy your pb. However, your ill-formed txt causes the RA to check the nightly records... You're scrwed.")
				return self.exit_scene('death') 
			else:
				print("You tap in, and make it to the elevator")
				return self.exit_scene('Extra_lock')# raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	
class Reentry_friend_good_txt(Scene):
	
	name = 'Reentry_friend_good_txt'
	global suspect
	def enter(self):
		print ("You make it make to your dorm, peaunut butter in hand. Here is your last test: how do you get back in uncaught?") 
		return self.action()
		
		
	def action(self):
		global suspect
		print ("What will you do?")
		print("1.) Attempt to slip while your friend signs in. | 2.) Try to create a distraction with your friend | 3.) Tap in and hope for the best ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			if suspect == 0:
				print ("Realizing the folly in signing in, you slip by while your friend does so. Although your friend is screwed, you have attained your pb uncaught. Good job Soldier!")        #the actions lead to different scenes
				return self.exit_scene('finished')
			else:
				print("You slip by successfully, but to your dismay the RA waiting at the enterance. That damn elevator talk...")
				return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Setting your phone in a corner, you set a firealarm recording to blare in 30 sec. In the ensuing confusion, both of you slip in. You may have lost your phone, but you have successfully attained your pb. Good work soldier!")
			return self.exit_scene('finished') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("You both tap in, and make it to the elevator")
			return self.exit_scene('Extra_lock') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	
class Reentry_friend_bad_txt(Scene):
	
	name = 'Reentry_friend_bad_txt'

	def enter(self):
		print ("You make it make to your dorm, peaunut butter in hand. Here is your last test: how do you get back in uncaught?") 
		return self.action()
		
		
	def action(self):
		print ("What will you do?")
		print("1.) Attempt to slip while your friend signs in. | 2.) Try to create a distraction with your friend | 3.) Tap in and hope for the best ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Realizing the folly in signing in, you slip by while your friend does so. However, on your way up to your room, you meet a suspicous RA by the lobby. You've been caught.")        #the actions lead to different scenes
			return self.exit_scene('death') # raise ValueError ('todo')
		elif int(choice) == 2:
			print ("Setting your phone in a corner, you set a firealarm recording to blare in 30 sec. In the ensuing confusion, both of you slip in. You may have lost your phone, but you have successfully attained your pb. Good work soldier!")
			return self.exit_scene('finished') # raise ValueError ('todo')
		elif int(choice) == 3:
			print ("Yoy both tap in, make it to your rooms, and enjoy your pb. However, your ill-formed txt causes the RA to check the nightly records... You're scrwed.")
			return self.exit_scene('laser_weapon_armory') # raise ValueError ('todo')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	