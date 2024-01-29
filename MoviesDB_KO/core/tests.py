from django.test import TestCase
from core.data_operations import ApiOperations, DatabaseOperations
from core.models import Actors, Movies


class TestApiOperations(TestCase):
    def setUp(self):
        self.database_operations = ApiOperations()

    def test_add_director(self):
        director_name = 'John Doe'
        director = self.database_operations.add_director(name=director_name)
        directors = self.database_operations.get_directors()
        self.assertIn(director, directors)
        self.database_operations.delete_director(director['id'])

    def test_delete_director(self):
        director_name = 'John Doe'
        director = self.database_operations.add_director(name=director_name)
        self.database_operations.delete_director(director['id'])
        directors = self.database_operations.get_directors()
        self.assertNotIn(director, directors)

    def test_getting_movies_for_director(self):
        director_name = 'John Doe'
        director = self.database_operations.add_director(name=director_name)
        movie_title = 'Test Movie'
        lead_actor_name = 'Test Actor'
        movie = self.database_operations.add_movie(
            title=movie_title, lead_actor_given=lead_actor_name, director_given=director_name
        )
        movies = self.database_operations.get_movies_for_director(director['id'])
        self.assertTrue(any(movie['title'] == movie_title for movie in movies))
        self.database_operations.delete_director(director['id'])
        self.database_operations.delete_movie(movie['id'])


class TestDatabaseOperations(TestCase):
    def setUp(self):
        self.database_operations = DatabaseOperations()

    def test_add_actor(self):
        # Adding actor test
        actor_name = "John Doe"
        self.database_operations.add_actor(name=actor_name)
        self.assertTrue(Actors.objects.filter(name=actor_name).exists())

    def test_add_delete_actor(self):
        # deleting actor test
        actor_name = "John Doe"
        self.database_operations.add_actor(name=actor_name)
        actor = Actors.objects.get(name=actor_name)
        self.database_operations.delete_actor(actor.id)
        self.assertFalse(Actors.objects.filter(name=actor_name).exists())

    def test_movie_from_actor(self):
        # Adding a movie did by an actor and then checking if this movies will be shown
        self.database_operations.add_movie(title="Test Movie", lead_actor_given="Test Actor", director_given="Test Director")
        self.assertTrue(Movies.objects.filter(title="Test Movie").exists())
        actor = Actors.objects.get(name="Test Actor")
        movies = self.database_operations.get_movies_for_actor(actor.id)
        self.assertEqual("Test Movie", movies[0]["title"])