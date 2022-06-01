import pandas as pd
import numpy as np

naics = pd.read_excel("data/2022_NAICS_Descriptions.xlsx")

naics['Code'] = naics['Code'].astype(str)
naics['Title'] = naics['Title'].str.replace("T$","",regex=True)
for idx in naics.loc[naics['Code'].str.contains('-')].index:
    s_codes = naics.loc[idx,'Code'].split('-')
    s_row = naics.loc[[idx]]
    for s_code in list(range(int(s_codes[0]),int(s_codes[1])+1)):
        s_row['Code'] = str(s_code)
        naics = pd.concat([naics,s_row])
naics = naics.loc[~naics['Code'].str.contains('-')]

def naics_lookup(naics_code):
    """
    Translate one naics code to all titles of sectors and industries

    Args:
        naics_code (str,int): valid naics code
    
    Returns:
        array: naics titles
    """
    naics_code = str(naics_code)
    subCodes = [naics_code[:2],naics_code[:3],naics_code[:4],naics_code[:5],naics_code]
    titles = naics.loc[naics['Code'].isin(subCodes),'Title'].drop_duplicates().values
    return titles

def naics2sectors(naics_codes):
    """
    Translate naics codes to sector titles

    Args:
        naics_code : array of naics codes
    
    Returns:
        list: naics sector titles
    """
    res = []
    if not hasattr(naics_codes, '__iter__'):
        naics_codes = [naics_codes]
    for naics_code in naics_codes:
        titles = naics_lookup(naics_code)
        res.append(np.nan if len(titles)<1 else titles[0])
    return res

def naics2industries(naics_codes):
    """
    Translate naics codes to industry titles

    Args:
        naics_code : array of naics codes
    
    Returns:
        list: naics industry titles
    """
    res = []
    if not hasattr(naics_codes, '__iter__'):
        naics_codes = [naics_codes]
    for naics_code in naics_codes:
        naics_code_str = str(naics_code)
        titles = naics_lookup(naics_code_str)
        res.append(np.nan if len(titles)<1 else titles[-1])
    return res

