lis = [
    ('Pilani', 'B.E. Computer Science', 327),
    ('Pilani', 'M.Sc. Economics', 271),
    ('Pilani', 'B.E. Chemical', 247),
    ('Pilani', 'M.Sc. Biological Sciences', 236),
    ('Goa', 'B.E. Computer Science', 301),
    ('Goa', 'M.Sc. Economics', 263),
    ('Goa', 'B.E. Chemical', 239),
    ('Goa', 'M.Sc. Biological Sciences', 234),
    ('Hyderabad', 'B.E. Computer Science', 298),
    ('Hyderabad', 'M.Sc. Economics', 261), 
    ('Hyderabad', 'B.E. Chemical', 238),
    ('Hyderabad', 'M.Sc. Biological Sciences', 234)]     #list of '24 batch cutoffs, as input

dic = {'Pilani': {}, 'Goa': {}, 'Hyderabad': {}}    #converting to required format dictionary
for i in lis:
    dic[i[0]][i[1]] = i[2]

print(dic)