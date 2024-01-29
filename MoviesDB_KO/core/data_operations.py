import datetime

import requests
from core.models import Actors, Directors, Movies
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from core.utils import cache_response

class DatabaseOperations(BaseCommand):
    # This class contains all the functions aplicable to local database version of text client
    def add_actor(self, name: str, date_of_birth=None, latest_movie=None):
        # Function responsible for adding an actor
        try:
            self.name = name
            try:
                self.date_of_birth = datetime.datetime.strptime(
                    date_of_birth, '%Y-%m-%d').date()
            except TypeError:
                self.date_of_birth = None
            self.latest_movie = latest_movie

            actor: Actors = Actors.objects.create(
                name=self.name,
                date_of_birth=self.date_of_birth,
                latest_movie=self.latest_movie
            )
            self.stdout.write(self.style.SUCCESS(
                f"Successfully added {self.name} to the database!"))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields weren't given, you need to pass the name at least"))

    def get_actors(self) -> list:
        # Function responsible for getting data about all the actors in database
        actors: Actors = Actors.objects.all()
        return [{'id': actor.id,
                 'name': actor.name,
                 'date_of_birth': actor.date_of_birth,
                 'latest_movie': actor.latest_movie} for actor in actors]

    def delete_actor(self, actor_id: int):
        # Function responsible for deleting an actor from the database
        actor_to_delete: Actors = Actors.objects.get(id=actor_id)
        actor_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(
            f"Successfully deleted actor no. {actor_id} from database!"))

    def get_movies_for_actor(self, actor_id: int) -> list:
        # Function responsible for getting data about movies that include acting performance of a chosen actor
        actor: Actors = Actors.objects.get(id=actor_id)
        movies: Movies = Movies.objects.filter(lead_actor=actor)
        return [{'title': movie.title,
                 'premiere_date': movie.premiere_date,
                 'director': movie.director.name,
                 'academy_awards': movie.academy_awards}
                for movie in movies]

    def add_director(self, name: str, date_of_birth=None, latest_movie=None):
        # Function responsible for adding a director to the database
        try:
            self.name = name
            try:
                self.date_of_birth = datetime.datetime.strptime(
                    date_of_birth, '%Y-%m-%d').date()
            except TypeError:
                self.date_of_birth = None
            self.latest_movie = latest_movie

            director: Directors = Directors.objects.create(
                name=self.name,
                date_of_birth=self.date_of_birth,
                latest_movie=self.latest_movie
            )

            self.stdout.write(self.style.SUCCESS(
                f"Successfully added {self.name} to the database!"))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields weren't given, you need to pass the name at least"))

    def get_directors(self) -> list:
        # Function responsible for getting data about all directors in the database
        directors: Directors = Directors.objects.all()
        return [{'id': director.id,
                 'name': director.name,
                 'date_of_birth': director.date_of_birth,
                 'latest_movie': director.latest_movie} for director in directors]

    def delete_director(self, director_id: int):
        # Function responsible for deleting a director from the database
        director_to_delete: Directors = Directors.objects.get(id=director_id)
        director_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(
            f"Successfully deleted director no. {director_id} from database!"))

    def get_movies_for_director(self, director_id: int) -> list:
        # Function responsible for getting data about all the movies directed by a selected director in the database
        director: Directors = Directors.objects.get(id=director_id)
        movies: Movies = Movies.objects.filter(director=director)
        return [{'title': movie.title,
                 'premiere_date': movie.premiere_date,
                 'lead_actor': movie.lead_actor.name,
                 'academy_awards': movie.academy_awards}
                for movie in movies]

    def add_movie(self, title: str, lead_actor_given: str, director_given: str, premiere_date=None, category=None, academy_awards=None):
        # Function responsible for adding a movie to the database
        try:
            self.title = title
            self.premiere_date = premiere_date
            self.director_given = director_given
            self.category = category
            self.lead_actor_given = lead_actor_given
            self.academy_awards = academy_awards

            self.director, created = Directors.objects.get_or_create(
                name=self.director_given)
            self.lead_actor, created = Actors.objects.get_or_create(
                name=self.lead_actor_given)

            movie: Movies = Movies.objects.create(
                title=self.title,
                premiere_date=self.premiere_date,
                director=self.director,
                category=self.category,
                lead_actor=self.lead_actor,
                academy_awards=self.academy_awards
            )

            self.stdout.write(self.style.SUCCESS(
                f'Successfully added movie "{title}" to the database!'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(
                'Manditory fields werent covered while trying to create a new movie record: Title, director and actor is at least needed!'))
        except Actors.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                'Actor given doesnt exist in the Database'))
        except Directors.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                'Director given doesnt exist in the Database'))

    def get_movies(self) -> list:
        # Function responsible for getting data about all the movies in the database
        movies: Movies = Movies.objects.all()
        return [{'id': movie.id,
                 'title': movie.title,
                 'premiere_date': movie.premiere_date,
                 'category': movie.category,
                 'director': movie.director,
                 'lead_actor': movie.lead_actor,
                 'academy_awards': movie.academy_awards} for movie in movies]

    def delete_movie(self, movie_id: int):
        # Function responsible for deleting a movie from the database
        movie_to_delete: Movies = Movies.objects.get(id=movie_id)
        movie_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(
            f"Successfully deleted movie no. {movie_id} from database!"))


class ApiOperations(BaseCommand):
    # This class contains all the functions aplicable to the api mode in text client
    API_BASE_URL = "http://127.0.0.1:8000"

<<<<<<< HEAD
    @cache_response(timeout=60) # api requests will be stored in local cache for 60 seconds
    def add_actor(self, name, date_of_birth=None, latest_movie=None):
        actor_data = {
=======
    def add_actor(self, name: str, date_of_birth=None, latest_movie=None):
        # Function responsible for adding an actor through api
        actor_data: dict = {
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
            'name': name,
            'date_of_birth': date_of_birth,
            'latest_movie': latest_movie
        }
        response = requests.post(
            f"{self.API_BASE_URL}/actors/", data=actor_data)

        if response.status_code == 201:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully added {name} to the Database"))
            return response.json()
        elif response.status_code == 500:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields werent given in the input!"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
    @cache_response(timeout=60)
    def get_actors(self):
        response = requests.get(f"{self.API_BASE_URL}/actors/")
        # Function responsible for getting data about all the actors in database through api
        if response.status_code == 200:
            return response.json()
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def delete_actor(self, actor_id):
=======

    def delete_actor(self, actor_id: int):
        # Function responsible for deleting an actor from the database through api
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.delete(f"{self.API_BASE_URL}/actors/{actor_id}/")

        if response.status_code == 204:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully deleted actor {actor_id} from the Database."))
        elif response.status_code == 404:
            self.stdout.write(self.style.ERROR(
                "There is no actors with given index"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def get_movies_for_actor(self, actor_id):
=======

    def get_movies_for_actor(self, actor_id: int):
        # Function responsible for getting data through api about movies that include acting performance of a chosen actor
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.get(
            f"{self.API_BASE_URL}/actors/{actor_id}/movies/")
        if response.status_code == 200:
            movie_info = response.json()
            for movie in movie_info:
                director = requests.get(
                    f"{self.API_BASE_URL}/directors/{movie['director']}/")
                movie['director'] = director.json()['name']
            return movie_info
        elif response.status_code == 404:
            self.stdout.write(self.style.ERROR(
                f"No movies found for actor with ID {actor_id}."))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def add_director(self, name, date_of_birth=None, latest_movie=None):
        director_data = {
=======

    def add_director(self, name: str, date_of_birth=None, latest_movie=None):
        # Function responsible for adding a director to the database through api
        director_data: dict = {
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
            'name': name,
            'date_of_birth': date_of_birth,
            'latest_movie': latest_movie
        }
        response = requests.post(
            f"{self.API_BASE_URL}/directors/", data=director_data)

        if response.status_code == 201:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully added {name} to the database"))
            return response.json()
        elif response.status_code == 500:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields werent given in the input!"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
    @cache_response(timeout=60)
    def get_directors(self):
        # Function responsible for getting data about all directors in the database through api
        response = requests.get(f"{self.API_BASE_URL}/directors/")

        if response.status_code == 200:
            return response.json()
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def delete_director(self, director_id):
=======

    def delete_director(self, director_id: int):
        # Function responsible for deleting a director from the database through api
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.delete(
            f"{self.API_BASE_URL}/directors/{director_id}/")

        if response.status_code == 204:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully deleted director {director_id} from the Database."))
        elif response.status_code == 404:
            self.stdout.write(self.style.ERROR(
                "There is no directors with given index"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def get_movies_for_director(self, director_id):
=======

    def get_movies_for_director(self, director_id: int):
        # Function responsible for getting data through api about all the movies directed by a selected director in the database
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.get(
            f"{self.API_BASE_URL}/directors/{director_id}/movies/")
        if response.status_code == 200:
            movie_info = response.json()
            for movie in movie_info:
                lead_actor = requests.get(
                    f"{self.API_BASE_URL}/actors/{movie['lead_actor']}/")
                movie['lead_actor'] = lead_actor.json()['name']
            return movie_info
        elif response.status_code == 404:
            self.stdout.write(self.style.ERROR(
                f"No movies found for director with ID {director_id}."))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
<<<<<<< HEAD
    @cache_response(timeout=60)
    def get_or_create(self, person_name, person_type):
=======

    def get_or_create(self, person_name: str, person_type: str):
        # Function that either gets data through api about an actor or director if a person of given name exists, if not it creates a person with that name
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.get(
            f"{self.API_BASE_URL}/{person_type}/{person_name}/")
        if response.status_code == 200:
            return response.json()['id']
        elif response.status_code == 404:
            person_data: dict = {'name': person_name}
            response = requests.post(
                f"{self.API_BASE_URL}/{person_type}/", data=person_data)
            if response.status_code == 201:
                return response.json()['id']
            else:
                raise Exception(f"Failed to create a {person_type} object, status code: {
                                response.status_code}")
        else:
            raise Exception(f"Unexpected exceptio when trying to get or create a {
                            person_type} object, status code: {response.status_code}")
<<<<<<< HEAD
        
    @cache_response(timeout=60)
    def add_movie(self, title, lead_actor_given, director_given, premiere_date=None, category=None, academy_awards=None):
=======

    def add_movie(self, title: str, lead_actor_given: str, director_given: str, premiere_date=None, category=None, academy_awards=None):
        # Function responsible for adding a movie to the database through api
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        try:
            director = self.get_or_create(director_given, "directors")
            lead_actor = self.get_or_create(lead_actor_given, "actors")
            movie_data: dict = {
                'title': title,
                'premiere_date': premiere_date,
                'director': director,
                'lead_actor': lead_actor,
                'category': category,
                'academy_awards': academy_awards
            }
        except KeyError:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields werent given in the input!"))
            return 0

        response = requests.post(
            f"{self.API_BASE_URL}/movies/", data=movie_data)

        if response.status_code == 201:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully added {title} to the database or API!"))
            return response.json()
        elif response.status_code == 500:
            self.stdout.write(self.style.ERROR(
                "Mandatory fields werent given in the input!"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
            
    @cache_response(timeout=60)
    def get_movies(self):
        # Function responsible for getting data through api about all the movies in the database
        response = requests.get(f"{self.API_BASE_URL}/movies/")

        if response.status_code == 200:
            movies = response.json()
            for movie in movies:
                director_name = requests.get(
                    f"{self.API_BASE_URL}/directors/{movie['director']}/")
                actor_name = requests.get(
                    f"{self.API_BASE_URL}/actors/{movie['lead_actor']}/")
                if director_name.status_code==200:
                    director_name = director_name.json()['name']
                else:
                    director_name = None
                if actor_name.status_code==200:
                    actor_name = actor_name.json()['name']
                else:
                    actor_name = None
                movie['director'] = director_name
                movie['lead_actor'] = actor_name
            return movies
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))

<<<<<<< HEAD
    @cache_response(timeout=60)
    def delete_movie(self, movie_id):
=======
    def delete_movie(self, movie_id: int):
        # Function responsible for deleting a movie from the database through api
>>>>>>> 080d626318b1fab90ccf1653b7b511d6696e5857
        response = requests.delete(f"{self.API_BASE_URL}/movies/{movie_id}/")

        if response.status_code == 204:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully deleted movie {movie_id} from the Database."))
        elif response.status_code == 404:
            self.stdout.write(self.style.ERROR(
                "There is no directors with given index"))
        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}"))
