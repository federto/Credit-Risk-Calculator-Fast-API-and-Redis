from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from schemas import form,login
from middleware import model_predict
from controller.user import User
from lib.check_passw import check_user
import uvicorn
import os
import settings


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(req: Request):
  return templates.TemplateResponse("index.html", {"request": req})
  

@app.post("/", response_class=HTMLResponse)
def root(req: Request):
  return templates.TemplateResponse("index.html", {"request": req})


@app.get("/signup",response_class=HTMLResponse)
async def signup(request:Request):
    return templates.TemplateResponse('signup.html',{'request':request})

@app.get("/user", response_class=HTMLResponse)
def user(req: Request):

  return RedirectResponse("/")


@app.post("/user", response_class=HTMLResponse)
def user(req: Request, username: str = Form(), password_user: str = Form()):
  verify = check_user(username, password_user)
  if verify:
    return templates.TemplateResponse("credit_risk.html", {"request": req, "data_user": verify})
  
  return RedirectResponse("/")

@app.post("/data-processing")
def data_processing(form_login: login = Depends(login.as_login)):
  data_user = {
    "firstname": form_login.firstname,
    "lastname": form_login.lastname,
    "username": form_login.username,
    "password_user": form_login.password_user
  }
  db = User(data_user)
  db.create_user()


  return RedirectResponse("/")


@app.get("/credit-risk",response_class=HTMLResponse)
async def credit_risk_bootstrap(request:Request):
    return templates.TemplateResponse('credit_risk.html',{'request':request})


@app.post("/credit-risk",response_class=HTMLResponse)
async def credit_risk(request: Request, form_data: form = Depends(form.as_form)):

    credit_dict = get_credit_dict(form_data)

    predict_score = model_predict(credit_dict)
    return templates.TemplateResponse("report.html", {"request": request ,'form_data':form_data, 'Score':predict_score["Score"],"Result":predict_score["Result"]})

@app.post("/feedback",response_class=HTMLResponse)
async def feedback(request: Request,form_data: form = Depends(form.as_form)):

    credit_dict_feedback = get_credit_dict(form_data)
    credit_dict_csv = credit_dict_to_csv(credit_dict_feedback)
    with open(settings.FEEDBACK_FILEPATH, 'a') as plain_text: 

        plain_text.write(credit_dict_csv + '\n')

    plain_text.close()
    return templates.TemplateResponse("thanks.html",{"request":request})

def get_credit_dict(form_data):
    return {'PAYMENT_DAY':form_data.payment_day,'APPLICATION_SUBMISSION_TYPE':form_data.application_submission_type,
    'POSTAL_ADDRESS_TYPE':form_data.postal_adress_type,'SEX':form_data.sex,
'MARITAL_STATUS':form_data.marital_status,'QUANT_DEPENDANTS':form_data.quant_dependants,'STATE_OF_BIRTH':form_data.state_of_birth,
'CITY_OF_BIRTH':form_data.city_of_birth,'NACIONALITY':form_data.nacionality,
'RESIDENCIAL_STATE':form_data.residencial_state,'RESIDENCIAL_CITY':form_data.residencial_city,
'RESIDENCIAL_BOROUGH':form_data.residencial_borough,'FLAG_RESIDENCIAL_PHONE':form_data.flag_residencial_phone,
'RESIDENCIAL_PHONE_AREA_CODE':form_data.residencial_phone_area_code,'RESIDENCE_TYPE':form_data.residence_type,
'MONTHS_IN_RESIDENCE':form_data.months_in_residence,'FLAG_EMAIL':form_data.flag_email,
'PERSONAL_MONTHLY_INCOME':form_data.personal_monthly_income,'OTHER_INCOMES':form_data.other_incomes,
'FLAG_VISA':form_data.visa,'FLAG_MASTERCARD':form_data.mastercard,'FLAG_DINERS':form_data.diners,
'FLAG_AMERICAN_EXPRESS':form_data.american_express,'FLAG_OTHER_CARDS':form_data.others_cards,
'QUANT_BANKING_ACCOUNTS':form_data.quant_banking_accounts,'PERSONAL_ASSETS_VALUE':form_data.personal_assets_value,
'QUANT_CARS':form_data.quant_cars,'COMPANY':form_data.company,'FLAG_PROFESSIONAL_PHONE':form_data.flag_professional_phone,
'MONTHS_IN_THE_JOB':form_data.months_in_job,'PROFESSION_CODE':form_data.profession_code,
'OCCUPATION_TYPE':form_data.occupation_type,'PRODUCT':form_data.product,'AGE':form_data.age,'RESIDENCIAL_ZIP_3':form_data.residencial_zip}

def credit_dict_to_csv(credit_dict):
    return (f"{credit_dict['PAYMENT_DAY']},{credit_dict['APPLICATION_SUBMISSION_TYPE']},{credit_dict['POSTAL_ADDRESS_TYPE']},"\
    f"{credit_dict['SEX']},{credit_dict['MARITAL_STATUS']},{credit_dict['QUANT_DEPENDANTS']},{credit_dict['STATE_OF_BIRTH']},"\
    f"{credit_dict['CITY_OF_BIRTH']},{credit_dict['NACIONALITY']},{credit_dict['RESIDENCIAL_STATE']},{credit_dict['RESIDENCIAL_CITY']},"\
    f"{credit_dict['RESIDENCIAL_BOROUGH']},{credit_dict['FLAG_RESIDENCIAL_PHONE']},{credit_dict['RESIDENCIAL_PHONE_AREA_CODE']},"\
    f"{credit_dict['RESIDENCE_TYPE']},{credit_dict['MONTHS_IN_RESIDENCE']},{credit_dict['FLAG_EMAIL']},"\
    f"{credit_dict['PERSONAL_MONTHLY_INCOME']},{credit_dict['OTHER_INCOMES']},{credit_dict['FLAG_VISA']},"\
    f"{credit_dict['FLAG_MASTERCARD']},{credit_dict['FLAG_DINERS']},{credit_dict['FLAG_AMERICAN_EXPRESS']},"\
    f"{credit_dict['FLAG_OTHER_CARDS']},{credit_dict['QUANT_BANKING_ACCOUNTS']},{credit_dict['PERSONAL_ASSETS_VALUE']},"\
    f"{credit_dict['QUANT_CARS']},{credit_dict['COMPANY']},{credit_dict['FLAG_PROFESSIONAL_PHONE']},{credit_dict['MONTHS_IN_THE_JOB']},"\
    f"{credit_dict['PROFESSION_CODE']},{credit_dict['OCCUPATION_TYPE']},{credit_dict['PRODUCT']},{credit_dict['AGE']},"\
    f"{credit_dict['RESIDENCIAL_ZIP_3']}")

if __name__ == "__main__":
    uvicorn.run("fastapi_code:app",host="0.0.0.0", port=800)
