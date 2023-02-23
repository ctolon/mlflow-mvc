"""Extra Decorators Module"""

def setter_onlyf(f):
    """Util function for create write-only field"""
    
    return property(None, f)