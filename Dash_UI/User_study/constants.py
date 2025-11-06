import os
import json

# --- Constants ---
GRID_WIDTH = 20
GRID_HEIGHT = 20
UPDATE_INTERVAL_MS = 1000
SLOW_INTERVAL_MS = 2000
CLICK_POLL_INTERVAL_MS = 100 

# --- Constants for participant counting ---
PARTICIPANT_COUNT_FILE = 'study_data/participant_count.txt'
PARTICIPANT_COUNT_LOCK = 'study_data/participant_count.lock'
# -----------------------------------------------

THRESHOLD_VALUES = {
    'with_framework': {1: 5, 2: 12, 3: 15, 4: 9, 5: 10, 6: 11},
    'without_framework': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
}

SCENARIO_CONFIG = {
    1: {'total_time': 332.0, 'total_steps': 236},
    2: {'total_time': 307.0, 'total_steps': 212},
    3: {'total_time': 362.0, 'total_steps': 417},
    4: {'total_time': 358.0, 'total_steps': 373},
    5: {'total_time': 363.0, 'total_steps': 399},
    6: {'total_time': 398.0, 'total_steps': 441}
}

PAUSE_POINTS = {
    1: [10, 160, 220],
    2: [10, 100, 140],
    3: [10, 120, 170],
    4: [10, 100, 150],
    5: [10, 140, 190],
    6: [10, 130, 180]
}

# --- 24-COMBINATION STUDY DESIGN ---
STUDY_DESIGN_TABLE = [
    # C01-C04: Board (E1, E2) using Seq1-Seq4
    [(1, 1), (2, 0), (3, 3), (4, 2)],  # C01: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(1, 0), (2, 3), (3, 2), (4, 1)],  # C02: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(1, 3), (2, 2), (3, 1), (4, 0)],  # C03: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(1, 2), (2, 1), (3, 0), (4, 3)],  # C04: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C05-C08: Board (E1, E3) using Seq1-Seq4
    [(1, 1), (2, 0), (5, 3), (6, 2)],  # C05: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(1, 0), (2, 3), (5, 2), (6, 1)],  # C06: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(1, 3), (2, 2), (5, 1), (6, 0)],  # C07: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(1, 2), (2, 1), (5, 0), (6, 3)],  # C08: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C09-C12: Board (E2, E1) using Seq1-Seq4
    [(3, 1), (4, 0), (1, 3), (2, 2)],  # C09: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(3, 0), (4, 3), (1, 2), (2, 1)],  # C10: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(3, 3), (4, 2), (1, 1), (2, 0)],  # C11: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(3, 2), (4, 1), (1, 0), (2, 3)],  # C12: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C13-C16: Board (E2, E3) using Seq1-Seq4
    [(3, 1), (4, 0), (5, 3), (6, 2)],  # C13: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(3, 0), (4, 3), (5, 2), (6, 1)],  # C14: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(3, 3), (4, 2), (5, 1), (6, 0)],  # C15: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(3, 2), (4, 1), (5, 0), (6, 3)],  # C16: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C17-C20: Board (E3, E1) using Seq1-Seq4
    [(5, 1), (6, 0), (1, 3), (2, 2)],  # C17: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(5, 0), (6, 3), (1, 2), (2, 1)],  # C18: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(5, 3), (6, 2), (1, 1), (2, 0)],  # C19: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(5, 2), (6, 1), (1, 0), (2, 3)],  # C20: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C21-C24: Board (E3, E2) using Seq1-Seq4
    [(5, 1), (6, 0), (3, 3), (4, 2)],  # C21: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(5, 0), (6, 3), (3, 2), (4, 1)],  # C22: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(5, 3), (6, 2), (3, 1), (4, 0)],  # C23: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(5, 2), (6, 1), (3, 0), (4, 3)]   # C24: Seq4 - Textual+F, Map+N, Map+F, Textual+N
]

# --- SCENARIO CONTENT (BRIEFINGS AND QUESTIONS) ---
SCENARIO_CONTENT = {
    1: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the southwest (SW) region. 
Robot 2 is responsible for the northwest (NW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Has more than one package been discovered?",
                "options": ["Yes", "No"]
            },
            {
                "text": "Which quadrant has most packages been discovered?",
                "options": ["SE", "SW", "NE", "NW"]
            },
            {
                "text": "Which containment zone will robot 3 deliver its package to?",
                "options": [
                    "a. Robot 3 will leave the SW quadrant and deliver its package in the NW",
                    "b. Robot 3 will remain in the SW quadrant and deliver its package in the SW",
                    "c. Robot 3 will go to the NE quadrant and deliver its package in the NW",
                    "d. Robot 3 will leave the SW quadrant and deliver its package in the SE"
                ]
            }
        ]
    },
    2: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the southwest (SW) region. 
Robot 2 is responsible for the northwest (NW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which robot(s) are currently navigating around an obstacle?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "None"]
            },
            {
                "text": "What obstacle is Robot 3 facing?",
                "options": [
                    "Robot 3 is communicating to a different robot",
                    "Robot 3 is stuck in rough terrain",
                    "Robot 3 is recharging",
                    "Robot 3 is encountering bad weather"
                ]
            },
            {
                "text": "Which robot do you expect will finish its task last?",
                "options": ["Robot 1", "Robot 2", "Robot 3"]
            }
        ]
    },
    3: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northwest (NW) region. 
Robot 2 is responsible for the southeast (SE) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "What is the status of Robot 2?",
                "options": ["Replanning due to bad weather", "Replanning due to rough terrain", "Recharging", "On track"]
            },
            {
                "text": "What are the implications of robot 2 being caught in a bad weather system?",
                "options": [
                    "Robot 2 will have to send its assignment to a different robot",
                    "Robot 2’s delivery will not be impacted",
                    "Robot 2 will desert its mission entirely",
                    "Robot 2 will have to replan its route"
                ]
            },
            {
                "text": "Which robot is likely to deliver a package next?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "Robot 2 and 3 simultaneously"]
            }
        ]
    },
    4: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northwest (NW) region. 
Robot 2 is responsible for the southeast (SE) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which quadrant is Robot 3 in?",
                "options": ["SE", "NE", "NW", "SW"]
            },
            {
                "text": "Why is Robot 3 in the NW quadrant?",
                "options": [
                    "Robot 3 discovered a package in the NE and is delivering it to the NW",
                    "Robot 3 was assigned a package in the NW and is delivering it",
                    "Robot 1 requested Robot 3 to pick-up a package in the NW region",
                    "Robot 2 requested Robot 3 to pick-up a package in the NW region"
                ]
            },
            {
                "text": "Which containment zone will robot 3 end its mission?",
                "options": ["SE", "SW", "NE", "NW"]
            }
        ]
    },
    5: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northeast (NE) region. 
Robot 2 is responsible for the southwest (SW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "What is the status of robot 2?",
                "options": ["Just picked up a package", "Just delivered a package", "Robot 2 is recharging", "Robot 2 is replanning"]
            },
            {
                "text": "Given that robot 2 just delivered a package, what comes next?",
                "options": [
                    "Robot 2 will head towards a different package in the NW quadrant",
                    "Robot 2 will assist Robot 2 in the NW quadrant",
                    "Robot 2 will head towards a different package in the SW quadrant",
                    "Robot 2 will assist Robot 3 in the NE quadrant",
                    "Robot 2 will search the NE and SE quadrants for remaining packages"
                ]
            },
            {
                "text": "Which robot is likely to finish its mission next?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "Robot 1 and 2 simultaneously", "Robot 3 and 2 simultaneously"]
            }
        ]
    },
    6: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northeast (NE) region. 
Robot 2 is responsible for the southwest (SW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which robot(s) are currently navigating around an obstacle?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "No robots are encountering an obstacle"]
            },
            {
                "text": "What type of obstacle(s) are robot 2 and robot 3 experiencing?",
                "options": [
                    "Both robots are experiencing poor weather",
                    "Both robots are experiencing rough terrain",
                    "Robot 2 is experiencing poor weather, Robot 3 is experiencing rough terrain",
                    "Robot 2 is experiencing rough terrain, Robot 3 is experiencing poor weather"
                ]
            },
            {
                "text": "What is robot 3 going to do now that it has cleared both the NE and SE quadrants and dropped off any discovered packages?",
                "options": [
                    "Robot 3 will end its mission",
                    "Robot 3 will assist Robot 2 in the SE",
                    "Robot 3 will assist Robot 1 in the NW",
                    "Robot 3 will recharge"
                ]
            }
        ]
    }
}