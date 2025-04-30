import requests

base_url = 'http://5.101.50.27:8000'


class CompanyApi:
    def __init__(self, url):
        self.url = url

    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        resp = requests.post(self.url + "/auth/login", json=creds)
        assert resp.status_code == 200, 'неожиданный статус ответа при логине'
        return resp.json()['user_token']

    def create_company(self, name, description=""):
        company = {'name': name, 'description': description}
        resp = requests.post(self.url + "/company/create", json=company)
        assert resp.status_code == 201, 'неожиданный статус при создании компании'
        return resp.json()

    def get_company(self, company_id):
        resp = requests.get(f"{self.url}/company/{company_id}")
        assert resp.status_code in (200, 404)
        return resp.json()

    def delete_company(self, company_id):
        token = self.get_token()
        resp = requests.delete(f"{self.url}/company/{company_id}?client_token={token}")
        assert resp.status_code == 200
        return resp.json()


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        resp = requests.post(self.url + "/auth/login", json=creds)
        assert resp.status_code == 200, 'неожиданный статус при логине'
        return resp.json()['user_token']

    def create_employee(self, first_name, last_name, company_id, email, phone, birthdate):
        token = self.get_token()
        employee = {
            'first_name': first_name,
            'last_name': last_name,
            'company_id': company_id,
            'email': email,
            'phone': phone,
            'birthdate': birthdate,
            'is_active': True
        }
        resp = requests.post(f"{self.url}/employee/create/?client_token={token}", json=employee)
        assert resp.status_code == 200, f"Ошибка создания сотрудника: {resp.text}"
        return resp.json()

    def get_employee(self, employee_id):
        resp = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert resp.status_code in (200, 404)
        return resp.json()

    def update_employee(self, employee_id, data: dict):
        token = self.get_token()
        resp = requests.patch(f"{self.url}/employee/change/{employee_id}/?client_token={token}", json=data)
        assert resp.status_code == 200, f"Ошибка обновления сотрудника: {resp.text}"
        return resp.json()
