from .models import *
# Create your views here.
import sys
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .create_log import create_log
from .RuBertSentiment import predict

api_log = create_log("api.log", "api")
@csrf_exempt
def api(request):
	if request.method == "GET":
		return HttpResponse("Панель API классификатора")
	if request.method == "POST":
		resp = {}
		key = request.POST.get("key")
		action = request.POST.get("action")

		# api_log.info(str(request.POST))
		# credentials = UserApiCredentials.objects.filter(key = key).first()
		# if not credentials:
		# 	resp["error"] = "Invalid credentials"
		# 	api_log.error("Invalid credentials")
		# 	return JsonResponse(resp)	

		if action == "classify":
			return classify(request)

		resp["error"] = "No such action"
		api_log.error("No such action")
		return JsonResponse(resp)
@csrf_exempt
def classify(request):
	review = request.POST.get("review")
	api_log.error(str(review))
	probs, classes = predict(review)
	result = {
        "predicted_class": int(classes[0]),
        "probabilities": probs.tolist()
    }
	return JsonResponse({'status' : 'success', 'review' : review, 'result' : result})

def test(request):
	return render(request, 'test.html')


