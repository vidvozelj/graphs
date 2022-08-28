from functions import file_manager
from datetime import datetime
from matplotlib import pyplot as plt, dates
import matplotlib.dates as mdates

#<------------------Insert graph parameters here <3 <3 <3 ------------------------->

file_name = "Podatki_ogrevalna_sezona.xlsx" # Prekopiraj ime Excel datoteke (vkljucno z koncnico) - Ime se mora popolnoma ujemati
sheet_name = "SMPS-delci_evaluacija" # Prekopiraj ime strani v Excelu s podatki

x_axis = "A" # Vstavi ime stolpca, ki vsebuje podatke za x-os Oblika: "Ime stolpca"
x_axis_label = "Datum, Ura" # Ime x-osi Oblika: "Ime osi"

y_axes = ["AH", "AP", "BA", "AX"] # Vstavi stolpce, ki vsebujejo podatke za y-osi Oblika: ["Ime 1. stolpca", "Ime 2. stolpca",...]
y_axes_colum_numbers = [4, 200] # Napisi mejne vrstici tabele (zacetna in koncna vrstica) Oblika: [stevilka_1, stevilka_2]

line_colors = ['r', 'g', 'b', "m"] # Vstavi barve linij grafov (st. barvo mora biti enako st. y-osi) Oblika: "barva" (b : blue, g : green, r : red, c : cyan, m : magenta, y : yellow, k : black, w : white)
y_axis_labels = ["neki", "drugo", "tretje", "bla bla"] # Vstavi imena y-osi (st. barvo mora biti enako st. y-osi) Oblika: ["Ime 1. y-osi", "Ime 2. y-osi",...]

squere_borders = [['3/27/2022 21:00', '3/28/2022 3:00'], ['3/28/2022 6:00', '3/28/2022 12:00']] # Vstavi meje kvadratov Oblika: [["spodnja_meja_1", "zgornja_meja_1"], ["spodnja_meja_2", "zgornja_meja_2"],...]

#<------------------------------------------->

#<----START-get data-------------------->
y_axes_data = []
x_axis_data = []

worksheet = file_manager.open_excel_file(file_name, sheet_name)

for value in range(y_axes_colum_numbers[0], y_axes_colum_numbers[1] + 1):
    x_axis_data.append(datetime.strptime(worksheet[f"{x_axis}{value}"].value, '%m/%d/%Y %H:%M:%S'))

for y_axis in y_axes:
    y_axis_data = []
    for value in range(y_axes_colum_numbers[0], y_axes_colum_numbers[1] + 1):
        y_axis_data.append(round(worksheet[f"{y_axis}{value}"].value, 2))
    y_axes_data.append(y_axis_data)
#<----END-get data-------------------->

fig, ax = plt.subplots(nrows=len(y_axes), ncols=1, sharex=True)
lines = []

for _ in range(len(y_axes)):
    y = y_axes_data[_]
    lines.append(ax[_].plot(x_axis_data, y, color=line_colors[_]))
    ax[_].grid()
    ax[_].set_ylabel(y_axis_labels[_])
    ax[_].set_xlabel(x_axis_label)
    if len(squere_borders) > 0:
        for squere in squere_borders:
            ax[_].axvspan(*mdates.datestr2num(squere), color='blue', alpha=0.2)
    if _ == 0:
        ax[_].xaxis.set_major_formatter(dates.DateFormatter('%d/%m %H:00'))

plt.subplots_adjust(hspace=.0)

plt.show()
