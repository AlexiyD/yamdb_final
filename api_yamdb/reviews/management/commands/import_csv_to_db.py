import csv
import os

from django.core.management.base import BaseCommand
from reviews.models import (Category, Comment, Genre, Review, Title,
                            TitleGenre, User)

from api_yamdb.settings import BASE_DIR

CATEGORY = 'category.csv'
COMMENTS = 'comments.csv'
GENRE_TITLE = 'genre_title.csv'
GENRE = 'genre.csv'
REVIEW = 'review.csv'
TITLES = 'titles.csv'
USERS = 'users.csv'


class Command(BaseCommand):

    def csv_file_path(self, file_name):
        return os.path.join(BASE_DIR, 'static/data/', file_name)

    def category_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    Category.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        slug=row[2],
                    )
                row_number += 1

    def genre_title_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    TitleGenre.objects.get_or_create(
                        id=row[0],
                        title_id=row[1],
                        genre_id=row[2],
                    )
                row_number += 1

    def genre_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    Genre.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        slug=row[2],
                    )
                row_number += 1

    def title_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    Title.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        year=row[2],
                        category_id=row[3]
                    )
                row_number += 1

    def users_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    User.objects.get_or_create(
                        id=row[0],
                        username=row[1],
                        email=row[2],
                        role=row[3],
                        bio=row[4],
                        first_name=row[5],
                        last_name=row[6]
                    )
                row_number += 1

    def review_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    Review.objects.get_or_create(
                        id=row[0],
                        title_id=row[1],
                        text=row[2],
                        author_id=row[3],
                        score=row[4],
                        pub_date=row[5]
                    )
                row_number += 1

    def comments_db_entries(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            row_number = 0
            for row in reader:
                if row_number != 0:
                    Comment.objects.get_or_create(
                        id=row[0],
                        review_id=row[1],
                        text=row[2],
                        author_id=row[3],
                        pub_date=row[4]
                    )
                row_number += 1

    def handle(self, *args, **kwargs):
        category_csv_file = self.csv_file_path(CATEGORY)
        self.category_db_entries(category_csv_file)

        ganre_csv_file = self.csv_file_path(GENRE)
        self.genre_db_entries(ganre_csv_file)

        titles_csv_file = self.csv_file_path(TITLES)
        self.title_db_entries(titles_csv_file)

        genre_title_csv_file = self.csv_file_path(GENRE_TITLE)
        self.genre_title_db_entries(genre_title_csv_file)

        users_csv_file = self.csv_file_path(USERS)
        self.users_db_entries(users_csv_file)

        review_csv_file = self.csv_file_path(REVIEW)
        self.review_db_entries(review_csv_file)

        comments_csv_file = self.csv_file_path(COMMENTS)
        self.comments_db_entries(comments_csv_file)
