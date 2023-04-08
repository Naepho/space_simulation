def cavendish():
    si = 6.6743*1e-11
    num = ((365*24*3600)**2)*1e24
    den = 1e27
    frac = num/den
    return si*frac

# Values used through the project
val = {
    'init': [
        [0, 0, 0, 0, 0, 0, 1.988e6], # Sun
        [-1.451*100, 0, 0, 0, 923, 0, 5.972], # Earth
        [-1.5*100, 0, 50, -100, 923, 0, 0.001], # Moon
        [0, 0, 500, -400, 0, 0, 10], # Jupiter ?
        [103, -456, 32, -133, 456, -43, 2],
        [87, 456, -100, 0, 24, 103, 10]
    ],
    'length': 1,
    'cavendish': cavendish(),
    'solveivp': {
        'rtol': 1e-13,
        'atol': 1e-13,
        'max-step': 1e-2
    }
}
