# Generated by Django 2.1.10 on 2019-11-17 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Address')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]