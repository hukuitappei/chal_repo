def reverse_dict(input_dict):
    try:
        output_dict = {v: k for k, v in input_dict.items()}
    except Exception:
        return None                
    if len(input_dict) != len(output_dict):
        return None
    return output_dict
