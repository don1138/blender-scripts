import math

# refractiveindex.info
# IOR WAVELENGTHS: R = 0.65, G = 0.55, B = 0.44
# Reflectivity theta = 0
# Edge Tint theta = 80

# red_n, green_n, blue_n, red_k, green_k, blue_k, name
mats = [
    {'aluminium': [1.3456, 0.96521, 0.58460, 7.4746, 6.3995, 5.1874, 'Aluminium']},
    {'brass': [0.44400, 0.52700, 1.1910, 3.6950 , 2.7650, 1.7970, 'Brass']},
    {'chromium': [4.3486, 3.5880, 2.2288, 4.6840, 4.8982, 4.3757, 'Chromium']},
    {'copper': [0.27105, 0.67693, 1.3336, 3.6092, 2.6248, 2.2963, 'Copper']},
    {'gold': [0.18299, 0.42108, 1.4327, 3.4242, 2.3459, 1.7916, 'Gold']},
    {'iron': [2.9114, 2.9497, 2.5295, 3.0893, 2.9318, 2.7370, 'Iron']},
    {'lead': [1.9100, 1.8300, 1.4400, 3.5100, 3.4000, 3.1800, 'Lead']},
    {'mercury': [2.0733, 1.5523, 1.0147, 5.3383, 4.6510, 3.7769, 'Mercury']},
    {'nickel': [1.9900, 1.9212, 1.7190, 4.2086, 3.6158, 2.8785, 'Nickel']},
    {'palladium_hydride': [2.1286, 2.0377, 1.9030, 3.5239, 3.0363, 2.6094, 'Palladium Hydride']},
    {'palladium': [1.7893, 1.6412, 1.3880, 4.3750, 3.8455, 3.1940, 'Palladium']},
    {'platinum': [2.3757, 2.0847, 1.8227, 4.2655, 3.7153, 3.0787, 'Platinum']},
    {'silicon': [3.8491, 4.0715, 4.8095, 0.0015810, 0.0062500, 0.10603, 'Silicon']},
    {'silver': [0.15943, 0.14512, 0.13530, 3.9291, 3.1900, 2.2915, 'Silver']},
    {'tin': [4.3100, 3.2400, 2.3780, 38.700, 32.900, 26.520, 'Tin']},
    {'titanium': [2.7407, 2.5418, 2.2370, 3.8143, 3.4345, 3.0235, 'Titanium']},
    {'zinc': [1.2338, 0.92943, 0.65730, 5.8730, 4.9751, 3.9102, 'Zinc']},
]

def clamp(val, min_val, max_val):
    return min(max(val, min_val), max_val)

def n_min(r):
    return (1-r)/(1+r)

def n_max(r):
    return (1+math.sqrt(r))/(1-math.sqrt(r))

def get_n(r,g):
    return n_min(r)*g + (1-g)*n_max(r)

def get_k2(r, n):
    nr = (n+1)**2*r-(n-1)**2
    return nr/(1-r)

def get_r(n, k):
    return ((n-1)**2+k**2)/((n+1)**2+k**2)

def get_g(n, k):
    r = get_r(n,k)
    return (n_max(r)-n)/(n_max(r)-n_min(r))

def fresnel(r, g, theta):
    # clamp parameters
    _r = clamp(r,0.1,0.99)
    # compute n and k
    n = get_n(_r,g)
    k2 = get_k2(_r,n)

    c = math.cos(theta)
    rs_num = n**2 + k2 - 2*n*c + c**2
    rs_den = n**2 + k2 + 2*n*c + c**2
    rs = rs_num/rs_den

    rp_num = (n**2 + k2)*c**2 - 2*n*c + 1
    rp_den = (n**2 + k2)*c**2 + 2*n*c + 1
    rp = rp_num / rp_den

    return 0.5*(rs+rp)

def calc_colors(units):
    uv_dict = mats[units]
    unit_key = list(uv_dict.keys())[0]
    unit_value = uv_dict[unit_key]

    theta_refl = 0.0
    theta_edge = 80.0
    r_red = get_r(unit_value[0], unit_value[3])
    g_red = get_g(unit_value[0], unit_value[3])
    reflectivity_red = fresnel(r_red, g_red, theta_refl)
    edgetint_red = fresnel(r_red, g_red, theta_edge)

    r_green = get_r(unit_value[1], unit_value[4])
    g_green = get_g(unit_value[1], unit_value[4])
    reflectivity_green = fresnel(r_green, g_green, theta_refl)
    edgetint_green = fresnel(r_green, g_green, theta_edge)

    r_blue = get_r(unit_value[2], unit_value[5])
    g_blue = get_g(unit_value[2], unit_value[5])
    reflectivity_blue = fresnel(r_blue, g_blue, theta_refl)
    edgetint_blue = fresnel(r_blue, g_blue, theta_edge)

    print(unit_value[6])
    print(f"[{round(reflectivity_red, 6)}, {round(reflectivity_green, 6)}, {round(reflectivity_blue, 6)}, 1]")
    print(f"[{round(edgetint_red, 6)}, {round(edgetint_green, 6)}, {round(edgetint_blue, 6)}, 1]\n")
    

count = len(mats)
for i in range(count):
    calc_colors(i)
