def choose_country(quiz_data):
    if quiz_data['q1'] == 'beach' and quiz_data['q2'] == 'sunny' and quiz_data['q3'] == 'european' and quiz_data['q5'] != 'weekend':
        return "greece"
    elif quiz_data['q1'] != 'hiking' and quiz_data['q2'] == 'sunny' and quiz_data['q3'] == 'exotic' and quiz_data['q5'] == 'week':
        return "thailand"
    elif quiz_data['q1'] == 'hiking' and quiz_data['q3'] == 'exotic' and quiz_data['q4'] != 'family' and quiz_data['q5'] == 'month':
        return "china"
    elif quiz_data['q2'] == 'chilly' and quiz_data['q3'] == 'any' and quiz_data['q4'] != 'family' and quiz_data['q5'] != 'month':
        return "norway"
    elif quiz_data['q2'] != 'chilly' and quiz_data['q3'] == 'european' and quiz_data['q4'] != 'month':
        return "spain"
    elif quiz_data['q1'] == 'hiking' and quiz_data['q3'] == 'european' and quiz_data['q4'] != 'family' and quiz_data['q4'] != 'month':
        return "switzerland"
    elif quiz_data['q1'] == 'beach' and quiz_data['q2'] == 'sunny' and quiz_data['q3'] != 'european' and quiz_data['q5'] != 'weekend':
        return "barbados"
    else:
        return "spain"
