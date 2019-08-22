def atmosphere_ln_pressure_coordinate(p0, lev):
    """
        Creates a dimensioned version of atmosphere natural log pressure coordinate.
        
        Definition:
        p(k) = p0 * exp(-lev(k))
        
        where p(k) is the pressure at gridpoint (k), p0 is a reference pressure, lev(k) is the dimensionless coordinate at vertical gridpoint (k).
    """
    
    return p0 * np.exp(-lev)


def atmosphere_sigma_coordinate(ptop, sigma, ps):
    """
        Creates a dimensioned version of atmosphere sigma pressure coordinate.
        
        Definition:
        p(n,k,j,i) = ptop + sigma(k)*(ps(n,j,i)-ptop)
        
        where p(n,k,j,i) is the pressure at gridpoint (n,k,j,i), ptop is the pressure at the top of the model, sigma(k) is the dimensionless \
        coordinate at vertical gridpoint (k), and ps(n,j,i) is the surface pressure at horizontal gridpoint (j,i)and time (n).
    """
    
    return ptop + sigma * ( ps - ptop )


def atmosphere_hybrid_sigma_pressure_coordinate_v1(a, b, p0, ps):
    """
        Creates a dimensioned version of v1 atmosphere hybrid sigma pressure coordinate.
        
        Definition:
        p(n,k,j,i) = a(k)*p0 + b(k)*ps(n,j,i)
        
        where p(n,k,j,i) is the pressure at gridpoint (n,k,j,i), a(k) and b(k) are components of the hybrid coordinate at level \
        k, p0 is a reference pressure, and ps(n,j,i) is the surface pressure at horizontal gridpoint (j,i) and time (n).
    """
    
    return a * p0 + b * ps


def atmosphere_hybrid_sigma_pressure_coordinate_v2(ap, b, ps):
    """
        Creates a dimensioned version of v2 atmosphere hybrid sigma pressure coordinate.
        
        Definition:
        p(n,k,j,i) = ap(k) + b(k)*ps(n,j,i)
        
        where p(n,k,j,i) is the pressure at gridpoint (n,k,j,i), a(k) or ap(k) and b(k) are components of the hybrid coordinate at level \
        k, p0 is a reference pressure, and ps(n,j,i) is the surface pressure at horizontal gridpoint (j,i) and time (n).
    """
    
    return ap + b * ps


def atmosphere_hybrid_height_coordinate(a, b, orog):
    """
        Creates a dimensioned version of atmosphere hybrid height coordinate.
        
        Definition:
        z(n,k,j,i) = a(k) + b(k)*orog(n,j,i)
        
        where z(n,k,j,i) is the height above the datum (e.g. the geoid, which is approximately mean sea level) at gridpoint (k,j,i) and \
        time (n), orog(n,j,i) is the height of the surface above the datum at (j,i) and time (n), and a(k) and b(k) are the coordinates \
        which define hybrid height level k. a(k) has the dimensions of height and b(i) is dimensionless.
    """
    
    return a + b * orog


def atmosphere_sleve_coordinate(a, ztop, b1, zsurf1, b2, zsurf2):
    """
        Creates a dimensioned version of atmosphere sleve coordinate.
        
        Definition:
        z(n,k,j,i) = a(k)*ztop + b1(k)*zsurf1(n,j,i) + b2(k)*zsurf2(n,j,i)
        
        where z(n,k,j,i) is the height above the datum (e.g. the geoid, which is approximately mean sea level) at gridpoint (k,j,i) \
        and time (n), ztop is the height of the top of the model above the datum, and a(k), b1(k), and b2(k) are the dimensionless \
        coordinates which define hybrid level k. zsurf1(n,j,i) and zsurf2(n,j,i) are respectively the large-scale and small-scale \
        components of the topography, and a, b1 and b2 are all functions of the dimensionless SLEVE coordinate. See Shaer et al \
        [SCH02] for details.
    """
    
    return a * ztop + b1 * zsurf + b2 * zsurf
