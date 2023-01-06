# Plan found with metric 1100
# Theoretical reachable cost 1100
# States evaluated so far: 22
# States pruned based on pre-heuristic cost lower bound: 0
# Time 5



waypoints = {"loc_base": [10,10], "loc_2" :[15,15] ,"loc_3":[5,17], "loc_4":[25,20], "loc_5":[30,22],
"loc_6":[30,30],"loc_7":[3,34],"loc_8":[25,39],"loc_9":[9,38],
"loc_10":[5,42],"loc_11":[15,44],"loc_12":[24,43],"loc_13":[35,45]}

drones = {"drone1":waypoints["loc_base"], "drone2":waypoints["loc_2"], "drone3":waypoints["loc_3"]}

costs = {"loc_base loc_2" :60, "loc_2 loc_3": 30,"loc_2 loc_4": 40,"loc_3 loc_4": 20,"loc_4 loc_5": 10,
"loc_3 loc_5": 20, "loc_4 loc_6": 30, "loc_5 loc_6":20,"loc_5 loc_7":10,"loc_6 loc_7":40,
"loc_7 loc_9":20,"loc_7 loc_8":20,"loc_6 loc_8":10,"loc_8 loc_9":30,"loc_9 loc_12":40,"loc_9 loc_10":60,"loc_8 loc_10":70,
"loc_10 loc_11":30,"loc_10 loc_12":30,"loc_11 loc_12":10,"loc_12 loc_13":40}

initial_battery ={"drone1":80, "drone2":90, "drone3":70}

target = {"drone1":waypoints["loc_8"], "drone2":waypoints["loc_10"], "drone3":waypoints["loc_13"]}


plan = {
1:"take_off drone3 loc_3",
2:"take_off drone2 loc_4",
3:"take_off drone1 loc_base",
4:"navigate drone3 loc_3 loc_5",
5:"navigate drone2 loc_2 loc_4",
6:"navigate drone1 loc_base loc_2",
7:"navigate drone2 loc_4 loc_5",
8:"land drone1 loc_2",
9:"navigate drone3 loc_5 loc_6",
10:"navigate drone2 loc_5 loc_7",
11:"recharge drone1 loc_2 loc_3",
12:"land drone3 loc_6",
13:"land drone2 loc_8",
14:"take_off drone1 loc_2",
15:"recharge drone3 loc_6 loc_7",
16:"navigate drone1 loc_2 loc_3",
17:"take_off drone2 loc_8",
18:"take_off drone3 loc_6",
19:"navigate drone1 loc_3 loc_5",
20:"navigate drone2 loc_7 loc_8",
21:"navigate drone3 loc_6 loc_7",
22:"raise_antenna drone1 gps1 loc_5",
23:"land drone2 loc_8",
24:"navigate drone3 loc_7 loc_9",
25:"get_gps_pos drone1 loc_5 gps1",
26:"recharge drone2 loc_8 loc_10",
27:"land drone3 loc_9",
28:"communicate_gps_pos drone1 loc_5",
29:"take_off drone2 loc_8",
30:"recharge drone3 loc_9 loc_10",
31:"focus_camera drone2 loc_8 camera2",
32:"raise_antenna drone2 gps1 loc_8",
33:"take_off drone3 loc_9",
34:"retract_antenna drone1 gps1 loc_5",
35:"take_image drone2 loc_8 camera2",
36:"navigate drone3 loc_9 loc_12",
37:"navigate drone1 loc_5 loc_6",
38:"communicate_image_data drone2 loc_8",
39:"navigate drone3 loc_12 loc_13",
40:"land drone1 loc_6",
41:"retract_antenna drone2 gps1 loc_8",
42:"focus_camera drone3 loc_13 camera3",
43:"recharge drone1 loc_6 loc_7",
44:"raise_antenna drone3 gps1 loc_13",
45:"take_image drone3 loc_13 camera3",
46:"navigate drone2 loc_8 loc_10",
47:"take_off drone1 loc_6",
48:"focus_camera drone2 loc_10 camera2",
49:"communicate_image_data drone3 loc_13",
50:"navigate drone1 loc_6 loc_8",
51:"raise_antenna drone2 gps1 loc_10",
52:"take_image drone2 loc_10 camera2",
53:"navigate drone1 loc_8 loc_9",
54:"communicate_image_data drone2 loc_10",
55:"raise_antenna drone1 gps1 loc_9",
56:"get_gps_pos drone1 loc_9 gps1",
57:"communicate_gps_pos drone1 loc_9"  
}