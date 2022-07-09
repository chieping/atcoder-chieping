def run_length(orig):
    """ランレングス圧縮"""
    return [[key, len(list(group))] for key, group in groupby(orig)]
