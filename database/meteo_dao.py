from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():
    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    def get_humidity_in_month(self,month):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor()
            query = """ SELECT s.Localita, AVG(s.Umidita)
                    FROM situazione as s
                    WHERE MONTH(s.Data) = %s
                    GROUP BY s.Localita"""
            cursor.execute(query,(month,))
            for city,avg_humidity in cursor:
                result.append((city,avg_humidity))
            cursor.close()
            cnx.close()
        return result

    def get_humidity_date_and_city(self,month):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                                FROM situazione s
                                WHERE (MONTH(s.Data) = %s)
                                ORDER BY s.Data ASC 
                                """
            cursor.execute(query,(month,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result


# if __name__ == '__main__':
#     m = MeteoDao()
#     print([el for el in m.get_humidity_date_and_city(1)])
#     print(m.get_humidity_date_and_city(1)[0])
