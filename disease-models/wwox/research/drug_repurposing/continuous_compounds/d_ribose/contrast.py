"""Recalculate the comparisons from the published summaries; see exposure.md."""
import csv
import sys

writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
writer.writerow(['source', 'comparison', 'value', 'unit'])

def report(source, comparison, value, unit):
    writer.writerow([source, comparison, f'{value:.4f}', unit])

# mg/dL times ten gives mg/L; D-ribose molecular weight is 150.13 mg/mmol.
for route, mg_dl in [('oral', 4.8), ('IV', 81.7)]:
    report('Gross_1989', f'{route}_steady_state', mg_dl * 10 / 150.13, 'mmol/L_serum')
for meal, cmax_loss, auc_loss in [('high_fat', 42.6, 40.8), ('high_carbohydrate', 69.1, 64.9)]:
    report('Thompson_2014', f'{meal}_Cmax_retained', 100 - cmax_loss, 'percent_of_fasting')
    report('Thompson_2014', f'{meal}_AUC_retained', 100 - auc_loss, 'percent_of_fasting')
for time, c1, c3 in [('15min', 30.1, 66.7), ('2h', 31.4, 65.4)]:
    report('Hiatt_1958_Table1', f'{time}_glucose_C1_plus_C3', c1+c3, 'percent_of_glucose_radiocarbon')
report('zur_Nedden_thesis_Fig8.4', 'pretreatment_dead_cells_ribose_minus_OGD', 37-58, 'percentage_points')
for burst, combination, control in [('second', 107.8, 76.5), ('third', 93.2, 63.5)]:
    report('hall_2018_Fig5c', f'{burst}_interburst_interval_combination_minus_control',
           combination - control, 'seconds')
