# Plan found with metric 110.000
# Theoretical reachable cost 110.000
# States evaluated so far: 22
# States pruned based on pre-heuristic cost lower bound: 0
# Time 0.05


drones = {"drone1":[10,10]}
waypoints = {"loc_base": [10,10], "loc_2" :[15,20] ,"loc_3":[27,23], "loc_4":[17,28], "loc_5":[12,35]}
costs = {"loc_base loc_2" :60,"loc_2 loc_3":30,"loc_3 loc_4": 20, "loc_4 loc_5":10 ,"loc_3 loc_5": 20 }
initial_battery ={"drone1":80}
target = {"drone1":[12, 35]}

plan = {
1:"take_off drone1 loc_base",
2:"navigate drone1 loc_base loc_2",
3:"land drone1 loc_2",
4:"recharge drone1 loc_2 loc_3",
5:"take_off drone1 loc_2",
6:"raise_antenna drone1 gps1 loc_2",
7:"get_gps_pos drone1 loc_2 gps1",
8:"communicate_gps_pos drone1 loc_2",
9:"retract_antenna drone1 gps1 loc_2",
10:"navigate drone1 loc_2 loc_3",
11:"navigate drone1 loc_3 loc_5",
12:"focus_camera drone1 loc_5 camera1",
13:"take_image drone1 loc_5 camera1",
14:"raise_antenna drone1 gps1 loc_5",
15:"communicate_image_data drone1 loc_5",
}

