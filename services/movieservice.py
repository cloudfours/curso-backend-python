from models.movie import Movies as MovieBd
from schema.model import Movie


class MovieService():
    def __init__(self, bd) -> None:
        self.bd = bd

    def get_movie(self):
        result = self.bd.query(MovieBd).all()
        return result

    def get_id_movie(self, id):
        result = self.bd.query(MovieBd).filter(MovieBd.id == id).first()
        return result

    def get_cat_movies(self, category):
        result = self.bd.query(MovieBd).filter(
            MovieBd.category == category).first()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieBd(**movie.dict())
        self.bd.add(new_movie)
        self.bd.commit()
        return

    def update_movie(self, id: int, update_movie: Movie):
        result = self.bd.query(MovieBd).filter(MovieBd.id == id).first()
        result.title = update_movie.title
        result.overview = update_movie.overview
        result.rating = update_movie.rating
        result.year = update_movie.year
        result.category = update_movie.category
        self.bd.commit()
        return
    def delete_movie(self,id:int):
        result=self.bd.query(MovieBd).filter(MovieBd.id==id).first()
        self.bd.delete(result)
        self.bd.commit()
        return
