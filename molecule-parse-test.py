elemData = [['A', 'B', 'C', 'D'],
            [ 1,   2,   3,   4]]

def partMass(atomArr):
    """
    recursive function for finding the mass of a molecule partition array

    atomArr is an array of strings of either:  a single element, 
    a single element with an integer multiple, or a compound in parentheses
    """
    mass = 0
    for atom in atomArr:
        if len(atom) == 1:                                              # just a single atom
            mass += elemData[1][elemData[0].index(atom)]
        
        elif '(' not in atom or '(' not in atom:                        # single element with integer multiple, like Cl2
            i = 0
            for ch in atom:                                                     # find index of number start
                if ch not in '1234567890':
                    i += 1
                else:
                    break
            mass += partMass(atom[:i]) * int(atom[i:])
        
        else:                                                           # compound in parentheses
            i = -1
            for ch in atom[::-1]:                                               # find index of last closing parenthesis
                if ch != ')':
                    i -= 1
                else:
                    break
            mass += partMass(partMol(atom[1:i])) * int(atom[i+1:])
    return mass
    
"""
NOTES:

two functions:
/info [element] : gives info on the provided element
/mass [molecule] : gives mass of molecule, that's what this function is for!

look at solution to roman numeral problem for help parsing!
"""