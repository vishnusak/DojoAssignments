from system.core.controller import *
import time

class Leads(Controller):
    def __init__(self, action):
        super(Leads, self).__init__(action)
        self.load_model('Lead')
        self.__db = self.models['Lead']
        self.__details = {}
        self.__paginate = {}

    def __get_dtl(self, page_num, limit=19):
        count = self.__db.get_count()
        pages = ((count / limit) if (count % limit == 0) else (count / limit) + 1)
        data = self.__db.get_page(page_num, limit)

        self.__paginate = {
        'pages': pages,
        'cur': page_num
        }

        self.__details = {
        'leads': data
        }

    def __filter_dtl(self, form, page_num=1, limit=19):
        count = self.__db.get_filter_count(form)
        pages = ((count / limit) if (count % limit == 0) else (count / limit) + 1)
        data = self.__db.get_filter_page(page_num, limit, form)

        self.__paginate = {
        'pages': pages,
        'cur': page_num
        }

        self.__details = {
        'leads': data
        }

    def index(self):
        page_num = 1
        self.__get_dtl(page_num)
        return self.load_view('leads.html', dtl = self.__details, pg = self.__paginate, today = time.strftime('%Y-%m-%d'))

    def another_page(self, page_num):
        form = request.form
        self.__details = {}

        if form['name'] or form['from'] or form['to']:
            self.__filter_dtl(form, page_num)
        else:
            self.__get_dtl(page_num)

        page_resp = self.load_view('paginate.html', pg = self.__paginate)
        dtl_resp = self.load_view('details.html', dtl = self.__details)
        return jsonify(page=page_resp,details=dtl_resp)

    def filter_page(self):
        self.__details = {}
        self.__filter_dtl(request.form)
        page_resp = self.load_view('paginate.html', pg = self.__paginate)
        dtl_resp = self.load_view('details.html', dtl = self.__details)
        return jsonify(page=page_resp,details=dtl_resp)
