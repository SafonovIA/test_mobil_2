import os
from github import Github, Auth
from dotenv import load_dotenv


# Загрузка переменных
load_dotenv()

# Получение переменных
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

# Создание объекта Github с использованием токена и получение пользователя
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)
user = g.get_user()

# Создание репозитория
def create_repo():
    user.create_repo(
        name=REPO_NAME,
        description="New repo",
        private=False
    )

# Проверка репозитория
def chek_repo():
    repos = user.get_repos()
    for repo in repos:
        if repo.name == REPO_NAME:
            return True
    return False

# Удаление репозитория
def delet_repo():
    repo = user.get_repo(REPO_NAME)
    repo.delete()



# Тестирование API
def test_git_api():
    assert not chek_repo()
    create_repo()
    assert chek_repo()
    delet_repo()
    assert not chek_repo()
