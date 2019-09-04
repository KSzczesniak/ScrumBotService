



## story_1  <!-- name of the story  -->
* greet
   - utter_greet
* get_help{"scrum_core": "scrum"}  <!-- user utterance, in format intent{entities} -->
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next       <!-- action that the bot should execute -->
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye
   
## story_2
* greet
   - utter_greet
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_core": "scrum"} 
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next   
* create_task
   -utter_get_more_info
* create_task{"scrum_task": "story", "PERSON": "John", "CARDINAL": "13", "scrum_artifacts": "sp"}
   -utter_task_created
   -utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye
   
## story_3  
* greet
   - utter_greet
* get_help
   - utter_intro
>check_intro
* get_help{"scrum_ceremonies": "retro"} 
   - utter_inform_retro
   - utter_does_help
* mood_deny
   - utter_show_more   
* create_task{"scrum_task": "epic", "PERSON": "Sara", "CARDINAL": "8", "scrum_artifacts": "sp"}
   -utter_task_created
   -utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next  
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

## story_4
* get_help
   - utter_intro
* get_help{"scrum_ceremonies": "retro"} 
   - utter_inform_retro
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_core": "scrum"} 
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next  
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

   
## story_5  
>check_intro
* get_help{"scrum_core": "scrum"} 
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

## story_6
>check_intro
* get_help{"scrum_core": "scrum"} 
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_ceremonies": "retro"} 
   - utter_inform_retro
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye


## story_7 
>check_intro
* get_help{"scrum_core": "scrum"} 
   - utter_inform_scrum
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

## story_8  
>check_intro
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

## story_9
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* create_task{"scrum_task": "epic", "PERSON": "Sara", "CARDINAL": "8", "scrum_artifacts": "sp"}
   -utter_task_created
   -utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye

## story_10
* create_task{"scrum_task": "epic", "PERSON": "Sara", "CARDINAL": "8", "scrum_artifacts": "sp"}
   -utter_task_created
   -utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye


## story_11
>check_intro
* create_task{"scrum_task": "epic", "PERSON": "Sara", "CARDINAL": "8", "scrum_artifacts": "sp"}
   -utter_task_created
   -utter_next
* get_help{"scrum_ceremonies": "planning"} 
   - utter_inform_planning
   - utter_does_help
* mood_affirm
   - utter_next
* get_help{"scrum_roles": "sm"} 
   - utter_inform_sm
   - utter_does_help
* mood_affirm
   - utter_next
* mood_affirm
   - utter_next
* mood_deny
   - utter_happy_to_help
* goodbye
   - utter_goodbye
