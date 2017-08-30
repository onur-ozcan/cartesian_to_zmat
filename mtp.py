import numpy as np

ex_file = open('harmine.mol2','r')
content = ex_file.readlines()
#print len(content)

atom_type=[]
x=[]
y=[]
z=[]
bond=[]

#print 'empty xyz : ',x,y,z

for i in range(len(content)):
    if content[i][0:13] == "@<TRIPOS>ATOM":
        a = i+1
        while content[a][0:9] != '@<TRIPOS>':
            #print content[a]
            split_content = content[a].split()
            atom_type.append(str(split_content[1]))
            x.append(float(split_content[2]))
            y.append(float(split_content[3]))
            z.append(float(split_content[4]))
            a += 1
            
    elif content[i][0:13] == "@<TRIPOS>BOND":
        b = i+1
        #print b,type(b),content[b],type(content[b])

        while b < len(content) and content[b][0:9] != '@<TRIPOS>':
                #print content[b]
                split2_content= content[b].split()
                bond.append([int(split2_content[1]),int(split2_content[2]),split2_content[3]])
                b += 1
        
        
#print 'after append xyz : ',x,y,z
#print bond

at_arr = np.asarray(atom_type)
x_arr = np.asarray(x)
y_arr = np.asarray(y)
z_arr = np.asarray(z)

for item in bond:
    if item[2] == 'am':
        item[2] = int(4)
    
    elif item[2] == 'ar':
        item[2] = int(5)
    
    elif item[2] == 'du':
        item[2] = int(6)
        
    elif item[2] == 'un':
        item[2] = int(7)
        
    elif item[2] == 'nc':
        item[2] = int(8)
        
for item2 in bond:
    item2[2] = int(item2[2])
    
    
bond_arr = np.asarray(bond)

#print type(at_arr)
#print bond_arr
#print bond_mat

bond_mat = np.zeros((len(x_arr)+1,len(x_arr)+1))

#print len(bond)
#print bond
#print bond_mat.shape

for i in range(len(bond)):
    mi = bond[i][0]
    mj = bond[i][1]
    ms = bond[i][2]
    print mi,mj,ms
    bond_mat[mi,mj]=ms

#print bond_mat[5,6]
