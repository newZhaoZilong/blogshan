import re



postData = {
    'search':'nihao'
}


isSearch = postData.get('search')
search_reg = re.compile(isSearch)

if not (search_reg.search('nihao') or search_reg.search('nihao')):
    print('存在')

else:
    print('不存在')