from poetry_deps import get_test_data
def find_rev_deps(name):
    return [1, 2, 3]
 
def process_raw_data(raw_data):
    """Sort deps by name, add reverse dependancies to dictionary"""
    for elem in raw_data:
        elem['rev_deps'] = find_rev_deps(elem['name'])
    
    data_sorted = sorted(raw_data, key=lambda d: d['name'])
    return data_sorted #???list of dictionaries 

deps = process_raw_data(get_test_data()) #map object

def find_dep_by_name(name):
    """Find dependency by name and return a dep-dictionary"""
    for dep in iter(deps): 
        if dep['name'] == name:
            return dep
    return None

def get_dep_names():
    """Get a list of dependancy names for representation"""
    dep_names = []
    for dep in iter(deps):
        dep_names.append(dep['name'])
    return dep_names

def get_opt_dep_names(name = ''):
    """Get a list of optional dependancy names for representation in html Dependancy page"""
    opt_dep_names = []
    for dep in iter(deps):
        if dep['name'] == name:
            for d in dep['optional_deps']:
                opt_dep_names.append(d)
    #print(opt_dep_names)
    return opt_dep_names

# dep_names = get_dep_names(index_page = False, name = 'cachecontrol')
# opt_dep_names = get_opt_dep_names('cachecontrol')