# Задание "Свой YouTube":
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return self.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # Заголовок
        self.duration = duration  # Продолжительность
        self.time_now = time_now  # Секунда остановки
        self.adult_mode = adult_mode  # Ограничение по возрасту


class UrTube:
    def __init__(self):
        self.users = []  # Список объектов User (nickname, password, age)
        self.current_user = None  # Текущий User (his nickname)
        self.videos = []  # Список объектов Video

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        for i in self.users:
            if i[0] == self.nickname and i[1] == self.password:
                self.current_user = self.nickname
                break

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.user = [self.nickname, self.password, self.age]
        for i in self.users:
            if i[0] == self.nickname:  # проверка имени пользователя
                print(f"Пользователь {self.nickname} уже существует")
                self.log_in(self.nickname, self.password)  # авторизация
                break
        self.users.append(self.user)
        self.current_user = self.nickname

    def log_out(self, current_user):
        self.current_user = current_user
        #self.current_user = None


    def add(self, *args):
        for i in args:
            video = [i.title, i.duration, i.time_now, i.adult_mode]
            if not self.videos:  # если каталог videos пуст добавляем первый фильм
                self.videos.append(video)
                continue
            else:
                for j in self.videos:
                    if i.title == j[0]:
                        print(f"фильм {i.title} уже существует !!! ")
                        break
                self.videos.append(video)

    def get_videos(self, search_video):
        self.search_video = search_video.lower()
        self.my_search_list = []
        for i in self.videos:
            my_str = i[0]
            self.my_str = my_str.lower()
            if self.my_str.find(self.search_video) != -1:
                self.my_search_list.append(i[0])
        return self.my_search_list

    def watch_video(self, get_video):
        self.get_video = get_video
        if self.current_user != None:  # Проверка авторизации пользователя

            """ Выбор видео """
            for i in self.videos:
                if i[0] == self.get_video and i[3] == True:
                    self.current_duration = i[1]
                    self.current_time_now = i[2]

                    """Проверка возраста и прокрутка видео"""

                    if self.age > 18:
                        print(f"Старт видео: {self.get_video}")
                        for j in range(self.current_duration):
                            self.current_time_now = j
                            print(self.current_time_now + 1, " ", end="")
                            time.sleep(1)
                        print("Конец видео")
                    else:
                        print("Вам нет 18. Пожалуйста, покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
        self.log_out(self.current_user)



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
