from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import DataBase


def keyword_finder(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search.find('.') != -1:
            # print("Contains given substring ")

            url = 'https://' + search
            # print(url)
            headers = {
                "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
            }

            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            source_keyword = soup.find('meta', attrs={'name': 'keywords'})
            str_keyword = str(source_keyword)
            final_keyword = str_keyword[15:len(str_keyword) - 19]

            source_dec = soup.find("meta", property="og:description")
            str_dec = str(source_dec)
            final_dec = str_dec[15:len(str_dec) - 29]

            source_img = soup.find("meta", property="og:image")
            str_img = str(source_img)
            final_img = str_img[15:len(str_img) - 23]

            source_type = soup.find("meta", property="og:type")
            str_type = str(source_type)
            final_type = str_type[15:len(str_type) - 22]

            source_csrf = soup.find('meta', attrs={'name': 'csrf-token'})
            str_csrf = str(source_csrf)
            final_csrf = str_csrf[15:len(str_csrf) - 21]
            if DataBase.objects.filter(url=url):
                print('PASS')
            else:
                data = DataBase()
                data.url = url
                data.keywords = final_keyword
                data.img_url = final_img
                data.type = final_type
                data.csrf_code = final_csrf
                data.description = final_dec

                data.save()

            obj = DataBase.objects.all()

            db_keywords_list = []
            db_url_list = []
            for i in obj:
                db_keywords_list.append(i.keywords)
                db_url_list.append(i.url)
            note = 'The KeyWord are Present in '
            # query = 'SELECT * FROM keywordfinder_database WHERE keywords LIKE %s', [search]
            px = []
            for p in DataBase.objects.raw('SELECT * FROM keywordfinder_database'):
                # print(p.keywords)
                px.append(p.keywords)
            matching_px = [i for i in px]
            dummy_keyword = final_keyword
            keyword_list = dummy_keyword.split(',')

            matching = [s for s in matching_px if keyword_list[0] in s]
            # result = matching[]-keywords_list[]

            result_list = [i for i in matching if i in keyword_list[0]]
            print(result_list)

            meta_data = {'keyword': final_keyword,
                         'dec': final_dec,
                         'img': final_img,
                         'type': final_type,
                         'csrf': final_csrf,
                         'url': url,
                         'text': matching,
                         'note': note
                         }

            return render(request, 'keywordfinder/keyword_finder.html', meta_data)

        else:

            return render(request, 'keywordfinder/keyword_finder.html', {'text': 'matching', 'note': 'note',
                                                                         })

    else:
        return render(request, 'keywordfinder/keyword_finder.html')


'''
            for p in DataBase.objects.raw('SELECT * FROM keywordfinder_database WHERE keywords LIKE %s', [search]):

'''
