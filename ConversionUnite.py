def conversionUnite(valeur,unite,uniteconv):
    conversion = {
        'mesures': {
            'km': 1000,
            'dm': 10,
            'm': 1,
            'dcm': 0.1,
            'cm': 0.01,
            'mm': 0.001
            },
        'poids': {
            't': 1000,
            'q': 100,
            'kg': 1,
            'dc': 0.1,
            'g': 0.001,
            'mg': 0.000001
            }
    }



print(conversionUnite(2357,'m','km'))
