import json

from fuzzywuzzy import fuzz

def build_scores(search_key, search_term, data):
    """ fuzzywuzzy your way to results
    """
    scores = []
    for item in data[search_key]:
        score = fuzz.ratio(search_term, item)
        if score > 50:
            scores.append((score, item, search_key))
    return scores

def search(search_key, search_term):
    # TODO: pull this out to the init so we don't r every search
    # and environ filename
    with open("fodmap_list.json", "r") as f:
        data = json.load(f)
    scores = []
    if search_key == 'either':
        # we just want to know what key it exists in, if any.
        scores += build_scores('high', search_term, data)
        scores += build_scores('low', search_term, data)
    else:
        scores += build_scores(search_key, search_term, data)
    # highest score first
    if not scores:
        return None
    scores.sort(reverse=True)
    return scores