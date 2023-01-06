(define (problem drone_2) (:domain firefighting_drone)
(:objects
	drone1 drone2 drone3 - drone
	loc_base loc_2 loc_3 loc_4 loc_5 loc_6 loc_7 loc_8 loc_9 loc_10 loc_11 loc_12 loc_13 - waypoint
	camera1 camera2 camera3 - camera
	gps1 gps2 gps3 - gps
)
(:init 
	(= (total_cost) 0)
	(= (battery_level drone1) 80)
	(= (battery_level drone2) 90)
	(= (battery_level drone3) 70)

	(= (battery_cost loc_base loc_2) 60)  
	(= (battery_cost loc_2 loc_3) 30)
	(= (battery_cost loc_2 loc_4) 40)
	(= (battery_cost loc_3 loc_4) 20)
	(= (battery_cost loc_3 loc_5) 20)
	(= (battery_cost loc_4 loc_5) 10)
	(= (battery_cost loc_4 loc_6) 30)
	(= (battery_cost loc_5 loc_6) 20)
	(= (battery_cost loc_5 loc_7) 10)
	(= (battery_cost loc_6 loc_7) 40)
	(= (battery_cost loc_6 loc_8) 10)
	(= (battery_cost loc_7 loc_9) 20)
	(= (battery_cost loc_7 loc_8) 20)
	(= (battery_cost loc_8 loc_9) 30)
	(= (battery_cost loc_8 loc_10) 70)
	(= (battery_cost loc_9 loc_10) 60)
	(= (battery_cost loc_9 loc_12) 40)
	(= (battery_cost loc_10 loc_11) 30)
	(= (battery_cost loc_10 loc_12) 30)
	(= (battery_cost loc_11 loc_12) 10)
	(= (battery_cost loc_12 loc_13) 40)

	(at drone1 loc_base)
	(at drone2 loc_2)
	(at drone3 loc_3)

	(equipped_for_imaging drone1 camera1)
	(equipped_for_gps_signal drone1 gps1)
	(antenna_retracted drone1)
	(at_docking_station drone1 loc_base)
	(rechargeable drone1)

	(equipped_for_imaging drone2 camera2)
	(equipped_for_gps_signal drone2 gps2)
	(antenna_retracted drone2)
	(at_docking_station drone2 loc_4)
	(rechargeable drone2)

	(equipped_for_imaging drone3 camera3)
	(not (equipped_for_gps_signal drone3 gps3))
	(antenna_retracted drone3)
	(at_docking_station drone3 loc_3)
	(rechargeable drone3)

	(can_fly drone1 loc_base loc_2)
	(can_fly drone1 loc_2 loc_base)
	(can_fly drone1 loc_2 loc_3)
	(can_fly drone1 loc_3 loc_2)
	(can_fly drone1 loc_3 loc_4)
	(can_fly drone1 loc_4 loc_3)
	(can_fly drone1 loc_4 loc_5)
	(can_fly drone1 loc_3 loc_5)
	(can_fly drone1 loc_5 loc_6)
	(can_fly drone1 loc_6 loc_8)
	(can_fly drone1 loc_8 loc_9)

	(can_fly drone2 loc_2 loc_4)
	(can_fly drone2 loc_4 loc_5)	
	(can_fly drone2 loc_5 loc_6)	
	(can_fly drone2 loc_5 loc_7)	
	(can_fly drone2 loc_7 loc_8)	
	(can_fly drone2 loc_8 loc_10)	
	(can_fly drone2 loc_10 loc_12)

	(can_fly drone3 loc_3 loc_5)
	(can_fly drone3 loc_5 loc_6)
	(can_fly drone3 loc_6 loc_7)
	(can_fly drone3 loc_7 loc_9)
	(can_fly drone3 loc_9 loc_12)
	(can_fly drone3 loc_12 loc_13)
)

(:goal 
	(and
	(communicated_image_data loc_8)
	(communicated_image_data loc_10)		
	(communicated_image_data loc_13)
	(communicated_GPS_pos loc_5)
	(communicated_GPS_pos loc_9)
	)
)

(:metric minimize (total_cost))

)