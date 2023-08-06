#------------------------------------------------------------------------------
# Libraries
#------------------------------------------------------------------------------
# Standard
import sys, time, random
from datetime import datetime
import numpy as np
import pandas as pd
import numbers
from functools import reduce
import itertools
from pandas.api.types import is_integer_dtype
from pandas.api.types import is_float_dtype
        
# User
from .exceptions import WrongInputException
from .sanity_check import check_type
#------------------------------------------------------------------------------
# Cross validation tools
#------------------------------------------------------------------------------
def generate_random_masks(n_obs, n_split, test_pct, run_unit_test=False):    
    """
    Generate random masks to split data
    """
    # Define masks for training and testing
    if n_split==0:
        masks = np.array_split(ary=np.random.permutation(n_obs), indices_or_sections=1)
    elif n_split==1:
        masks = np.array([False]*n_obs)
        masks[np.random.permutation(n_obs)[0:int(n_obs*test_pct)]] = True
        masks = [masks]
    elif n_split>1:
        
        # Split array into position masks (integers)
        mask_positions = np.array_split(ary=np.random.permutation(n_obs), indices_or_sections=n_split)
        
        # Pre-allocate
        masks = []
        
        for m in mask_positions:
            # Initialize mask
            mask = np.array([False]*n_obs)
        
            # Set masked array to True (test set)
            mask[m] = True
            
            # Append
            masks.append(mask)
            
    if run_unit_test:
        for idx in range(1,len(masks)):
            if any(masks[0][masks[0]] == masks[idx][masks[0]]):
                raise Exception("Masking failed. Some cells are repeated in masks")

    return masks

def generate_grid_from_dict(d):
    """
    Generate list of all dict permutations
    Default to empty list if dict is empty
    """
    check_type(x=d,allowed=dict,name="d")

    d = convert_dict_values_to_list(d)
    
    keys, values = zip(*d.items())
    grid = [dict(zip(keys, v)) for v in itertools.product(*values)]        
    
    return grid

#------------------------------------------------------------------------------
# Tools to start and stopping scripts
#------------------------------------------------------------------------------
def initialize_script(seed=1991):

    # Start Timer
    t0 = time.time()

    # Set seed
    random.seed(1991)

    # Get current time and date
    now = datetime.now()
    
    print2(f"This script was initialized {now.strftime('at %H:%M:%S on %B %d, %Y')}")

    return t0


def end_script(t0):

    # Stop Timer
    t1 = time.time()
    
    # Set seed
    random.seed(1991)

    # Get current time and date
    now = datetime.now()
    
    print2(f"""This script was ended {now.strftime('at %H:%M:%S on %B %d, %Y')}:

   It took:
       {int(t1-t0)} seconds,
       {int((t1-t0)/60)} minutes, and
       {round((t1-t0)/3600,2)} hours
    """)
    
def stop():
    sys.exit("Script was intentially stopped by user")    


#------------------------------------------------------------------------------
# Convert dtypes
#------------------------------------------------------------------------------
def downcast(df, downcast_int=True, downcast_float=True):
    """
    Downcast numerical dtypes of dataframe
    """
    check_type(x=df,
               allowed=pd.DataFrame,
               name="df")
        
    if downcast_int:
        # Downcast to integer if possible
        df = df.apply(lambda x: pd.to_numeric(x, downcast='integer', errors="ignore"))

    if downcast_float: 
        # Downcast float if possible
        df = df.apply(lambda x: pd.to_numeric(x, downcast='float', errors="ignore"))
    
    return df

def upcast(df, upcast_int=True, upcast_float=True):
    """
    Upcast numerical dtypes of dataframe
    """
    check_type(x=df,
               allowed=pd.DataFrame,
               name="df")
        
    if upcast_int:
        # Upast to integer if possible
        df = df.apply(lambda x: x.astype(np.int64) if is_integer_dtype(x) else x)
        
    if upcast_float: 
        # Upcast float if possible
        df = df.apply(lambda x: x.astype(np.float64) if is_float_dtype(x) else x)
    
    return df

def convert_to_list(x):
    """Convert object "x" to list"""
    
    # List non-iterables and iterables. Note that we cannot rely on __iter__ attribute, because then str will be iterable!
    NON_ITERABLES = (str,numbers.Number)
    ITERABLES = (list, tuple, np.ndarray, pd.Series)
    
    if isinstance(x,NON_ITERABLES):
        x = [x]
    elif isinstance(x,ITERABLES):
        x = [i for i in x]
    else:
        try:
            x = [i for i in x]
        except:
            x = [x]
            
    return x

def convert_dict_values_to_list(d):
    """ Turn all values into list """
    check_type(x=d,allowed=dict,name="d")
    
    d = {key:(value if isinstance(value, list) else [value]) for key,value in d.items()}
    
    return d

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def intersect(l):
    """
    Find intersection of elements in list (typically list of lists)
    """
    check_type(x=l,allowed=list,name="l")
    
    l_intersect = list(set.intersection(*map(set,l)))
    
    return l_intersect
    
def subset_list(l, boolean_l):
    """
    Subset list based on another boolean list
    """
    check_type(x=l,allowed=list,name="l")
    check_type(x=boolean_l,allowed=list,name="boolean_l")
    
    if not len(l)==len(boolean_l):
        raise Exception(f"Length of 'l' (={len(l)}) must equal length of 'boolean_l' (={len(boolean_l)})")
    
    l_subset = list(itertools.compress(l, boolean_l))
    
    return l_subset

def unique_list(l):
    """
    Subset to unique elements of list while preserving order
    
    NB: Elements cannot be unhasable types (e.g., dict)
    """
    check_type(x=l,allowed=list,name="l")
    
    # Exclude duplicates but preserve order
    l = list(dict.fromkeys(l))
    
    return l

def drop_duplicates_in_list(l):
    """
    Verbatim unique_list()
    """
    return unique_list(l=l)
    

def compute_correlation(df, values, by=None, insert_info_cols=True):
    """
    Compute correlation between two columns in pd.DataFrame
    """
    check_type(x=df,allowed=pd.DataFrame,name="df")
    
    if by:
        df_corr = df.groupby(by=by)[values].corr().rename_axis(index={None:"DEL"})        
        df_corr.drop(labels=values[1], level="DEL", axis=0, inplace=True)
        df_corr.index = df_corr.index.droplevel("DEL")
        
    else:
        df_corr = df[values].corr()
        df_corr.drop(labels=values[1], axis=0, inplace=True)
        
    # Drop remainder
    df_corr.drop(labels=values[0], axis=1, inplace=True)
    
    # Rename
    df_corr.rename(columns={values[1]:'Correlation'}, inplace=True)

    if insert_info_cols:
        df_corr.insert(loc=0, column=values[1], value=values[1])
        df_corr.insert(loc=0, column=values[0], value=values[0])
    
    return df_corr

def isin(a, b, how="all", return_element_wise=True):
    """Check if any/all of the elements in 'a' is included in 'b'
    Note: Argument 'how' has NO EFFECT when 'return_element_wise=True'
    
    """
    HOW_OPT = ["all", "any"]

    # NB! We cannot use ".sanity_check.check_str" here, because it will lead to RecursionError: maximum recursion depth exceeded while calling a Python object
    # This is because ".sanity_check.check_str" itself uses isin.
    if not any(how==h for h in HOW_OPT):
        raise WrongInputException(x=how,
                                  allowed=HOW_OPT,
                                  name="how")
    
    # Convert "a" and "b" to lists
    a = convert_to_list(x=a)
    b = convert_to_list(x=b)

    # For each element (x) in a, check if it equals any element (y) in b
    is_in_temp = [any(x == y for y in b) for x in a]

    if return_element_wise:
        is_in = is_in_temp
    else:
        # Evaluate if "all" or "any" in found, when we only return one (!) answer
        if how=="all":
            is_in = all(is_in_temp)
        elif how=="any":
            is_in = any(is_in_temp)
                    
    if (len(a)==1) and isinstance(is_in, list):
        # Grab first and only argument if "a" is not iterable
        is_in = is_in[0]
            
    return is_in

def remove_empty_elements(d):
    """
    Remove empty elements from dict or list
    """
    if isinstance(d, dict):
        return dict((k, remove_empty_elements(v)) for k, v in d.items() if v and remove_empty_elements(v))
    elif isinstance(d, list):
        return [remove_empty_elements(v) for v in d if v and remove_empty_elements(v)]
    else:
        return d
    
    
def merge_multiply_dfs(l,
                       how='inner',
                       on=None,
                       left_on=None,
                       right_on=None,
                       left_index=False,
                       right_index=False,
                       sort=False,
                       suffixes=('_x', '_y'),
                       copy=True,
                       indicator=False,
                       validate=None):
    """
    Merge multiple pd.DataFrame
    """
    check_type(x=l, allowed=list,name="l")
    
    # Check if all elements are pd.dataframes
    if not all(isinstance(df,pd.DataFrame) for df in l):
        raise Exception("All elements in 'l' must be instances of pd.DataFrame")
        
    # Merge
    df_merged = reduce(lambda left,right: pd.merge(left,
                                                   right,
                                                   how=how,
                                                   on=on,
                                                   left_on=left_on,
                                                   right_on=right_on,
                                                   left_index=left_index,
                                                   right_index=right_index,
                                                   sort=sort,
                                                   suffixes=suffixes,
                                                   copy=copy,
                                                   indicator=indicator,
                                                   validate=validate
                                                   ), l)
    
    return df_merged




def print2(msg=""):
    
    print(
f"""
------------------------- MESSAGE -------------------------
{msg}
-----------------------------------------------------------
"""
        )
        
def insert_missing_rows_groupwise(df, groups, df_insert=None):
    """
    Insert rows with missing groups.
    E.g., if year 1 has observations 'a', and 'b', whereas year 2 has 'b' and 'c', then the merged data with have 'a', 'b', and 'c' for both year 1 and 2.
    """    
    # Pre-allocate list of mergeables
    mergeables = []
    
    for g in groups:
        # Get df of unique values
        df_mergeable = df[g].drop_duplicates().reset_index(drop=True)
        
        # Add key
        df_mergeable['key'] = "A"
        
        # Add to list of mergeable dfs
        mergeables.append(df_mergeable)
        
    if df_insert is not None:        
        # Add key to df to be inserted
        df_insert['key'] = "A"
            
        # Add to list of mergeable dfs
        mergeables.append(df_insert.drop_duplicates().reset_index(drop=True))
    
    # Get the number of unique rows needed
    nunique_rows = np.prod([len(d) for d in mergeables])

    # Construct data with all groups
    df_unique = merge_multiply_dfs(l=mergeables,on=['key'],how='outer') 

    # Remove key
    df_unique.drop(columns="key", inplace=True)
    
    # Sanity check
    if len(df_unique)!=nunique_rows:
        raise Exception("Creating the unique data to be merged with didn't work.")

    # Merge with unique data and thereby insert extra rows
    df_merged = df.merge(right=df_unique,
                         on=df_unique.columns.tolist(),
                         how="outer")
    
    return df_merged


def expand_df(df, by, non_observed=None):
    """
    Expand df by inserting extra rows groupwise that were missing.
    Additionally, provide extra unique values that are not observed in 'non_observed'.
    Note that if non_observed contains a DataFrame, the key should be the list of column names converted to a string, e.g., str(df.columns.tolist())
        
    E.g., if year 1 has observations 'a', and 'b', whereas year 2 has 'b' and 'c', then the merged data with have 'a', 'b', and 'c' for both year 1 and 2.
    """    
    KEY_COL = "KEY#€%"
    KEY_VAL = "A"
    
    check_type(x=df,
               allowed=pd.DataFrame,
               name="df")

    check_type(x=by,
               allowed=list,
               name="by")
        
    # Pre-allocate
    mergeables = {}

    # Get all unique groups    
    for b in by:
        
        # Convert to list if string
        if isinstance(b,str):
            b_name = b
            b=[b]
        else:
            b_name = str(b)
            
        # Get df of unique values
        df_mergeable = df[b].drop_duplicates().reset_index(drop=True)
        
        # Add key
        df_mergeable[KEY_COL] = KEY_VAL
        
        # Add to dict
        mergeables[str(b_name)] = df_mergeable
                
    if non_observed is not None:
        
        check_type(x=non_observed,
                   allowed=dict,
                   name="non_observed")
        
        for k,v in non_observed.items():            
            if not k in df.columns:
                raise Exception(f"Key '{k}' is not present in df {df.columns.tolist()}")

            check_type(x=v,
                       allowed=(pd.Series,pd.DataFrame),
                       name="v")

            if isinstance(v,pd.Series):
                df_mergeable =  v.to_frame(name=k)
            else:
                df_mergeable = v
                
            # Add key
            df_mergeable[KEY_COL] = KEY_VAL
                
            if k in mergeables.keys():
                
                mergeables[k] = pd.concat(objs=[mergeables[k],
                                                df_mergeable],
                                          axis=0,
                                          ignore_index=True).drop_duplicates()

            else:    
                mergeables[k] = df_mergeable.drop_duplicates()
        
    # Convert values to list
    mergeables = list(mergeables.values())
    
    # Get the number of unique rows needed
    nunique_rows = np.prod([len(d) for d in mergeables])

    # Construct data with all groups
    df_unique = merge_multiply_dfs(l=mergeables,on=[KEY_COL],how='outer') 

    # Remove key
    df_unique.drop(columns=KEY_COL, inplace=True)
    
    # Sanity check
    if len(df_unique)!=nunique_rows:
        raise Exception("Creating the unique data to be merged with didn't work.")

    # Columns to merge by
    merge_by = df_unique.columns.tolist()

    # Merge with unique data and thereby insert extra rows
    df_merged = df.merge(right=df_unique,
                         on=merge_by,
                         how="outer")
    df_merged.sort_values(by=merge_by, inplace=True)
    
    
    return df_merged




    