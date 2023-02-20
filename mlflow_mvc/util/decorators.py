def setterOnly(f):
    """Util function for create write-only field"""
    
    return property(None, f)