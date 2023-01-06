(define (domain firefighting_drone)
(:requirements  :strips :typing :adl :fluents  :conditional-effects :equality)
(:types drone waypoint camera gps)

(:predicates
	(at ?d - drone ?loc - waypoint)
	(can_fly ?d - drone ?loc_x - waypoint ?loc_y - waypoint) 
	(equipped_for_imaging ?d - drone ?c - camera)
	(equipped_for_gps_signal ?d - drone ?g - gps) 
    (have_image ?d - drone ?loc_x - waypoint )
	(communicated_image_data ?loc - waypoint )
	(raised_antenna ?d - drone)
	(antenna_retracted ?d - drone)
	(have_GPS_pos ?d - drone ?loc_y - waypoint )
	(communicated_GPS_pos ?loc_y - waypoint )
	(at_flight_altitude ?d - drone)
	(at_docking_station ?d - drone ?loc - waypoint)
	(focused ?d - drone ?c - camera ?loc - waypoint)
	(rechargeable ?d - drone)
)

(:functions
(battery_level ?d - drone)
(battery_cost ?loc_x - waypoint ?loc_y - waypoint)
(total_cost) - number
)

(:action take_off
:parameters ( ?d - drone ?loc - waypoint )
 	:precondition
		(and (at_docking_station ?d ?loc)
		(antenna_retracted ?d)
		)
 	:effect
		(and (at_flight_altitude ?d)
		(not(at_docking_station ?d ?loc))
		(not (rechargeable ?d))
		)	
)

(:action land
	:parameters (?d - drone ?loc - waypoint)
	:precondition (and (at_flight_altitude ?d)
	(antenna_retracted ?d))
	:effect (and (at_docking_station ?d ?loc)
	(not (at_flight_altitude ?d))
	(rechargeable ?d))
)

(:action navigate
 	:parameters ( ?d - drone ?loc_x - waypoint ?loc_y - waypoint)
	:precondition 	(and 
        (can_fly ?d ?loc_x ?loc_y)  
        (at ?d ?loc_x)
        (at_flight_altitude ?d)
        (antenna_retracted ?d)
        (> (battery_level ?d) (battery_cost ?loc_x ?loc_y)))			
	:effect
	    (and 
	    (at ?d ?loc_y) 
	   	(not (at ?d ?loc_x))
	   	(decrease (battery_level ?d) (battery_cost ?loc_x ?loc_y))
	   	(increase (total_cost) (battery_cost ?loc_x ?loc_y))
	   	)	
)

(:action recharge
	:parameters (?d - drone ?loc_z - waypoint ?loc_w - waypoint)
	:precondition (and (<= (battery_level ?d) (battery_cost ?loc_z ?loc_w))
		(at_docking_station ?d ?loc_z)
		(rechargeable ?d)
		(at ?d ?loc_z)
		)
	:effect (and (assign (battery_level ?d) 100))
)
			
(:action focus_camera
	:parameters ( ?d - drone ?loc_y - waypoint ?c - camera)
 	:precondition
		(and (at ?d ?loc_y) 
		(at_flight_altitude ?d) 
		(equipped_for_imaging ?d ?c))
 	:effect
		(and (focused ?d ?c ?loc_y ) 
		)	
)


(:action take_image
 	:parameters ( ?d - drone ?loc_y - waypoint ?c - camera)
 	:precondition (and  
		(at ?d ?loc_y) 
		(focused ?d ?c ?loc_y))
 	:effect
		(and (have_image ?d ?loc_y ) 
		(not (focused ?d ?c ?loc_y )))
)


(:action communicate_image_data
 	:parameters ( ?d - drone  ?loc_y - waypoint )
 	:precondition 
		(and (at ?d ?loc_y)  
		(have_image ?d ?loc_y )
		(raised_antenna ?d)
		 )
 	:effect
		(and (communicated_image_data ?loc_y )
		(not (have_image ?d ?loc_y )))
)
		

(:action raise_antenna
	:parameters (?d - drone ?g - gps ?loc_y - waypoint)
	:precondition (and  
	(at ?d ?loc_y) 
	(at_flight_altitude ?d))
	:effect (and 
	(raised_antenna ?d)
	(not (antenna_retracted ?d))
	)
)


(:action retract_antenna
	:parameters (?d - drone ?g - gps ?loc_y - waypoint)
	:precondition (and (raised_antenna ?d)
	(at ?d ?loc_y))
	:effect (and 
	(antenna_retracted ?d)
	(not (raised_antenna ?d))
	)
)


(:action get_GPS_pos
 :parameters ( ?d - drone ?loc_y - waypoint ?g - gps )
 :precondition (and
	(equipped_for_gps_signal ?d ?g) 
	(at ?d ?loc_y) 
	(at_flight_altitude ?d)
	(raised_antenna ?d))
 :effect
	(and (have_GPS_pos ?d ?loc_y))
)

(:action communicate_GPS_pos
 :parameters ( ?d - drone  ?loc_y - waypoint )
 :precondition (and
	(at ?d ?loc_y)   
	(have_GPS_pos ?d ?loc_y )
	(raised_antenna ?d))
 :effect
	(and  (communicated_GPS_pos ?loc_y ) 
	(not (have_GPS_pos ?d ?loc_y)))
)
)







