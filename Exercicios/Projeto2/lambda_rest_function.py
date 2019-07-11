def lambda_rest(o,z):
    ''' Defining the relation between lambda_rest, lambda_obs and redshift '''
    r = o/(1+z)
    return ["%.0f" % a for a in r]
