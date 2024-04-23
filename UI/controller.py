import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        avg_humidity = self._model.get_humidity_in_month(self._mese)
        self._view.lst_result.controls.clear()
        if len(avg_humidity) != 3:
            self._view.lst_result.controls.append(ft.Text("Datas are not complete"))
        elif self._mese == 0:
            self._view.lst_result.controls.append(ft.Text("Please select a month"))
        else:
            for row in avg_humidity:
                self._view.lst_result.controls.append(ft.Text(f"{row[0]} : {row[1]}"))
        self._view.update_page()

    def handle_sequenza(self, e):
        self._view.lst_result.controls.append(ft.Text("Ciao"))
        self._model.get_datas_to_analyse(self._mese)
        self._model.analyse()
        results = self._model.sequence
        optimal_cost = str(self._model.optimal_cost)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(value=optimal_cost))
        for row in results:
            self._view.lst_result.controls.append(ft.Text(row.__str__))
        self._view.update_page()


    def read_mese(self, e):
        self._mese = int(e.control.value)

if __name__ == '__main__':
    c = Controller()
    c.handle_sequenza()
