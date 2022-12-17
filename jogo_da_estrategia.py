j , r  = [ int ( x ) for  x  in  input (). split ()]
input  =  list ( map ( int , input ( ). split ()))
 
points  = [ 0 ] *  j
 
for  k  in  range ( j ):
 points [ k ] =  sum ( input [ k :: j ])
 
points  =  points [:: - 1 ]
winner  =  j  -  points . index ( max ( points ))
print ( winner )