import os
import django

# 初始化 Django 环境（必须写在最前面）
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from core.models import Topic, Entry  # 你的模型路径

# 初始化 faker
fake = Faker(locale="zh_CN")  # 中文数据


def create_test_data():
    # 1. 先创建一个测试用户
    user, created = User.objects.get_or_create(
        username="testuser",
        defaults={"email": "test@example.com", "password": "123456"}
    )

    # 2. 批量创建 10 个主题
    for _ in range(10):
        topic = Topic.objects.create(
            text=fake.sentence(nb_words=4),  # 随机4个词的标题
            owner=user
        )

        # 3. 每个主题下创建 3~6 条笔记
        for _ in range(fake.random_int(min=3, max=6)):
            Entry.objects.create(
                text=fake.text(max_nb_chars=200),  # 随机长文本
                topic=topic
            )

    print("✅ 批量数据创建完成！")
    print(f"用户：{user.username}")
    print(f"已创建 10 个主题 + 每个主题 3~6 条笔记")


if __name__ == '__main__':
    create_test_data()