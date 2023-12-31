# Generated by Django 4.2.1 on 2023-07-16 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0003_alter_comment_comment_text_alter_comment_rating_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="category", new_name="categories",
        ),
        migrations.AlterField(
            model_name="author",
            name="author",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="news.author"
            ),
        ),
    ]
