def process(df, exculde_cols = [], to_numeric_cols = []):
    """ Performs preliminary processing of a dataframe by dropping unwanted columns and changing categorical features to numerical ones.
        
    Args:
        df:                   A pandas data frame containing the input data
        exclude_cols          A list of column names to exclued from the result
        to_numeric_cols       A list of column names of categorial features to change into numerical ones
        
    Returns:
        A processed dataframe
    """
    
    if exclude_cols:
        df = df.drop(exclude_cols, axis=1) # axis=1 to drop from columns, axis=0 drops entries
    df = pd.get_dummies(to_numeric_cols, drop_first=True)
    return df