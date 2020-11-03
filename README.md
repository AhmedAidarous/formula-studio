# formula-studio
A CMS for yoga and fitness studios written in Django.

The aim of this project is to create a CMS for managing subscriptions, single visits and purchases for gyms, yoga studios. This project is a result of frustration with available expensive CMS services, while open source variants seem to be very complex with functionality that I did not need anyways. It is largely a learn-as-you go along process, given that this is my fist Django app. But this software is already being actively used as the main accounting tool at one studio in Russia, [Formula Yoga](https://www.formulayoga.com/).   

It seeks to have minimal dependencies and preferably based on Django, specifically around its already integrated admin interface, for easy deployment. Some front-end elements could eventually be written in React. 


## Installation 
 
### On Linux and macOS

For installation, make sure yoy have `python3` and `pip3` installed. Clone repo

```
$ git clone https://github.com/mbrav/formula-studio
cd formula-studio
```

Setup a local python environment:

```
$ python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
$ pip3 install -r requirements.txt
```

Setup Django database and migrations:

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Setup an admin user:

```
$ python3 manage.py createsuperuser
```

Run server

```
$ python3 manage.py runserver
```

Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Development

This project is in still in alpha phase of development and goals will be fully established before the beta release.

Django admin interface in [alpha version](https://github.com/mbrav/formula-studio/releases/tag/alpha):
![](https://i.imgur.com/PBsBs1c.png) 

Database Model structure in [alpha version](https://github.com/mbrav/formula-studio/releases/tag/alpha):
![](https://i.imgur.com/r57wa1O.png) 

### Development Roadmap

#### *αιρha*
- [x] Basic database back-end polished, suitable for limited practical usage
- [ ] Add settings/configuration page to admin
- [ ] A model with to-register user who signed up for a class
- [x] Hacked together scripts for importing data
	- [ ] Publish as `jupyter` notebooks) 

#### *βετα*
- [ ] Integration with Google Calendar
    - [ ] Poling events 
    - [ ] Custom variables for integration 
- [ ] Tie Django's authentication models to user models
- [ ] Finance
	- [ ] Polished reports
	- [ ] Wage calculation tools 
	- [ ] Expenses, revenue
	- [ ] Graphs using [`django-admin-charts`](https://github.com/PetrDlouhy/django-admin-charts)
	- [ ] More efficient generation of statistics using [`Celery`](https://docs.celeryproject.org/en/stable/)
- [ ] Integrate all scripts into actual functionality  

#### *0.1*
- [ ] Front-end for class registration 
- [ ] Deployment setup

### Contributing

If you've found a bug, add a feature or improve formula-studio and think it is useful then please consider contributing. Patches, pull requests or just suggestions are always welcome!

- Source code: https://github.com/mbrav/formula-studio

- Bug tracker: https://github.com/mbrav/formula-studio/issues

- Project board manager: https://github.com/mbrav/formula-studio/projects/1

- Lastly, if you found this project helpful and practical, please leave some feedback!

