# Generated by Django 3.1.7 on 2021-03-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField()),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('estoque', models.IntegerField()),
            ],
        ),
    ]
