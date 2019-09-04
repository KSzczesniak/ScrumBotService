from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config
import json
import random
import os

cwd = os.getcwd()

temp_dir = cwd + "/models/nlu/default/current"  # where model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(temp_dir)

def print_json(o):   
    print(json.dumps(o, indent=2))


responses = {}
with open('responses.json','r') as responses_file:
   responses = json.load(responses_file)

valid_entities = ["CARDINAL", "PERSON"]
task_creation_required_keys = {
    'PERSON' : "assignee",
    'CARDINAL' : "estimation",
    'scrum_task': "type of task",
    'scrum_artifacts': "unit of measure"
}
member_addition_required_keys = {
    'PERSON' : "assignee",
    'scrum_roles': "role in the team"
}

ACTION_DEFAULT = 0
ACTION_NAVIGATE_TO_DASHBOARD = 1
ACTION_TOGGLE_TASK_MODAL = 2 
ACTION_UPDATE_CURRENT_TASK = 3
ACTION_TASK_CREATED = 4
ACTION_NAVIGATE_TO_TEAM = 11
ACTION_TOGGLE_MEMBER_MODAL = 12
ACTION_UPDATE_CURRENT_MEMBER = 13
ACTION_MEMBER_ADDED = 14
ACTION_NAVIGATE_TO_ROLES = 20
ACTION_NAVIGATE_TO_PO = 21
ACTION_NAVIGATE_TO_SM = 22
ACTION_NAVIGATE_TO_DEV = 23
ACTION_NAVIGATE_TO_EVENTS = 30
ACTION_NAVIGATE_TO_SPRINT = 31
ACTION_NAVIGATE_TO_PLANNING = 32
ACTION_NAVIGATE_TO_REVIEW = 33
ACTION_NAVIGATE_TO_DAILY = 34
ACTION_NAVIGATE_TO_RETROSPECTIVE = 35
ACTION_NAVIGATE_TO_ARTIFACTS = 50

ent_to_help_actions_dict = {
    'product owner': ACTION_NAVIGATE_TO_PO,
    'scrum master': ACTION_NAVIGATE_TO_SM,
    'dev': ACTION_NAVIGATE_TO_DEV,
    'sprint': ACTION_NAVIGATE_TO_SPRINT,
    'planning': ACTION_NAVIGATE_TO_PLANNING,
    'review': ACTION_NAVIGATE_TO_REVIEW,
    'daily': ACTION_NAVIGATE_TO_DAILY,
    'retrospective': ACTION_NAVIGATE_TO_RETROSPECTIVE,
}

def process_entity_name(entity_name):
    processed_name = ''
    splitted_name = entity_name.split()
    if len(splitted_name):
        processed_name = '_'.join(splitted_name)
    else:
        processed_name = entity_name
    return processed_name


def handle_get_help(entities, params):
    result = []
    if not entities:
        if not params:
            result.append(random.choice(responses['utter_get_help']))
        else:
            result.append(random.choice(responses['utter_create_task_get_help']))
    else:
        for ent in entities:
            result.append(random.choice(responses[f'utter_get_help_{process_entity_name(ent["value"])}']))
        if not params:
            result.append(random.choice(responses['utter_does_help']))
        for ent in entities:
            params[ent["entity"]] = str(ent["value"])
    return result

def handle_greet(entities, params):
    return random.choice(responses['utter_greet'])

def handle_goodbye(entities, params):
    return random.choice(responses['utter_goodbye'])

def handle_create_task(entities, params):
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    
    missing_keys = [value for key, value in task_creation_required_keys.items() if key not in params]
    
    result = []
    actions = []
    actions.append(ACTION_TOGGLE_TASK_MODAL)
    if not params:
        result.append(random.choice(responses['utter_create_task']))
        actions.append(ACTION_NAVIGATE_TO_DASHBOARD)
    else:
        if missing_keys:
            response = random.choice(responses['utter_more_info'])
            for key in missing_keys:
                response = response + f" {key} "
            result.append(response)
            actions.append(ACTION_NAVIGATE_TO_DASHBOARD)
        else:
            result.append(random.choice(responses['utter_create_task_confirm']).format(params["scrum_task"], params["CARDINAL"], params["PERSON"]))
        actions.append(ACTION_UPDATE_CURRENT_TASK)
    return result, actions

def handle_task_created(entities, params):
    bot_responses =  [
        random.choice(responses['utter_task_created']),
        random.choice(responses['utter_next'])
    ]
    actions = [ACTION_TASK_CREATED]
    return bot_responses, actions

def handle_wrong_task_data(entities, params):
    return random.choice(responses['utter_create_task'])

def handle_add_member(entities, params):
    for ent in entities:
        params[ent["entity"]] = str(ent["value"])
    
    missing_keys = [value for key, value in member_addition_required_keys.items() if key not in params]
    
    result = []
    actions = []
    actions.append(ACTION_TOGGLE_MEMBER_MODAL)
    skills = ''
    if not params:
        result.append(random.choice(responses['utter_add_member']))
        actions.append(ACTION_NAVIGATE_TO_TEAM)
    else:
        if missing_keys:
            response = random.choice(responses['utter_more_info'])
            for key in missing_keys:
                response = response + f" {key} "
            result.append(response)
            actions.append(ACTION_NAVIGATE_TO_TEAM)
        else:
            if 'skills' in params:
                skills = params['skills']
            result.append(random.choice(responses['utter_add_member_confirm']).format(params["PERSON"], params["scrum_roles"], skills))
        actions.append(ACTION_UPDATE_CURRENT_MEMBER)
    return result, actions

def handle_member_added(entities, params):
    bot_responses = [
        random.choice(responses['utter_member_added']),
        random.choice(responses['utter_next'])
    ]
    actions = [ACTION_MEMBER_ADDED]
    return bot_responses, actions

def handle_wrong_member_data(entities, params):
    return random.choice(responses['utter_create_task'])

def handle_add_member_get_help(entities, params):
    result = []
    if not entities:
        result.append(random.choice(responses['utter_add_member_get_help']))
    else:
        result = handle_get_help(entities, params)
    return result

def handle_helped(entities, params):
    params.clear()
    return random.choice(responses['utter_next'])

def handle_show_more(entities, params):
    if not params:
        return random.choice(responses['utter_unclear']), [],
    first_entity = list(params.values())[0]
    actions = []
    if first_entity in ent_to_help_actions_dict:
        actions.append(ent_to_help_actions_dict[first_entity])
    
    params.clear()
    result = [
        random.choice(responses['utter_show_more']),
        random.choice(responses['utter_next'])
    ]
    return result, actions

def handle_unclear(entities, params):
    return random.choice(responses['utter_unclear'])

def handle_no_more_questions(entities, params):
    return random.choice(responses['utter_happy_to_help'])

def handle_more_questions(entities, params):
    return random.choice(responses['utter_go_ahead'])

BASE = 1
HELP = 2
TASK_CREATION = 3
MEMBER_ADDITION = 4

# Define the policy rules
policy = {
    (BASE, "greet"): (BASE, handle_greet),
    (BASE, "get_help"): (HELP, handle_get_help),
    (BASE, "create_task"): (TASK_CREATION, handle_create_task),
    (BASE, "add_member"): (MEMBER_ADDITION, handle_add_member),
    (BASE, "unclear"): (BASE, handle_unclear),
    (BASE, "mood_deny"): (BASE, handle_no_more_questions),
    (BASE, "mood_affirm"): (BASE, handle_more_questions),
    (BASE, "goodbye"): (BASE, handle_goodbye),

    (HELP, "get_help"): (HELP, handle_get_help),
    (HELP, "mood_affirm"): (BASE, handle_helped),
    (HELP, "mood_deny"): (BASE, handle_show_more),
    (HELP, "create_task"): (TASK_CREATION, handle_create_task),
    (HELP, "add_member"): (MEMBER_ADDITION, handle_add_member),
    (HELP, "goodbye"): (BASE, handle_goodbye),

    (TASK_CREATION, "create_task"): (TASK_CREATION, handle_create_task),
    (TASK_CREATION, "get_help"): (TASK_CREATION, handle_get_help),
    (TASK_CREATION, "mood_affirm"): (BASE, handle_task_created),
    (TASK_CREATION, "mood_deny"): (TASK_CREATION, handle_wrong_task_data),
    (TASK_CREATION, "goodbye"): (BASE, handle_goodbye),

    (MEMBER_ADDITION, "add_member"): (MEMBER_ADDITION, handle_add_member),
    (MEMBER_ADDITION, "get_help"): (MEMBER_ADDITION, handle_add_member_get_help),
    (MEMBER_ADDITION, "mood_affirm"): (BASE, handle_member_added),
    (MEMBER_ADDITION, "mood_deny"): (MEMBER_ADDITION, handle_wrong_member_data),
    (MEMBER_ADDITION, "goodbye"): (BASE, handle_goodbye),
}

def checkClarityOfPrediction(interpretation):
    rank = interpretation["intent_ranking"]
    firstPrediction = rank[0]["confidence"]
    secondPrediction = rank[1]["confidence"]
    return firstPrediction - secondPrediction > 0.05

def interpret(message, state, suggestion):
    intent = ''
    entities = []

    interpretation = interpreter.parse(message)
    if checkClarityOfPrediction(interpretation):
        intent = interpretation["intent"]["name"]
        temp_ents = interpretation["entities"]
        if temp_ents:
            entities = [{"entity": ent["entity"], "value": ent["value"]} for ent in temp_ents if ent["entity"].islower() or ent["entity"] in valid_entities]
    else:
        intent = "unclear"

    return intent, entities

def respond(state, message, params, suggestion, actions, policy = policy):
    intent, entities = interpret(message, state, suggestion)

    responses = []
    if (state, intent) in policy:
        (new_state, handler) = policy[(state, intent)]
        result = handler(entities, params)
        new_actions = []
        if isinstance(result, tuple):
            responses, new_actions = result
        else:
            responses = result
        actions = new_actions
    else:
        responses = random.choice(responses['utter_unclear'])
    
    formatted_responses = []
    if isinstance(responses, list):
        formatted_responses.extend(responses)
    else:
        formatted_responses.append(responses)
   
    return new_state, formatted_responses, params, suggestion, actions

def send_message(policy, state, message, params, suggestion, actions):
    with open("test_file.txt", "a") as test_file:
        test_file.write("USER: {}\n".format(message))
        print("USER: {}".format(message))
        new_state, responses, params, suggestion, actions = respond(state, message, params, suggestion, actions, policy)
        for response in responses:
            print("BOT: {}".format(response))
            test_file.write("BOT: {}\n".format(response))
    return new_state, params, suggestion, actions
    

stories = {}
with open('sample_stories.json','r') as sample_stories_file:
   stories = json.load(sample_stories_file)

# Call send_message() for each message
params, actions = {}, []
suggestion = ''
state = BASE

for message in stories['story5']:
    state, params, suggestion, actions = send_message(policy, state, message, params, suggestion, actions)