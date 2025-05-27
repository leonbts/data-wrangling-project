def extract_payload_info(df):
    payload_types = []
    orbits = []
    
    for payloads in df['payloads']:
        types = []
        orbits_for_launch = []
        
        if payloads:
            for p in payloads:
                p_type = p.get('type', 'Unknown')
                orbit = p.get('orbit', 'Unknown')
                types.append(p_type)
                orbits_for_launch.append(orbit)
        else:
            types.append('Unknown')
            orbits_for_launch.append('Unknown')
        
        payload_types.append(", ".join(types))
        orbits.append(", ".join(orbits_for_launch))
    
    df['payload_types'] = payload_types
    df['orbits'] = orbits
    return df

def clean_success_column(df):
    df['success'] = df['success'].fillna(False).astype(bool)
    return df