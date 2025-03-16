class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Child:
    def __init__(self, father, mother, choice_index_father, choice_index_mother):
        self.inherited_alleles = (father.blood_types[choice_index_father], mother.blood_types[choice_index_mother])
        self.blood_type = self.determine_blood_type()
    
    def determine_blood_type(self):
        alleles = set(self.inherited_alleles)
        if alleles == {'A', 'B'}:
            return 'AB'
        elif 'A' in alleles and 'O' in alleles:
            return 'A'
        elif 'B' in alleles and 'O' in alleles:
            return 'B'
        elif alleles == {'A'}:
            return 'A'
        elif alleles == {'B'}:
            return 'B'
        else:
            return 'O'
    
    def __str__(self):
        return f"Child's Blood Type: {self.blood_type} (Inherited Alleles: {self.inherited_alleles})"


father = Father(('A', 'O'))
mother = Mother(('B', 'O'))
child = Child(father, mother, 0, 1)

print(child)
