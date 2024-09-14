import inspect


def introspection_info(obj):

    # Определяем тип объекта и выводим его в удобочитаемый вид
    tp = str(type(obj))
    tp = tp.split()
    tp = tp[1]
    tp = tp.replace('>', '')

    # Получаем атрибуты и методы и разделяем их по спискам через фильтр на __
    attr = []
    meth = []
    loatr = dir(obj)
    for i in loatr:
        if '__' in i:
            meth.append(i)
        else:
            attr.append(i)

    # Определяем модуль к которому принадлежит объект
    mod = str(inspect.getmodule(introspection_info))
    mod = mod.split()
    mod = mod[1]

    # Выводим результаты в удобочитаемом виде
    return {'type': tp.strip("'"), 'attributes': attr, 'methods': meth, 'module': mod.strip("'")}


number_info = introspection_info(42)
print(number_info)
