import pygal.maps.world

def get_country_code(country_name):
    """很据国家，返回国别码"""
    for code,name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    #没有找到指定国家
    return None


