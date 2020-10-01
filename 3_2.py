# def user_data(name, surname, birth_year, city_of_residence, email, phone):
def user_data(name, **kwargs):
    print(name, kwargs)


user_data(name='Denis', surname='Spitcin', birth_year=1980, city_of_residence='Novosibirsk', email='spicindv@mail.ru',
          phone='+79773698377')
