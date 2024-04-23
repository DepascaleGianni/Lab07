from database.meteo_dao import MeteoDao
class Model:
    def __init__(self):
        self.m_dao = MeteoDao()
        self._datas = []
        self.sequence = []
        self.optimal_cost = 10000000

    def get_humidity_in_month(self,month):
        return self.m_dao.get_humidity_in_month(month)

    def get_datas_to_analyse(self,month):
        self._datas = self.m_dao.get_humidity_date_and_city(month)

    def analyse(self,partial = []):
        if len(partial) == 15:
            cost = self.calculate_cost(partial)
            if cost < self.optimal_cost:
                self.optimal_cost = cost
                self.sequence = partial
                return
        else:
            for s in self._datas[len(partial)*3::len(partial)*3+3]:
                partial.append(s)
                if self.is_admissible(partial):
                    self.analyse(partial)
                partial.pop(len(partial)-1)

    def calculate_cost(seq : list):
        costo = 0
        giorno = 0
        cambiata = False
        while giorno <= 15:
            if giorno == 0:
                costo += seq[giorno].umidita
                giorno += 1
            else:
                if seq[giorno].localita == seq[giorno-1].localita:
                    if cambiata == True:
                        costo += seq[giorno].umidita + 100
                        cambiata = False
                    else:
                        costo += seq[giorno].umidita
                else:
                    costo += seq[giorno].umidita + 100
                    cambiata = True
                giorno += 1
        return costo

    def is_admissible(self,seq : list):
        seq_cities = [s.localita for s in seq]
        cities = set(seq_cities)
        for city in cities:
            giorno = 0
            tot_count = 0
            while giorno <= len(seq):
                if seq_cities[giorno] == city:
                    tot_count += 1
            if tot_count > 6:
                return False

        giorno = 0
        consecutive = []
        while giorno <= len(seq):
            consecutive.append(seq_cities[giorno])
            if len(consecutive) == 3:
                if len(set(consecutive)) == 1:
                    return False
                else:
                    consecutive.clear()
            giorno += 1
        return True

if __name__ == '__main__':
    m = Model()
    m.get_datas_to_analyse(1)
    print(m.analyse())
