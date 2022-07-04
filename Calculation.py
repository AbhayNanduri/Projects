from numpy import *

def Calculate( alpha, t , l , r , omega, e ) :

    theta = 0 
    if alpha == 0 : theta = ( omega *  t  )
    else : theta = ( alpha * ( t ** 2 ) ) / 2

    x1 = r * cos(theta)
    h = ( r * sin(theta) ) + e
     
    x2 = sqrt( l**2 - h**2 )

    x = x1 + x2

    dx1 = -( r * omega * sin(theta) )
    dh = r * omega * cos(theta)
    dx2 =  - (h * dh) / ( sqrt( l**2 - h**2 ) )

    v = dx1 + dx2

    a = - ( (r*alpha) * ( sin(theta) + ( cos(theta) * ( h / x2 ) ) ) ) - (r * (omega**2)) * ( cos(theta) - ( sin(theta)  * (h/x2) ) + cos(theta) * ( ( x2*dh - h*dx2 ) / ( x2**2 ) ) )

    return x, v ,a 


