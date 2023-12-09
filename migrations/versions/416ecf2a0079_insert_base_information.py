"""insert base information

Revision ID: 416ecf2a0079
Revises: 
Create Date: 2023-12-05 05:17:20.891507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

# revision identifiers, used by Alembic.
revision = '416ecf2a0079'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    meta.reflect(only=('ingredient', 'ingredient_information'))
    ingredient = Table('ingredient', meta)
    ingredient_info = Table('ingredient_information', meta)
    op.bulk_insert(ingredient,
                   [
                        {'id': 1, 'name': 'Ovo'},
                        {'id': 2, 'name': 'Milho'},
                        {'id': 3, 'name': 'Carne de patinho'},
                        {'id': 4, 'name': 'Cebola'},
                        {'id': 5, 'name': 'Manteiga'},
                        {'id': 6, 'name': 'Mostarda'},
                        {'id': 7, 'name': 'Alho'},
                        {'id': 8, 'name': 'Ketchup'},
                        {'id': 9, 'name': 'Champignon'},
                        {'id': 10, 'name': 'Batata palha'},
                        {'id': 11, 'name': 'Leite'},
                        {'id': 12, 'name': 'Brócolis'},
                        {'id': 13, 'name': 'Creme de leite'},
                        {'id': 14, 'name': 'Frango'},
                        {'id': 15, 'name': 'Arroz branco'}
                   ])
    
    op.bulk_insert(ingredient_info,
                   [
                       {
                           'ingredient_id': 1,
                           'calories': 143.00,
                           'proteins': 13,
                           'fats': 8.9,
                           'carbohydrates': 1.6
                        },
                        {
                           'ingredient_id': 2,
                           'calories': 146.20,
                           'proteins': 6.60,
                           'fats': 0.60,
                           'carbohydrates': 28.60
                        },
                       {
                           'ingredient_id': 3,
                           'calories': 219,
                           'proteins': 35.9,
                           'fats': 7.31,
                           'carbohydrates': 0
                        },
                        {
                            'ingredient_id': 4,
                            'calories': 39.00,
                            'proteins': 1.70,
                            'fats': 0.10,
                            'carbohydrates': 8.90
                        },
                        {
                            'ingredient_id': 5,
                            'calories': 117.00,
                            'proteins': 0.85,
                            'fats': 81.11,
                            'carbohydrates': 0.06
                        },
                        {
                            'ingredient_id': 6,
                            'calories': 67.00,
                            'proteins': 4.37,
                            'fats': 4.01,
                            'carbohydrates': 5.33
                        },
                        {
                            'ingredient_id': 7,
                            'calories': 113.00,
                            'proteins': 7.00,
                            'fats': 0.20,
                            'carbohydrates': 23.90
                        },
                        {
                            'ingredient_id': 8,
                            'calories': 104.00,
                            'proteins': 1.53,
                            'fats': 0.36,
                            'carbohydrates': 27.30
                        },
                        {
                            'ingredient_id': 9,
                            'calories': 50.74,
                            'proteins': 1.87,
                            'fats': 3.20,
                            'carbohydrates': 5.09
                        },
                        {
                            'ingredient_id': 10,
                            'calories': 572.00,
                            'proteins': 6,
                            'fats': 40.00,
                            'carbohydrates': 44.00
                        },
                        {
                            'ingredient_id': 11,
                            'calories': 56.50,
                            'proteins': 3.00,
                            'fats': 2.0,
                            'carbohydrates': 4.4
                        },
                        {
                            'ingredient_id': 12,
                            'calories': 24.60,
                            'proteins': 2.10,
                            'fats': 0.30,
                            'carbohydrates': 4.4
                        },
                        {
                            'ingredient_id': 13,
                            'calories': 253.30,
                            'proteins': 0.00,
                            'fats': 16.0,
                            'carbohydrates': 0.00
                        },
                        {
                            'ingredient_id': 14,
                            'calories': 182.00,
                            'proteins': 17.00,
                            'fats': 4.0,
                            'carbohydrates': 0.00
                        },
                        {
                            'ingredient_id': 15,
                            'calories': 130.00,
                            'proteins': 2.69,
                            'fats': 0.28,
                            'carbohydrates': 28.17
                        }
                   ])
    pass


def downgrade():
    op.execute('DELETE FROM ingredient_information WHERE true')
    op.execute('DELETE FROM ingredient WHERE true')
    pass
