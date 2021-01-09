from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,art):
    """
    This cuts out all values of "arg" from the string!
    
    """
    return value.replace(art,'')


# register.filter('cut',cut)