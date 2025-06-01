import numpy as np
import pandas as pd
import ast

def extract_payload_info(df_launches):
    """
    Extracts payload types and orbit types from the nested payloads column.
    Handles missing values and ensures all items are strings.
    """
    payload_types = []
    orbits = []

    for payloads in df_launches['payloads']:
        types = []
        orbit_types = []

        if isinstance(payloads, list):
            for p in payloads:
                p_type = str(p.get('type') or 'Unknown')
                orbit = str(p.get('orbit') or 'Unknown')
                types.append(p_type)
                orbit_types.append(orbit)
        else:
            types.append('Unknown')
            orbit_types.append('Unknown')

        payload_types.append(", ".join(types))
        orbits.append(", ".join(orbit_types))

    df_launches['payload_types'] = payload_types
    df_launches['orbits'] = orbits
    return df_launches


def extract_payload_mass(payloads):
    if not isinstance(payloads, list):
        return None
    masses = []
    for payload in payloads:
        mass = payload.get('mass_kg')
        if isinstance(mass, (int, float)):
            masses.append(mass)
    return sum(masses) if masses else None


def clean_success_column(df_launches):
    """
    Cleans the 'success' column:
    - Keeps missing/None values as NaN
    - Converts non-null values explicitly to boolean
    """
    df_launches['success'] = df_launches['success'].apply(lambda x: bool(x) if pd.notnull(x) else np.nan)
    return df_launches


def merge_launchpads(launches_df, launchpads_df):
    merged_df = launches_df.merge(
        launchpads_df,
        how='left',
        left_on='launchpad',
        right_on='id'
    )
    return merged_df