# import words
#
# text = 'реДиска Дом редиСКа ornoesring wkemfoweimf ЖОПА'
#
#
# def censor(x):
#     text_1 = ''
#     if isinstance(x, str):
#         for i in x.split():
#             # i = i.lower()
#             if i.lower() in words.WORDS:
#                 text_1 += i.replace(i, f'  {i[0]}{"*" * (len(i) - 1)}   ')
#             else:
#                 text_1 += '   ' + i + '   '
#         text_1 = ' '.join(text_1.split())
#         return text_1
#
#
# a = censor(text)
# print(a)
