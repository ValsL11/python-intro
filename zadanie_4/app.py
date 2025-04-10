import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm import normalizations, weights

# kryteria (koszt, jakość, czas)
decision_matrix = np.array([
  [30000, 7.5, 12],   
  [25000, 8.0, 14],   
  [27000, 6.0, 10],   
  [29000, 7.0, 11],   
])

weights_vector = weights.entropy_weights(decision_matrix)

# koszt i czas – minimalizujemy, jakość – maksymalizujemy
criteria_types = ['min', 'max', 'min']
criteria_types_num = np.array([1 if t == 'max' else -1 for t in criteria_types])

normalized_matrix = normalizations.minmax_normalization(decision_matrix, criteria_types)

bounds = np.array([[decision_matrix[:, j].min(), decision_matrix[:, j].max()] for j in range(decision_matrix.shape[1])])

topsis = TOPSIS()
spotis = SPOTIS(bounds)

topsis_result = topsis(decision_matrix, weights_vector, criteria_types)
spotis_result = spotis(decision_matrix, weights_vector, criteria_types_num)

alternatives = ['A1', 'A2', 'A3', 'A4']
results_df = pd.DataFrame({
  'Alternatywa': alternatives,
  'Wynik TOPSIS': topsis_result,
  'Pozycja TOPSIS': topsis_result.argsort()[::-1].argsort() + 1,
  'Wynik SPOTIS': spotis_result,
  'Pozycja SPOTIS': spotis_result.argsort().argsort() + 1
})

print(results_df)