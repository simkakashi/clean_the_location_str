class exception (Exception):
    pass

class PlaceTypeNotExist(exception):
    pass

class InputTypeNotExist(exception):
    input_type = '''
    it should be
    Province | City | Area/District
    
    '''
    pass