
import re
abbreviation_mapping = {
    'wt': 'what',
    'hw': 'how',
    'y': 'why',
    'u': 'you',
    'uu': 'you',
    'uuuu': 'you',
    'uuu': 'you',
    'yu': 'you',
    'btw': 'between',
    'b/w': 'between',
}

def handle_special_cases(text):
    if re.match(r'\bwt\b', text, re.IGNORECASE):
        return 'what'
    elif re.match(r'\bhw\b', text, re.IGNORECASE):
        return 'how'
    elif re.match(r'\by\b', text, re.IGNORECASE):
        return 'why'
    elif re.match(r'\bu+\b', text, re.IGNORECASE):
        return 'you'
    elif re.match(r'\bbtw\b|\bb/w\b', text, re.IGNORECASE):
        return 'between'
    
    return text

def expand_abbreviations(text):
    for abbreviation, full_form in abbreviation_mapping.items():
        text = text.replace(abbreviation, full_form)
    return text
