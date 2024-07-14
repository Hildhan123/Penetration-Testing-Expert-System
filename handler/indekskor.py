from collections import defaultdict
import json
import streamlit as st

def determine_score(alert):
    confidence = alert['confidence']
    risk = alert['risk']

    if confidence == 'High':
        if risk == 'High':
            return 10 
        elif risk == 'Medium':
            return 7 
        elif risk == 'Low':
            return 4 
    elif confidence == 'Medium':
        if risk == 'High':
            return 9 
        elif risk == 'Medium':
            return 6 
        elif risk == 'Low':
            return 3 
    else:
        return 1

def indekskor(data): 
    unique_attacks = defaultdict(list)

    for attack in data:
        key = (attack["name"], attack["description"], attack["risk"], attack["confidence"])
        unique_attacks[key].append(attack["url"])
    
    scores = {}
    for key, urls in unique_attacks.items():
        scores[key] = determine_score({
            "confidence": key[3],
            "risk": key[2]
        })

    total_unique_attacks = len(unique_attacks)
    average_score = sum(scores.values()) / len(scores)
    
    return average_score