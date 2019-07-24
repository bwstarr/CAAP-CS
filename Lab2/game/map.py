# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter, 
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'Room' : S.Room(),
				'Elevator' : S.Elevator(),   #this connects names to scenes
				'Extra_lock' : S.Extra_lock(),
				'text' : S.text(),
				'Friend_solo' : S.Friend_solo(),
				'Reentry_solo' : S.Reentry_solo(),
				'Reentry_friend_good_txt' : S.Reentry_friend_good_txt(),
				'Reentry_friend_bad_txt' : S.Reentry_friend_bad_txt(),
				'death' : Death()
				# raise ValueError ('todo')
				}
	
	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene    #self is the variabel
	
	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)