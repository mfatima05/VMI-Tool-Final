def format_bytes(size):
    """Format bytes as human-readable string."""
    if size == 0:
        return "0 Bytes"
    unit = 1024
    for x in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < unit:
            return f"{size:.2f} {x}"
        size /= unit

def print_dict(d):
    """Print dictionary in a formatted way."""
    for key, value in d.items():
        print(f"{key}: {value}")
