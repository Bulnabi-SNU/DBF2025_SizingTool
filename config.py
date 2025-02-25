from src.internal_dataclass import *
from src.setup_dataclass import *

def get_config():
    presetValues = PresetValues(
        m_x1 = 200,                             # g
        x1_time_margin = 10,                    # sec
        
        throttle_takeoff = 0.9,                 # 0~1
        max_climb_angle = 40,                   # deg
        max_load = 30,                          # kg
        h_flap_transition = 5,                  # m
        
        number_of_motor = 2,                 
        min_battery_voltage = 21.8,             # V 
        score_weight_ratio = 0.5                # mission2/3 score weight ratio (0~1)
        )
    
    propulsionSpecs = PropulsionSpecs(
        M2_propeller_data_path = "data/propDataCSV/PER3_8x6E.csv",
        M3_propeller_data_path = "data/propDataCSV/PER3_8x6E.csv",
        battery_data_path = "data/batteryDataCSV/Maxamps_2250mAh_6S.csv",
        Kv = 109.91,                            # (rad/s) / V
        R = 0.062,                              # Ohm
        number_of_battery = 2,
        n_cell = 6,
        battery_Wh = 49.95,                     # Wh
        max_current = 60,                       # A
        max_power = 1332                        # W
    )
    
    aircraftParamConstraints = AircraftParamConstraints (
  
        span_min = 1750.0,                      # mm
        span_max = 1750.0,                   
        span_interval = 25.0,
    
        AR_min = 4.50,                       
        AR_max = 4.50,
        AR_interval = 0.25,
        
        taper_min = 0.60,
        taper_max = 0.60,                      
        taper_interval = 0.05,
        
        twist_min = 2.0,                        # degree
        twist_max = 2.0,                     
        twist_interval = 1.0,
        
        #airfoil_list = ['sg6043','s9027','hq3011','e216','s4022']
        # airfoil_list = ['sg6043','s9027','hq3011','s4022']
        airfoil_list = ['e216']
        )
    
    aerodynamicSetup = AerodynamicSetup(
        alpha_start = -3,                       # degree
        alpha_end = 10,
        alpha_step = 1,
        fuselage_cross_section_area = 19427,    # mm2
        fuselage_Cd_datapath = "data/fuselageDragCSV/fuselageDragCoefficients.csv",
        AOA_stall = 13,                         # degree
        AOA_takeoff_max = 10,
        AOA_climb_max = 8,
        AOA_turn_max = 8  
    )

    baseAircraft = Aircraft(
        m_fuselage = 2500,
        wing_area_blocked_by_fuselage = 72640,  # mm2
        wing_density = 0.0000588,               # g/mm3

        mainwing_span = 1800,                   # mm
        mainwing_AR = 5.45,           
        mainwing_taper = 0.65,        
        mainwing_twist = 0.0,                   # degree
        mainwing_sweepback = 0,                 # degree
        mainwing_dihedral = 5.0,                # degree
        mainwing_incidence = 0.0,               # degree

        flap_start = [0.182, 0.402],            # spanwise ratio(0~1)
        flap_end = [0.335, 0.628],              # spanwise ratio(0~1)
        flap_angle = [20.0, 20.0],              # degree
        flap_c_ratio = [0.35, 0.35],            # chordwise ratio(0~1)

        horizontal_volume_ratio = 0.7,          
        horizontal_area_ratio = 0.25,           
        horizontal_AR = 4.0,                    
        horizontal_taper = 1,               
        horizontal_ThickChord = 8,              

        vertical_volume_ratio = 0.053,          
        vertical_taper = 0.6,        
        vertical_ThickChord = 9,  
        
        mainwing_airfoil_datapath = "data/airfoilDAT/sg6043.dat",
        horizontal_airfoil_datapath= "data/airfoilDAT/naca0008.dat",
        vertical_airfoil_datapath= "data/airfoilDAT/naca0009.dat"
        
        )

    missionParamConstraints = MissionParamConstraints (
                
                MTOW_min = 8.0,                     # Kg
                MTOW_max = 8.2,                  
                MTOW_analysis_interval = 0.2,
                
                M2_max_speed_min = 34,              # m/s
                M2_max_speed_max = 34,
                M3_max_speed_min = 24,
                M3_max_speed_max = 24,
                max_speed_analysis_interval = 2,    
                
                #Constraints for calculating mission2
                M2_climb_thrust_ratio_min = 0.9, 
                M2_climb_thrust_ratio_max = 0.9,
                M2_turn_thrust_ratio_min = 0.7,
                M2_turn_thrust_ratio_max = 0.7,
                M2_level_thrust_ratio_min = 0.9,
                M2_level_thrust_ratio_max = 0.9,
                M2_thrust_analysis_interval = 0.05,
    
                #Constraints for calculating mission3  
                M3_climb_thrust_ratio_min = 0.9,
                M3_climb_thrust_ratio_max = 0.9,
                M3_turn_thrust_ratio_min = 0.4,
                M3_turn_thrust_ratio_max = 0.4,
                M3_level_thrust_ratio_min = 0.5,
                M3_level_thrust_ratio_max = 0.5,
                M3_thrust_analysis_interval = 0.05,
                
                wing_loading_min = 5,               # kg/m2
                wing_loading_max = 15
                )
        

    return (presetValues, propulsionSpecs, aircraftParamConstraints, 
            aerodynamicSetup, baseAircraft, missionParamConstraints)