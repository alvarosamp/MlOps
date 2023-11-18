from main import app
from fastapi.testclient import TestClient
import pytest
import requests
import json
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning) 

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Welcome to Loan Prediction App using API - CI CD Jenkins"}


data = {
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}

def test_pred_():
  response = client.post("/prediction_api", json=data)
  assert response.json()["status"] != ''
  assert response.json() == {"status": "Approved"}