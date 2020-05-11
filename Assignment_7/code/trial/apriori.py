for i in range(100): 
    for j in range(100): 
        a.append(i) 
        b.append(j) 
        c.append(i*i*j) 
                                                                                        
fig = plt.figure()                                                                              

ax = fig.add_subplot(111, projection='3d')                                                      

ax.scatter(a,b,c)                                                                               

ax.set_zlabel('time')                                                                           

ax.set_ylabel('number of Hidden States')                                                        


ax.set_xlabel('number of Observable states')                                                    

plt.show()  
