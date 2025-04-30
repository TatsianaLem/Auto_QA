from base_requests import CompanyApi, EmployeeApi, base_url

def test_create_employee():
    company_api = CompanyApi(base_url)
    emp_api = EmployeeApi(base_url)

    company = company_api.create_company("Компания QA", "для теста")
    company_id = company['id']

    email = "anna@example.com"
    emp = emp_api.create_employee(
        first_name="Анна",
        last_name="Тестова",
        company_id=company_id,
        email=email,
        phone="+79990000001",
        birthdate="1991-03-15"
    )

    assert emp['first_name'] == "Анна"
    assert emp['last_name'] == "Тестова"
    assert emp['email'] == email
    assert emp['company_id'] == company_id


def test_get_employee():
    company_api = CompanyApi(base_url)
    emp_api = EmployeeApi(base_url)

    company = company_api.create_company("TestComp", "")
    company_id = company['id']

    email = "ivan@example.com"
    emp = emp_api.create_employee(
        first_name="Иван",
        last_name="Кириллов",
        company_id=company_id,
        email=email,
        phone="+79991112233",
        birthdate="1988-07-07"
    )

    emp_id = emp['id']
    info = emp_api.get_employee(emp_id)

    assert info['first_name'] == "Иван"
    assert info['last_name'] == "Кириллов"
    assert info['email'] == email
    assert info['company_id'] == company_id


def test_update_employee():
    company_api = CompanyApi(base_url)
    emp_api = EmployeeApi(base_url)

    company = company_api.create_company("TestUpdate", "")
    company_id = company['id']

    emp = emp_api.create_employee(
        first_name="Мария",
        last_name="Смирнова",
        company_id=company_id,
        email="maria@example.com",
        phone="+79993334455",
        birthdate="1993-09-09"
    )

    emp_id = emp['id']
    new_email = "maria.new@example.com"
    new_phone = "+79990001122"

    updated = emp_api.update_employee(emp_id, {
        "email": new_email,
        "phone": new_phone
    })

    assert updated['email'] == new_email
    assert updated['phone'] == new_phone
