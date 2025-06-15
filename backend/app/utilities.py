def rungeKutta(f, x0, y0, h, n):
    """
    Runge-Kutta method for solving ordinary differential equations.
    
    Parameters:
    f : function - la función definida por la EDO
    x0 : float - valor de x
    y0 : float - valor de y
    h : float - tamaño del salto.
    n : int - cant de saltos.
    
    Returns:
    list of tuples (x, y) representing the solution at each step
    """
    result = [(x0, y0)]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        
        y_next = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x0 + h
        
        result.append((x_next, y_next))
        
        x0, y0 = x_next, y_next
    
    return result


