def drag_force(rho, Cd, area, v):
    return 0.5 * rho * Cd * area * v * abs(v)