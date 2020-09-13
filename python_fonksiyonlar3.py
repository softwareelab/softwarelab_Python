def func(**kwargs):
    print("Kullanıcı Adı:", kwargs.get('username'))
    print("Parola:", kwargs.get('password'))

func(username='softwarelab', password='deneme123')