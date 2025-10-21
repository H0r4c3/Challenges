'https://py.checkio.org/en/mission/blood-distribution-3/share/66c45b812f3be41c71aa5db192350ffe/'

'''
Your mission is to distribute available blood of different types to patients requiring transfusions, considering each blood type's compatibility restrictions.

Input: The blood quantities (blood_avail) and the blood needs (blood_needs) for each blood type as dictionaries (dict) 
with string keys (str) and integer values (int).

Output: The output will be the distribution of blood quantities for each blood type as dictionary of dictionaries (dict) with 
string keys (str) and integer values (int).
'''
dist_blood = {
        'A': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'B': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'AB': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'O': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
    }

def dist_bl(bl_n, bl_av, blood_all, dist_blood):
    if blood_all[bl_av][0] >= blood_all[bl_n][1]:
        #distributed from blood type bl_n
        dist_blood[bl_av][bl_n] += blood_all[bl_n][1]
        #new available
        blood_all[bl_av][0] = blood_all[bl_av][0] - blood_all[bl_n][1]
        #new needs
        blood_all[bl_n][1] = 0
    else:
        #distributed from blood type bl_av
        dist_blood[bl_av][bl_n] += blood_all[bl_av][0]
        #new needs
        blood_all[bl_n][1] = blood_all[bl_n][1] - blood_all[bl_av][0]
        #new available
        blood_all[bl_av][0] = 0
        
    return blood_all, dist_blood

def distribute_blood(
    blood_avail: dict[str, int], blood_needs: dict[str, int]
) -> dict[str, dict[str, int]]:
    
    print('--------START-------')
    
    dist_blood = {
        'A': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'B': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'AB': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
        'O': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
    }
    
    # create a dictionary with avail and needs for all
    blood_all = {'A': [blood_avail['A'], blood_needs['A']], 
                 'B': [blood_avail['B'], blood_needs['B']],
                 'AB': [blood_avail['AB'], blood_needs['AB']],
                 'O': [blood_avail['O'], blood_needs['O']]}
    
    print(blood_all)

    # resolve O from O -> TO CHANGE into TO, not FROM
    blood_all_after, dist_blood_after = dist_bl('O', 'O', blood_all, dist_blood)
    
    # resolve A from A
    blood_all_after, dist_blood_after = dist_bl('A', 'A', blood_all, dist_blood)
    
    # resolve B from B
    blood_all_after, dist_blood_after = dist_bl('B', 'B', blood_all, dist_blood)
    
    # resolve AB from AB
    blood_all_after, dist_blood_after = dist_bl('AB', 'AB', blood_all, dist_blood)
    
    # resolve AB from A, B
    blood_all_after, dist_blood_after = dist_bl('AB', 'A', blood_all, dist_blood)
    blood_all_after, dist_blood_after = dist_bl('AB', 'B', blood_all, dist_blood)
    
    # resolve A from O
    blood_all_after, dist_blood_after = dist_bl('A', 'O', blood_all, dist_blood)
    
    # resolve B from O
    blood_all_after, dist_blood_after = dist_bl('B', 'O', blood_all, dist_blood)
    
    # resolve AB from 0
    blood_all_after, dist_blood_after = dist_bl('AB', 'O', blood_all, dist_blood)
    
    print('dist_blood_after')
    print(dist_blood_after)
    
    return dist_blood_after


if __name__ == "__main__":
    assert distribute_blood(
        {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}
    ) == {
        "A": {"A": 100, "B": 0, "AB": 50, "O": 0},
        "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
        "O": {"A": 0, "B": 0, "AB": 0, "O": 0},
    }
    assert distribute_blood(
        {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
    ) == {
        "A": {"A": 10, "B": 0, "AB": 0, "O": 0},
        "B": {"A": 0, "B": 10, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 20, "O": 0},
        "O": {"A": 10, "B": 0, "AB": 10, "O": 0},
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")
