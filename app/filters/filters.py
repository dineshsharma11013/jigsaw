def status_filter(value):
    return "Active" if value == 1 else "Inactive"

def uppercase(value):
    return value.upper()

def truncate(value, length=10):
    return value[:length] + "..." if len(value) > length else value

def register_filters(app):
    app.add_template_filter(status_filter, 'status_filter')
    app.add_template_filter(uppercase, 'uppercase')
    app.add_template_filter(truncate, 'truncate')
