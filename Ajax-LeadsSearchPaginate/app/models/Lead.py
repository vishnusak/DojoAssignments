from system.core.model import Model

class Lead(Model):
    def __init__(self):
        super(Lead, self).__init__()
        self.__query = ''
        self.__db = {}

    def __run_query(self, query, data):
        return self.db.query_db(query, data)

    def get_count(self):
        self.__query = "SELECT count(*) as count FROM leads"
        self.__data = {}
        return self.__run_query(self.__query, self.__data)[0]['count']

    def get_page(self, page_num, limit):
        offset = (limit * (page_num - 1))
        self.__query = "SELECT leads_id, first_name, last_name,  date_format(registered_datetime, '%Y-%m-%d') as date, email FROM leads ORDER BY leads_id LIMIT :offset, :limit"
        self.__data = {
            'offset': offset,
            'limit': limit
        }
        return self.__run_query(self.__query, self.__data)

    def get_filter_count(self, form):
        self.__query = "SELECT count(*) as count FROM leads"
        name = form['name']+'%'

        if form['from']:
            from_date = form['from']

            if form['to']:
                to_date = form['to']

                self.__query = "SELECT count(*) as count FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') between :from_date and :to_date"
            else:
                to_date = ''

                self.__query = "SELECT count(*) as count FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') >= :from_date"
        else:
            from_date = ''

            if form['to']:
                to_date = form['to']

                self.__query = "SELECT count(*) as count FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') <= :to_date"
            else:
                to_date = ''

                self.__query = "SELECT count(*) as count FROM leads WHERE (first_name LIKE :name or last_name LIKE :name)"

        self.__data = {
            'name': name,
            'from_date': from_date,
            'to_date': to_date
        }
        return self.__run_query(self.__query, self.__data)[0]['count']

    def get_filter_page(self, page_num, limit, form):
        offset = (limit * (page_num - 1))
        name = form['name']+'%'

        if form['from']:
            from_date = form['from']

            if form['to']:
                to_date = form['to']

                self.__query = "SELECT leads_id, first_name, last_name,  date_format(registered_datetime, '%Y-%m-%d') as date, email FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') between :from_date and :to_date ORDER BY leads_id LIMIT :offset, :limit"
            else:
                to_date = ''

                self.__query = "SELECT leads_id, first_name, last_name,  date_format(registered_datetime, '%Y-%m-%d') as date, email FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') >= :from_date ORDER BY leads_id LIMIT :offset, :limit"
        else:
            from_date = ''

            if form['to']:
                to_date = form['to']

                self.__query = "SELECT leads_id, first_name, last_name,  date_format(registered_datetime, '%Y-%m-%d') as date, email FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) AND date_format(registered_datetime, '%Y-%m-%d') <= :to_date ORDER BY leads_id LIMIT :offset, :limit"
            else:
                to_date = ''

                self.__query = "SELECT leads_id, first_name, last_name,  date_format(registered_datetime, '%Y-%m-%d') as date, email FROM leads WHERE (first_name LIKE :name or last_name LIKE :name) ORDER BY leads_id LIMIT :offset, :limit"

        self.__data = {
            'offset': offset,
            'limit': limit,
            'name': name,
            'from_date': from_date,
            'to_date': to_date
        }
        return self.__run_query(self.__query, self.__data)
