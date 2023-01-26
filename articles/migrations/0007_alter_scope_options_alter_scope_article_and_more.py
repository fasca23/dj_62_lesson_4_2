# Generated by Django 4.1.5 on 2023-01-26 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_scopes_tag_articles_alter_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='статьи'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя тега'),
        ),
    ]