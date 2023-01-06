(define (problem drone_1) (:domain firefighting_drone)
(:objects
	drone1 - drone
	loc_base loc_2 loc_3 loc_4 loc_5 - waypoint
	camera1 - camera
	gps1 - gps
)
(:init 
	(= (total_cost) 0)
	(= (battery_level drone1) 80)
	(= (battery_cost loc_base loc_2) 60)  
	(= (battery_cost loc_2 loc_base) 60)
	(= (battery_cost loc_2 loc_3) 30)
	(= (battery_cost loc_3 loc_4) 20)
	(= (battery_cost loc_4 loc_5) 10)
	(= (battery_cost loc_3 loc_5) 20)

	(at drone1 loc_base)
	(equipped_for_imaging drone1 camera1)
	(equipped_for_gps_signal drone1 gps1)
	(antenna_retracted drone1)
	(at_docking_station drone1 loc_base)
	(rechargeable drone1)

	(can_fly drone1 loc_base loc_2)
	(can_fly drone1 loc_2 loc_base)
	(can_fly drone1 loc_2 loc_3)
	(can_fly drone1 loc_3 loc_2)
	(can_fly drone1 loc_3 loc_4)
	(can_fly drone1 loc_4 loc_3)
	(can_fly drone1 loc_4 loc_5)
	(can_fly drone1 loc_3 loc_5)
)

(:goal 
	(and
	(communicated_image_data loc_5 )
	(communicated_GPS_pos loc_2)
	)
)

(:metric minimize (total_cost))

)