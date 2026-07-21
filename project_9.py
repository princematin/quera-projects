from datetime import datetime

def day_calculator(date):
    date_vared_shode = datetime.strptime(date, '%Y-%m-%d')
    sajad_birth_date = datetime.strptime("1999-01-14", '%Y-%m-%d')
    if sajad_birth_date < date_vared_shode :
        date_ekhtelaf = (date_vared_shode - sajad_birth_date).days
        return date_ekhtelaf
    else :
        return 'Not yet born'


day_calculator('2005-01-06')