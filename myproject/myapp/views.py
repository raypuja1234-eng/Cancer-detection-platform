from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np
import os

# -----------------------------------------------------------------------
# Load the cancer detection model once at startup
# -----------------------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cancer_model.pkl')
cancer_model = joblib.load(MODEL_PATH)

# -----------------------------------------------------------------------
# Views
# -----------------------------------------------------------------------

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def analysis(request):
    return render(request, "analysis.html")

def ourteam(request):
    return render(request, "ourteam.html")

def prediction(request):
    return render(request, "prediction.html")

def pred(request):
    if request.method == 'POST':
        try:
            radius_mean  = float(request.POST['radius_mean'])
            texture_mean = float(request.POST['texture_mean'])

            # Run the ML model
            features = np.array([[radius_mean, texture_mean]])
            result   = cancer_model.predict(features)[0]           # 'M' or 'B'
            proba    = cancer_model.predict_proba(features)[0]     # [prob_B, prob_M]

            # Build context
            is_malignant   = (result == 'M')
            confidence_pct = round(max(proba) * 100, 2)

            context = {
                'result':         'Malignant' if is_malignant else 'Benign',
                'is_malignant':   is_malignant,
                'confidence':     confidence_pct,
                'radius_mean':    radius_mean,
                'texture_mean':   texture_mean,
            }
            return render(request, 'result.html', context)

        except (ValueError, KeyError) as e:
            return render(request, 'prediction.html', {'error': 'Invalid input. Please enter valid numbers.'})

    # GET request — redirect back to the form
    return render(request, 'prediction.html')
