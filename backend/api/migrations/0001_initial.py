# Generated by Django 3.1.3 on 2020-11-06 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('google_cal_id', models.CharField(blank=True, default='', max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Group Category',
                'verbose_name_plural': 'Group Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Item Category',
                'verbose_name_plural': 'Item Categories',
                'ordering': ('price',),
            },
        ),
        migrations.CreateModel(
            name='ItemPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Item Purchase',
                'verbose_name_plural': 'Item Purchases',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('writen_off', models.BooleanField(default=False, help_text='Set whether the payment should be written off from finances')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('method', models.CharField(choices=[('0', 'Cash'), ('1', 'Transfer'), ('2', 'Card')], default='0', max_length=2)),
                ('status', models.CharField(choices=[('0', 'Pending'), ('1', 'Paid')], default='1', help_text='Payment status', max_length=2)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('mobile_number', models.CharField(blank=True, max_length=11, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('group', models.CharField(blank=True, max_length=50, verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Signup',
                'verbose_name_plural': 'Singups',
            },
        ),
        migrations.CreateModel(
            name='SingleVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Single Visit',
                'verbose_name_plural': 'Single Visits',
                'ordering': ('-group__date',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'ordering': ('-registration_date',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('number_of_visits', models.PositiveIntegerField()),
                ('validity_in_days', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Subscription Category',
                'verbose_name_plural': 'Subscription Categories',
                'ordering': ('price',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('days', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Subscription Extension',
                'verbose_name_plural': 'Subscription Extensions',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='SubscriptionVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Subscription Visit',
                'verbose_name_plural': 'subscription Visits',
                'ordering': ('-group__date',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('mobile_number', models.CharField(max_length=11, unique=True, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('registered_on', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='img/member_profiles')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
                'ordering': ('last_name', 'first_name'),
            },
            bases=('api.userprofile',),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ('last_name', 'first_name'),
            },
            bases=('api.userprofile',),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['last_name', 'first_name'], name='api_userpro_last_na_d2809d_idx'),
        ),
        migrations.AddIndex(
            model_name='userprofile',
            index=models.Index(fields=['first_name'], name='first_name_idx'),
        ),
        migrations.AddField(
            model_name='subscriptionvisit',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_visits', to='api.group'),
        ),
        migrations.AddField(
            model_name='subscriptionvisit',
            name='subscription',
            field=models.ForeignKey(help_text='A visit based on a subscription', on_delete=django.db.models.deletion.CASCADE, related_name='subscription_visits', to='api.subscription'),
        ),
        migrations.AddField(
            model_name='subscriptionextension',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_extensions', to='api.subscription'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='api.payment'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='api.subscriptioncategory'),
        ),
        migrations.AddField(
            model_name='singlevisit',
            name='group',
            field=models.ForeignKey(help_text='Single visits that the group has', on_delete=django.db.models.deletion.CASCADE, related_name='single_visits', to='api.group'),
        ),
        migrations.AddField(
            model_name='singlevisit',
            name='payment',
            field=models.ForeignKey(help_text='Group to which a single visit occured', on_delete=django.db.models.deletion.CASCADE, related_name='single_visit', to='api.payment'),
        ),
        migrations.AddField(
            model_name='itempurchase',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.itemcategory'),
        ),
        migrations.AddField(
            model_name='itempurchase',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_purchases', to='api.payment'),
        ),
        migrations.AddField(
            model_name='group',
            name='category',
            field=models.ForeignKey(help_text='Category of the group', on_delete=django.db.models.deletion.CASCADE, related_name='group', to='api.groupcategory'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='member',
            field=models.ForeignKey(help_text='Subscriptions that the member has', on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='api.member'),
        ),
        migrations.AddField(
            model_name='singlevisit',
            name='member',
            field=models.ForeignKey(help_text='Single visits that the member has made', on_delete=django.db.models.deletion.CASCADE, related_name='single_visits', to='api.member'),
        ),
        migrations.AddField(
            model_name='signup',
            name='member',
            field=models.ForeignKey(blank=True, help_text='Payments that member has made', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signups', to='api.member'),
        ),
        migrations.AddField(
            model_name='payment',
            name='member',
            field=models.ForeignKey(help_text='Payments that member has made', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='api.member'),
        ),
        migrations.AddField(
            model_name='itempurchase',
            name='member',
            field=models.ForeignKey(help_text='Item purchases that the member has made', on_delete=django.db.models.deletion.CASCADE, related_name='item_purchases', to='api.member'),
        ),
        migrations.AddField(
            model_name='group',
            name='instructor',
            field=models.ForeignKey(help_text='Groups that the instructor leads', on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='api.instructor'),
        ),
    ]