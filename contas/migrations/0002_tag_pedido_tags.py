# Generated by Django 4.1.4 on 2022-12-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='tags',
            field=models.ManyToManyField(to='contas.tag'),
        ),
    ]
