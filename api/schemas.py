from fastapi import Form
from pydantic import BaseModel

class form(BaseModel):
    age: str
    mastercard: str
    payment_day: str
    application_submission_type: str
    postal_adress_type: str
    sex: str
    marital_status: str
    quant_dependants: int
    state_of_birth: str
    city_of_birth: str
    nacionality: str
    residencial_state: str
    residencial_city: str
    residencial_borough: str
    flag_residencial_phone: str
    residence_type: str
    months_in_residence: str
    flag_email: str
    personal_monthly_income: int
    other_incomes: str
    american_express: str
    visa: str
    diners: str
    others_cards: str
    quant_banking_accounts: str
    company: str
    residencial_phone_area_code: str
    personal_assets_value: str
    quant_cars: str
    flag_professional_phone: str
    months_in_job: str
    profession_code: str
    occupation_type: str
    product: str
    residencial_zip: str

    

    @classmethod
    def as_form(
        cls,
        age: str = Form(...),
        mastercard: str = Form(...),
        payment_day: str = Form(...),
        application_submission_type: str = Form(...),
        postal_adress_type:str = Form(...),
        sex: str = Form(...),
        marital_status: str = Form(...),
        quant_dependants: str = Form(...),
        state_of_birth: str = Form(...),
        city_of_birth: str = Form(...),
        nacionality: str = Form(...),
        residencial_state: str = Form(...),
        residencial_city: str = Form(...),
        residencial_borough: str = Form(...),
        flag_residencial_phone: str = Form(...),
        residence_type: str = Form(...),
        months_in_residence: str = Form(...),
        flag_email: str = Form(...),
        personal_monthly_income: int = Form(...),
        other_incomes: str = Form(...),
        american_express: str = Form(...),
        visa: str = Form(...),
        diners: str = Form(...),
        others_cards: str = Form(...),
        quant_banking_accounts: str = Form(...),
        company: str = Form(...),
        residencial_phone_area_code: str = Form(...),
        personal_assets_value: str = Form(...),
        quant_cars: str = Form(...),
        flag_professional_phone: str = Form(...),
        months_in_job: str = Form(...),
        profession_code: str = Form(...),
        occupation_type: str = Form(...),
        product: str = Form(...),
        residencial_zip: str = Form(...)

        
    ):

        return cls(
            age=age,
            mastercard=mastercard,
            payment_day=payment_day,
            application_submission_type=application_submission_type,
            postal_adress_type=postal_adress_type,
            sex=sex,
            marital_status=marital_status,
            quant_dependants=quant_dependants,
            state_of_birth=state_of_birth,
            city_of_birth=city_of_birth,
            nacionality=nacionality,
            residencial_state=residencial_state,
            residencial_city=residencial_city,
            residencial_borough=residencial_borough,
            flag_residencial_phone=flag_residencial_phone,
            residence_type=residence_type,
            months_in_residence=months_in_residence,
            flag_email=flag_email,
            personal_monthly_income=personal_monthly_income,
            other_incomes=other_incomes,
            american_express=american_express,
            visa=visa,
            diners=diners,
            others_cards=others_cards,
            quant_banking_accounts=quant_banking_accounts,
            company=company,
            residencial_phone_area_code=residencial_phone_area_code,
            personal_assets_value=personal_assets_value,
            quant_cars=quant_cars,
            flag_professional_phone=flag_professional_phone,
            months_in_job=months_in_job,
            profession_code=profession_code,
            occupation_type=occupation_type,
            product=product,
            residencial_zip=residencial_zip
            
        )

class login(BaseModel):
    
    firstname: str
    lastname: str
    username: str
    password_user: str

    @classmethod
    def as_login(
        cls,
        firstname: str = Form(...),
        lastname: str = Form(...),
        username: str = Form(...),
        password_user: str = Form(...),
    ):

        return cls(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password_user=password_user
        )

