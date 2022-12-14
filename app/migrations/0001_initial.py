# Generated by Django 4.1.3 on 2022-12-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail', models.EmailField(help_text='Enter email', max_length=254, verbose_name='Email')),
                ('phone', models.CharField(help_text='Enter phone number', max_length=150, verbose_name='Phone Number')),
                ('adress', models.CharField(help_text='Enter address', max_length=150, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter project name', max_length=150, verbose_name='Project name')),
                ('url', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter project url', verbose_name='Project URL')),
                ('image', models.ImageField(help_text='Upload image', upload_to='profile-images', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=150, verbose_name='Name')),
                ('image', models.ImageField(help_text='Upload image', upload_to='profile-images', verbose_name='Image')),
                ('age', models.IntegerField(help_text='Enter age', verbose_name='Age')),
                ('technologies', models.TextField(help_text='Enter technologies', verbose_name='Technologies')),
                ('job', models.CharField(help_text='Enter job', max_length=100, verbose_name='Job')),
                ('languages', models.TextField(default="O'zbek", help_text='Enter language', verbose_name='Languages')),
                ('resume', models.FileField(help_text='Upload resume', upload_to='resumes', verbose_name='Resume')),
                ('portfolio', models.IntegerField(default='1', help_text='Enter potfolios count', verbose_name='Portfolio Count')),
                ('profession', models.DecimalField(decimal_places=2, default='1.5', help_text='Enter profession year', max_digits=10, verbose_name='Profession Year')),
                ('projects', models.IntegerField(default='1', help_text='Enter projects count', verbose_name='Projects Count')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter telegram url', verbose_name='Telegram')),
                ('instagram', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter instagram url', verbose_name='Instagram')),
                ('tiktok', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter tiktok url', verbose_name='Tiktok')),
                ('facebook', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter facebook url', verbose_name='Facebook')),
                ('youtube', models.URLField(default='https://me.behzodasliddinov.uz', help_text='Enter youtube url', verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Social Link ',
                'verbose_name_plural': 'Social Links ',
            },
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
