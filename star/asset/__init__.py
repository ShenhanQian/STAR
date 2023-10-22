from pathlib import Path


ROOT_DIR = Path(__file__).parent

# could be downloaded in this repo: https://github.com/italojs/facial-landmarks-recognition/tree/master
predictor_path = str(ROOT_DIR / 'shape_predictor_68_face_landmarks.dat')

# could be downloaded here: https://drive.google.com/file/d/1aOx0wYEZUfBndYy_8IYszLPG_D2fhxrT/view
model_path = str(ROOT_DIR / '300W_STARLoss_NME_2_87.pkl')