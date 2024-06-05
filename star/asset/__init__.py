from pathlib import Path
import gdown


CACHE_DIR = Path.home() / '.cache' / 'STAR'
if not CACHE_DIR.exists():
    CACHE_DIR.mkdir(parents=True)

# could be downloaded in this repo: https://github.com/italojs/facial-landmarks-recognition/tree/master
predictor_path = CACHE_DIR / 'shape_predictor_68_face_landmarks.dat'
predictor_url = 'https://raw.githubusercontent.com/italojs/facial-landmarks-recognition/master/shape_predictor_68_face_landmarks.dat'
if not predictor_path.exists():
    gdown.download(predictor_url, str(predictor_path))

# could be downloaded here: https://drive.google.com/file/d/1NFcZ9jzql_jnn3ulaSzUlyhS05HWB9n_/view
model_path = CACHE_DIR / '300W_STARLoss_NME_2_87.pkl'
model_url = "https://drive.google.com/uc?id=1NFcZ9jzql_jnn3ulaSzUlyhS05HWB9n_"
if not model_path.exists():
    print(f"Downloading from {model_url} to {model_path}...")
    gdown.download(model_url, str(model_path))

predictor_path = str(predictor_path)
model_path = str(model_path)