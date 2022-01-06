
condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

linguagem = 'Java'


if linguagem == 'Python':
    print('Linguagem eh Python')
elif linguagem == 'Java':
    print('Linguagem eh Java')
elif linguagem == 'JavaScript':
    print('Linguagem eh JavaScript')
else:
    print('Sem correspondencia')

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')