"""add base recipe

Revision ID: 68807db6ba87
Revises: 416ecf2a0079
Create Date: 2023-12-08 03:40:20.657505

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = '68807db6ba87'
down_revision = '416ecf2a0079'
branch_labels = None
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('recipe', 'recipe_ingredient'))
    recipe = Table('recipe', meta)
    ingredients = Table('recipe_ingredient', meta)
    
    op.execute(
        recipe.insert()
        .values(id='1', name='Strogonoff de Frango', instruction='Placeholder')
    )

    op.bulk_insert(ingredients,
                   [
                       {'recipe_id': 1, 'ingredient_id': 14, 'quantity': 1000}, # Frango
                       {'recipe_id': 1, 'ingredient_id': 4, 'quantity': 40},    # Cebola
                       {'recipe_id': 1, 'ingredient_id': 5, 'quantity': 30},    # Manteiga
                       {'recipe_id': 1, 'ingredient_id': 8, 'quantity': 45},    # Ketchup
                       {'recipe_id': 1, 'ingredient_id': 6, 'quantity': 30},    # Mostarda
                       {'recipe_id': 1, 'ingredient_id': 9, 'quantity': 100},   # Champignon
                       {'recipe_id': 1, 'ingredient_id': 13, 'quantity': 200},  # Creme de leite
                       {'recipe_id': 1, 'ingredient_id': 10, 'quantity': 40}    # Batata palha
                   ])
    
    op.execute("SELECT setval('recipe_id_seq'::regclass, (SELECT max(id)::bigint from recipe));")

    pass


def downgrade():
    op.execute('DELETE FROM recipe_ingredient WHERE true')
    op.execute('DELETE FROM recipe WHERE true')
    pass
